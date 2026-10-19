class Projects:
  _next_id = 1000
  _projects = {}
  def __init__(self,project_id,owner,title, description, due_date):
    self.project_id = project_id
    self.owner = owner
    self.title = title 
    self.description = description
    self.due_date = due_date
    self.tasks = []
    
  def __repr__(self):
      return f"""
    Project(
        Project Id: {self.project_id}, 
        Owner: {self.owner.user_id}, 
        Title:{self.title}, 
        Description: {self.description}, 
        Due_date: {self.due_date}
        Task: {self.tasks})"""
    
  @classmethod
  def create_project(cls,owner,title,description,due_date):
    project_id = cls._generate_id()
    project = cls(project_id,owner,title,description,due_date)
    cls._projects[project_id] = project
    return project
  
  @classmethod
  def _generate_id(cls):
    while True:
      cls._next_id += 1
      cls.project_id = f"PJT{cls._next_id}"
      if cls.project_id not in cls._projects:
        return cls.project_id
  
  @classmethod    
  def all_projects(cls):
    return print(list(cls._projects.values()))
  
  @classmethod
  def get_project(cls,project_id):
    return cls._projects[project_id]
  
  def add_task(self,task_id):
    if task_id not in self.tasks:
      self.tasks.append(task_id)

  @classmethod    
  def update(cls,project_id,value_to_update,owner=None,title=None, description=None,due_date=None):
    project = cls._projects.get(project_id)
    if project == None:
      return "No project found"
    if value_to_update == "owner":
      if owner is not None:
        project.owner = owner
    elif value_to_update == "title":
      if title is not None:
        project.title = title
    elif value_to_update == "description":
      if description is not None:
        project.description = description
    elif value_to_update == "due date":
      if due_date is not None:
        project.due_date = due_date
    elif value_to_update == "tasks":
      if previous_task is not None and updated_task is not None:
        for index,task in enumerate(user.tasks):
          if task == previous_task.title:
            user.task[index] = updated_task.title
            return f"task updated from {previous_task.title} to {updated_task.title}"
          else:
            return "No task found that matches previous task"

  def remove_task(self,task_id):
    if task_id in self.tasks:
      self.tasks.remove(task_id)

  @classmethod
  def delete_project(cls,project_id):
    project = cls._projects.get(project_id)
    if project is None:
      return "project not found"
    cls._projects.pop(project_id)

    from models.user import User

    for user in User._users.values():
      if project_id in user.projects:
        user.projects.remove(project_id)

    from models.tasks import Tasks

    for task in Tasks._tasks.values():
      if project_id == task.assigned_to.project_id:
        task.assigned_to.project_id = None
  def to_dict(self):
    return {
      "project_id":self.project_id,
      "owner":self.owner.user_id,
      "title":self.title,
      "description":self.description,
      "due_date":self.due_date
    }
  
  
  @classmethod
  def from_dict(cls, data):
      project = cls.__new__(cls)

      from models.user import User

      owner_id = data["owner"]
      project.owner = User._users.get(owner_id) if owner_id else None

      project.project_id = data["project_id"]
      project.title = data["title"]
      project.description = data["description"]
      project.due_date = data["due_date"]
      project.tasks = []

      return project
