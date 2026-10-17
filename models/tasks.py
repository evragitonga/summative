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
    Assigned to: {self.assigned_to.title}
    )"""
  
  @classmethod
  def create_task(cls,title,status,assigned_to):
    task_id = cls._generate_id()
    task = cls(task_id,title,status,assigned_to)
    cls._tasks[task_id] = task 
    return task
  
  @classmethod
  def _generate_id(cls):
    while True:
      cls._next_id += 1
      cls.task_id = f"TSK{cls._next_id}"
      if cls.task_id not in cls._tasks:
        return cls.task_id
  @classmethod
  def all_tasks(cls):
    return print(list(cls._tasks.values()))
  
  def get_task(cls,task_id):
    return print(cls._tasks[task_id])
         



