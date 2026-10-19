import argparse

from models.user import User
from models.projects import Projects
from models.tasks import Tasks
from data.data import save_data, load_data


def main():
    parser = argparse.ArgumentParser(
        description="Project Management CLI"
    )

    parser.add_argument("entity", choices=["user", "project", "task"])
    parser.add_argument(
        "action",
        choices=[
            "add", "list", "show", "update", "delete",
            "complete", "remove-task", "remove-project"
        ]
    )

    parser.add_argument("--id")
    parser.add_argument("--name")
    parser.add_argument("--email")
    parser.add_argument("--owner")
    parser.add_argument("--title")
    parser.add_argument("--description")
    parser.add_argument("--due-date")
    parser.add_argument("--project")
    parser.add_argument("--task-id")
    parser.add_argument(
        "--status",
        choices=["not complete", "complete"]
    )

    args = parser.parse_args()

    load_data()



    if args.entity == "user":

        if args.action == "add":
            user = User.create_user(args.name, args.email)
            print("User created:", user.user_id)

        elif args.action == "list":
            for user in User._users.values():
                print(user.user_id, user.name, user.email)

        elif args.action == "show":
            user = User._users.get(args.id)

            if user:
                print(user)

        elif args.action == "update":
            user = User._users.get(args.id)

            if user:
                if args.name is not None:
                    user.name = args.name
                if args.email is not None:
                    user.email = args.email
                print("User updated.")

        elif args.action == "delete":
            user = User._users.get(args.id)

            if user:
                for project in Projects._projects.values():
                    if project.owner is user:
                        project.owner = None

                del User._users[args.id]
                print("User deleted.")

        elif args.action == "remove-project":
            user = User._users.get(args.id)

            if user and args.project:
                user.remove_project(args.project)

                project = Projects._projects.get(args.project)
                if project and project.owner is user:
                    project.owner = None

                print("Project removed from user.")

        else:
            print("Action not available for users.")


    elif args.entity == "project":

        if args.action == "add":
            owner = User._users.get(args.owner)

            if owner:
                project = Projects.create_project(
                    owner,
                    args.title,
                    args.description,
                    args.due_date
                )

                owner.add_projects(project.project_id)
                print("Project created:", project.project_id)

            else:
                print("Owner not found.")

        elif args.action == "list":
            for project in Projects._projects.values():
                owner_id = (
                    project.owner.user_id if project.owner else "None"
                )
                print(project.project_id, project.title, owner_id)

        elif args.action == "show":
            project = Projects._projects.get(args.id)

            if project:
                print("ID:", project.project_id)
                print("Title:", project.title)
                print("Description:", project.description)
                print("Due date:", project.due_date)
                print("Tasks:", project.tasks)

        elif args.action == "update":
            project = Projects._projects.get(args.id)

            if project:
                if args.owner is not None:
                    new_owner = User._users.get(args.owner)

                    if new_owner is None:
                        print("Owner not found.")
                        return

                    if project.owner:
                        project.owner.remove_project(project.project_id)

                    project.owner = new_owner
                    new_owner.add_projects(project.project_id)

                if args.title is not None:
                    project.title = args.title
                if args.description is not None:
                    project.description = args.description
                if args.due_date is not None:
                    project.due_date = args.due_date

                print("Project updated.")

        elif args.action == "delete":
            project = Projects._projects.get(args.id)

            if project:
                for user in User._users.values():
                    user.remove_project(project.project_id)

                for task in Tasks._tasks.values():
                    if task.assigned_to is project:
                        task.assigned_to = None

                del Projects._projects[args.id]
                print("Project deleted.")

        elif args.action == "remove-task":
            project = Projects._projects.get(args.id)

            if project and args.task_id:
                project.remove_task(args.task_id)

                task = Tasks._tasks.get(args.task_id)
                if task and task.assigned_to is project:
                    task.assigned_to = None

                print("Task removed from project.")

        else:
            print("Action not available for projects.")


    elif args.entity == "task":

        if args.action == "add":
            project = Projects._projects.get(args.project)

            if project:
                task = Tasks.create_task(
                    args.title,
                    args.status or "not complete",
                    project
                )

                project.add_task(task.task_id)
                print("Task created:", task.task_id)

            else:
                print("Project not found.")

        elif args.action == "list":
            for task in Tasks._tasks.values():
                project_id = (
                    task.assigned_to.project_id
                    if task.assigned_to else "None"
                )
                print(
                    task.task_id,
                    task.title,
                    task.status,
                    project_id
                )

        elif args.action == "show":
            task = Tasks._tasks.get(args.id)

            if task:
                print("ID:", task.task_id)
                print("Title:", task.title)
                print("Status:", task.status)
                print(
                    "Project:",
                    task.assigned_to.project_id
                    if task.assigned_to else "None"
                )

        elif args.action == "update":
            task = Tasks._tasks.get(args.id)

            if task:
                if args.title is not None:
                    task.title = args.title

                if args.status is not None:
                    task.status = args.status

                if args.project is not None:
                    project = Projects._projects.get(args.project)

                    if project is None:
                        print("Project not found.")
                        return

                    if task.assigned_to:
                        task.assigned_to.remove_task(task.task_id)

                    task.assigned_to = project
                    project.add_task(task.task_id)

                print("Task updated.")

        elif args.action == "complete":
            task = Tasks._tasks.get(args.id)

            if task:
                task.status = "complete"
                print("Task completed.")

        elif args.action == "delete":
            task = Tasks._tasks.get(args.id)

            if task:
                if task.assigned_to:
                    task.assigned_to.remove_task(task.task_id)

                del Tasks._tasks[args.id]
                print("Task deleted.")

        else:
            print("Action not available for tasks.")


    if args.action != "list" and args.action != "show":
        save_data()


if __name__ == "__main__":
    main()
