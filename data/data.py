import json

from pathlib import Path
from models.user import User
from models.projects import Projects
from models.tasks import Tasks
def save_data(filename="data.json"):
  data = {
    "users":{
      user_id: user.to_dict() for user_id,user in User._users.items()
    },
    "projects":{
      project_id: project.to_dict() for project_id ,project in Projects._projects.items()
    },
    "tasks":{
      task_id: task.to_dict() for task_id,task in Tasks._tasks.items()
    }
  }
  with open(filename,"w",encoding="utf-8") as file:
    json.dump(data,file,indent=4)


def load_data(filename="data.json"):
  path = Path(filename)

  if not path.exists():
      print("No saved data found. Starting with empty collections.")
      return

  with path.open("r", encoding="utf-8") as file:
      data = json.load(file)

  User._users.clear()
  Projects._projects.clear()
  Tasks._tasks.clear()

  for user_id, user_data in data["users"].items():
      user = User.from_dict(user_data)
      User._users[user_id] = user

  for project_id, project_data in data["projects"].items():
      project = Projects.from_dict(project_data)
      Projects._projects[project_id] = project
  
  for task_id, task_data in data["tasks"].items():
      task = Tasks.from_dict(task_data)
      Tasks._tasks[task_id] = task

      if task.assigned_to is not None:
        task.assigned_to.add_task(task_id)

  User._next_id = max(
      (
          int(user_id[4:])
          for user_id in User._users
      ),
      default=1000
  )

  Projects._next_id = max(
      (
          int(project_id[3:])
          for project_id in Projects._projects
      ),
      default=1000
  )

  Tasks._next_id = max(
      (
          int(task_id[3:])
          for task_id in Tasks._tasks
      ),
      default=1000
  )

  print("Data loaded successfully.")
