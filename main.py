from models.user import User
from models.projects import Projects 
from models.tasks import Tasks

#users
amina = User.create_user("Amina", "amina@gmail.com")
brian = User.create_user("Brian", "brian@gmail.com")
charles = User.create_user("Charles", "charles@gmail.com")
diana = User.create_user("Diana", "diana@gmail.com")
evra = User.create_user("Evra", "evra@gmail.com")



#projects
project1 = Projects.create_project(amina,"Inventory Management System","Build a CLI application to add, view, search, update, and delete products while tracking stock levels.","2026-11-15"
)

project2 = Projects.create_project(brian,"Online Store","Develop an e-commerce website where users can browse products, add items to a cart, and place orders.","2026-12-01"
)

project3 = Projects.create_project(charles,"Student Management System",
"Create an application to register students, record grades, and manage student information.","2026-11-20"
)

project4 = Projects.create_project(diana,"Hospital Management System",
"Build a system to manage patient records, doctor appointments, and hospital services.","2026-12-10"
)

project5 = Projects.create_project(evra,"Portfolio Website","Develop a responsive portfolio website to showcase projects, skills, and contact information.","2026-11-30"
)


#tasks
task1 = Tasks.create_task("Design the database","not complete",project1
)

task2 = Tasks.create_task("Build the user interface","in progress",project2
)

task3 = Tasks.create_task(
    "Implement student registration",
    "complete",
    project3
)

task4 = Tasks.create_task(
    "Create appointment booking",
    "not complete",
    project4
)

task5 = Tasks.create_task(
    "Deploy the portfolio website",
    "in progress",
    project5
)


# =========================
# 4. CONNECT USERS TO PROJECTS
# =========================

amina.add_projects(project1)
brian.add_projects(project2)
charles.add_projects(project3)
diana.add_projects(project4)
evra.add_projects(project5)


# =========================
# 5. CONNECT PROJECTS TO TASKS
# =========================

project1.add_task(task1)
project2.add_task(task2)
project3.add_task(task3)
project4.add_task(task4)
project5.add_task(task5)



# User.view_users()
# Projects.all_projects()
# Tasks.all_tasks()
# User.update("USER1001","name","Alex")
# User.get_user("USER1001")
# User.update("USER1001","email",email="alex@gmail.com")
# User.get_user("USER1001")
