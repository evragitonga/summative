from utility.generate_id import generate_id

class Tasks:
  _next_id = 1000
  _tasks = {}
  def __init__(self,task_id,title, status, assigned_to):
    self.task_id = task_id
    self.title = title
    self.status = status
    self.assigned_to = assigned_to
    
    
  def __repr__(self):
    return f"""
  Task(
    Task id: {self.task_id}, 
    Title: {self.title}, 
    Status: {self.status}, 
    Assigned to: {self.assigned_to.project_id}
    )"""
  
  @classmethod
  def create_task(cls,title,status,assigned_to):
    task_id = cls._generate_id()
    task = cls(task_id,title,status,assigned_to)
    cls._tasks[task_id] = task 
    return task
  
  @classmethod
  def _generate_id(cls):
    return generate_id(cls,"TSK",cls._tasks)
  @classmethod
  def all_tasks(cls):
    return print(list(cls._tasks.values()))
  
  def get_task(cls,task_id):
    return print(cls._tasks[task_id])

  def assign_project(self,project_id):
    from models.projects import Projects
    project = Projects.get_project(project_id)
    if self.assigned_to.project_id == None:
      self.assigned_to.project_id = project_id


  @classmethod    
  def update(cls,task_id,value_to_update,title=None,status=None,assigned_to=None):
      task = cls._tasks.get(task_id)
      if task == None:
        return "No task found"
      if value_to_update == "title":
        if title is not None:
          task.title = title
      elif value_to_update == "status":
        if status is not None:
          task.status = status
      elif value_to_update == "task":
        if assigned_to is not None:
          task.assigned_to = assigned_to

  @classmethod
  def delete_task(cls,task_id):
    task = cls._tasks.get(task_id)
    if task is None:
      return "task not found"
    cls._tasks.pop(task_id)

    from models.projects import Projects

    for project in Projects._projects.values():
      if task_id in project.tasks:
        project.tasks.remove(task_id)

  @classmethod
  def mark_task_complete(cls,task_id):
    task = cls._tasks.get(task_id)
    if task.status == "not complete":
      task.status = "complete"

  def to_dict(self):
    return {
    "task_id":self.task_id,
    "title":self.title,
    "status":self.status,
    "assigned_to":self.assigned_to.project_id
    }

  
  @classmethod
  def from_dict(cls, data):
      task = cls.__new__(cls)

      from models.projects import Projects

      project_id = data["assigned_to"]
      task.assigned_to = (
          Projects._projects.get(project_id)
          if project_id else None
      )

      task.task_id = data["task_id"]
      task.title = data["title"]
      task.status = data["status"]

      return task



