# Project Management CLI

This is a simple Python program that helps you manage users, projects, and tasks using the terminal.

You can:

- Add, view, update, and delete users.
- Add, view, update, and delete projects.
- Add, view, update, and delete tasks.
- Assign projects to users and tasks to projects.
- Mark tasks as complete

## Installing Python

Before starting, install **Python 3** on your computer.

Download it here: https://www.python.org/downloads/

During installation on Windows, tick **Add Python to PATH**.

## Set Up the Project

### Step 1: Install Git

If Git is not installed on your computer, download it here:

https://git-scm.com/downloads

### Step 2: Clone the repository

Open your terminal and run:

```bash
git clone https://github.com/evragitonga/summative.git
```

### Step 3: Open the project folder

Navigate into the cloned repository:

```bash
cd summative
```

Make sure the project contains `main.py`, the `models` folder, and the `data` folder.

### Step 4: Check that Python is installed

Run:

```bash
python --version
```

## External Dependencies

This project uses **Colorama** to display colored messages in the terminal, making success messages and errors easier to distinguish.

### Installation

Alternatively, install all project dependencies using:

```bash
pip install -r requirements.txt
```

### Color Usage

- Green: Successful operations, such as creating users, projects, and tasks.
- Red: Errors, such as missing users, projects, or tasks.
- Yellow: Displaying lists and individual records.

## Requirements

- Python 3
- Colorama

## Starting the Program

To view the available commands, run:

```bash
python main.py --help
```

## How to Use the Program

Run each command in the terminal from the folder containing `main.py`.

### Users

### Add a user

```bash
python main.py user add --name "Amina" --email "amina@gmail.com"
```

### View all users

```bash
python main.py user list
```

### View one user

```bash
python main.py user show --id USER1001
```

### Update a user's name

```bash
python main.py user update --id USER1001 --name "Amina Wanjiku"
```

### Update a user's email

```bash
python main.py user update --id USER1001 --email "amina.new@gmail.com"
```

### Replace a user's project reference

```bash
python main.py user update --id USER1001 --previous-project PJT1001 --project PJT1002
```

### Remove a project from a user

```bash
python main.py user remove-project --id USER1001 --project PJT1003
```

### Delete a user

```bash
python main.py user delete --id USER1004
```

### Projects

### Add a project

```bash
python main.py project add --id USER1001 --title "Library System" --description "Manage books" --due-date 2026-12-10
```

### View all projects

```bash
python main.py project list
```

### View one project

```bash
python main.py project show --id PJT1001
```

### Update a project's title

```bash
python main.py project update --id PJT1001 --title "New Library System"
```

### Change a project's owner

```bash
python main.py project update --id PJT1001 --owner USER1002
```

### Update a project's description

```bash
python main.py project update --id PJT1001 --description "Manage library books and records"
```

### Update a project's due date

```bash
python main.py project update --id PJT1001 --due-date 2026-12-20
```

### Replace a task ID in a project

```bash
python main.py project update --id PJT1001 --previous-task TSK1001 --task TSK1002
```

### Delete a project

```bash
python main.py project delete --id PJT1001
```

### Tasks

### Add a task to a project

The `--id` value is the ID of the project receiving the task.

```bash
python main.py task add --title "Design the database" --status complete --id PJT1003
```

### View all tasks

```bash
python main.py task list
```

### View one task

```bash
python main.py task show --id TSK1001
```

### Update a task's title

```bash
python main.py task update --id TSK1001 --title "Create the database"
```

### Change a task's status

```bash
python main.py task update --id TSK1001 --status complete
```

### Mark it not complete

```bash
python main.py task update --id TSK1001 --status "not complete"
```

### Assign a task to another project

```bash
python main.py task update --id TSK1001 --project PJT1002
```

### Mark a task as complete

```bash
python main.py task complete --id TSK1001
```

### Delete a task

```bash
python main.py task delete --id TSK1001
```
