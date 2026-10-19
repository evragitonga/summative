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
    parser.add_argument("--previous-project")
    parser.add_argument("--previous-task")
    parser.add_argument("--task")
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
            print(User.view_users())
        elif args.action == "show":
            print(User.get_user(args.id))

        elif args.action == "update":
            if args.name is not None:
                User.update(args.id,"name",name=args.name)
                print("User updated.")
            if args.email is not None:
                User.update(args.id,"email",email=args.email)
                print("User updated.")
            
            if args.previous_project is not None and args.project is not None:
                previous_project = Projects.get_project(args.previous_project)
                updated_project = Projects.get_project(args.project)

                if previous_project and updated_project:
                    print(
                        User.update(args.id,"project",previous_project=previous_project,updated_project=updated_project))
                else:
                    print("Previous project or new project not found.")

        elif args.action == "delete":
            User.delete_user(args.id)
            print(f"User {args.id} deleted succesfully")

        elif args.action == "remove-project":
            user = User.get_user(args.id)

            if user and args.project:
                removed = user.remove_project(args.project)
                print("Project removed from user.")
            else:
                print("user or project id not provided.")

    elif args.entity == "project":

        if args.action == "add":
            owner = User.get_user(args.id)
            if owner:
                project = Projects.create_project(owner,args.title,args.description,args.due_date)
                print("Project created:", project.project_id)
            else:
                print("No owner found")

        elif args.action == "list":
            print(Projects.view_projects())
        elif args.action == "show":
            print(Projects.get_project(args.id))
        elif args.action == "update":
            if args.owner is not None:
                owner = User.get_user(args.id)
                Projects.update(args.id,"owner",owner=owner)
                print("project owner updated.")
            if args.title is not None:
                Projects.update(args.id,"title",title=args.title)
                print("Project title updated.")
            if args.description is not None:
                Projects.update(args.id,"description",description=args.description)
                print("Project description updated.")
            if args.due_date is not None:
                Projects.update(args.id,"due date",due_date=args.due-date)
                print("Project due date updated.")
            if args.previous_task is not None and args.task is not None:
                previous_task = Tasks.get_task(args.previous_task)
                updated_task = Tasks.get_task(args.task)

                if previous_task and updated_task:
                    print(
                        Projects.update(args.id,"tasks",previous_task=previous_task,updated_task=updated_task))
                else:
                    print("Previous task or new task not found.")

            
        elif args.action == "delete":
            Projects.delete_project(args.id)
            print(f"Project {args.id} deleted succesfully")

    elif args.entity == "task":

        if args.action == "add":
            project = Projects.get_project(args.id)

            if project:
                task = Tasks.create_task(args.title,args.status or "not complete",project
                )

                project.add_task(task.task_id)
                print("Task created:", task.task_id)

            else:
                print("Project not found.")

        elif args.action == "list":
            print(Tasks.all_tasks())
        elif args.action == "show":
            print(Tasks.get_task(args.id))
        elif args.action == "update":
            if args.title is not None:
                Tasks.update(args.id,"title",title=args.title)
                print("task title updated.")
            if args.status is not None:
                Tasks.update(args.id,"status",status=args.status)
                print("Task status updated.")
            if args.project is not None:
                project = Projects.get_project(args.project)

                if project:
                    Tasks.update(args.id,"assigned to",assigned_to=project)
                    print("project assigned to updated")
                else:
                    print("Project not found.")
        elif args.action == "complete":
            Tasks.mark_task_complete(args.id)
            print("task completed")
        elif args.action == "delete":
            Tasks.delete_task(args.id)
            print(f"Task {args.id} deleted succesfully.")

        else:
            print("Action not available for tasks.")


    if args.action != "list" and args.action != "show":
        save_data()


if __name__ == "__main__":
    main()
