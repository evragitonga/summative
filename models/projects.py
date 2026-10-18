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
        Owner: {self.owner.name}, 
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
    return print(cls._projects[project_id])
  
  def add_task(self,task):
    if task.title not in self.tasks:
      self.tasks.append(task.title)

  @classmethod    
  def update(cls,product_id,value_to_update,owner=None,title=None, description=None,due_date=None):
    project = cls._projects.get(product_id)
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

