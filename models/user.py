class User():
  _users = {}
  _next_id = 1000
  def __init__(self,user_id,name,email):
    self.user_id = user_id
    self.name = name
    self.email = email
    self.projects = []
    
  def __repr__(self):
        return f"""
      User(
        User Id: {self.user_id}, 
        Name: {self.name}, 
        Email: {self.email}, 
        Projects Assigned to: {self.projects})"""
    
  @classmethod
  def create_user(cls,name,email):
    user_id = cls._generate_id()
    user = cls(user_id,name,email)
    cls._users[user_id] = user
    return user
  
  @classmethod
  def _generate_id(cls):
    while True:
      cls._next_id += 1
      cls.user_id = f"USER{cls._next_id}"
      
      if cls.user_id not in cls._users:
        return cls.user_id
      
  @classmethod
  def view_users(cls):
    return print(list(cls._users.values()))
  
  @classmethod
  def get_user(cls,user_id):
    return print(cls._users[user_id])


  
  def add_projects(self,project_id):
    if project_id not in self.projects:
      self.projects.append(project_id)
      
  
  @classmethod    
  def update(cls,user_id,value_to_update,name=None,email=None,previous_project=None,updated_project=None):
    user = cls._users.get(user_id)
    if user == None:
      return "No user found"
    if value_to_update == "name":
      if name is not None:
        user.name = name
    elif value_to_update == "email":
        if email is not None:
          user.email = email
    elif value_to_update == "project":
      if previous_project is not None and updated_project is not None:
        for index,project in enumerate(user.projects):
          if project == previous_project.title:
            user.projects[index] = updated_project.title
            return f"project updated from {previous_project.title} to {updated_project.title}"
          else:
            return "No project found that matches previous project"

  def remove_project(self,project_id):
    if project_id in self.projects:
      self.projects.remove(project_id)
  
  @classmethod
  def delete_user(cls,user_id):
    user = cls._users.get(user_id)
    if user is None:
      return "User not found"
    cls._users.pop(user_id)

    from models.projects import Projects

    for project in Projects._projects.values():
      if user_id == project.owner.user_id:
        project.owner.user_id = None

  def to_dict(self):
    return {
    "user_id":self.user_id,
    "name":self.name,
    "email":self.email,
    "projects":self.projects
    }
  
  @classmethod
  def from_dict(cls, data):
    user = cls.__new__(cls)
    user.user_id = data["user_id"]
    user.name= data["name"]
    user.email = data["email"]
    user.projects = data["projects"]
    return user