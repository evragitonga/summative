# Project Management CLI

This is a simple Python program that helps you manage users, projects, and tasks using the terminal.

You can:

- Add, view, update, and delete users.
- Add, view, update, and delete projects.
- Add, view, update, and delete tasks.
- Mark tasks as complete or not complete.

## Installing python

Before starting, install **Python 3** on your computer.

You can download it here: https://www.python.org/downloads/

During installation on Windows, tick **Add Python to PATH**.

## Set up the project

**Step 1:** Download or copy the project folder to your computer.

**Step 2:** Open the project folder. Make sure it contains `main.py`, `models`, and `data`.

**Step 3:** Open a terminal inside the project folder.

**Step 4:** Check that Python is installed by running:

```bash
python --version
```

**Step 5:** Start the program:

```bash
python main.py --help
```

The program saves your information in `data.json`. Keep this file so you do not lose your saved data.

## How to use the program

Run each command in the terminal from the folder containing `main.py`.

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

### Update a user

```bash
python main.py user update --id USER1001 --name "Amina Wanjiku"
```

### Delete a user

```bash
python main.py user delete --id USER1001
```

### Add a project

```bash
python main.py project add --owner USER1001 --title "Library System" --description "Manage books" --due-date 2026-12-10
```

### View all projects

```bash
python main.py project list
```

### View one project

```bash
python main.py project show --id PJT1001
```

### Update a project

```bash
python main.py project update --id PJT1001 --title "New Library System"
```

### Delete a project

```bash
python main.py project delete --id PJT1001
```

### Add a task

```bash
python main.py task add --title "Design the database" --project PJT1001
```

### View all tasks

```bash
python main.py task list
```

### View one task

```bash
python main.py task show --id TSK1001
```

### Update a task

```bash
python main.py task update --id TSK1001 --title "Create the database"
```

### Mark a task as complete

```bash
python main.py task complete --id TSK1001
```

### Change a task's status

Mark it complete:

```bash
python main.py task update --id TSK1001 --status complete
```

Mark it not complete:

```bash
python main.py task update --id TSK1001 --status "not complete"
```

### Delete a task

```bash
python main.py task delete --id TSK1001
```
