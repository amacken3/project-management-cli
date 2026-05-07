# Project Management CLI Tool

A Python-based command-line project management tool for managing users, projects, and tasks. This app was built as a summative lab to practice object-oriented programming, command-line interfaces, file I/O, testing, package management, and clean project structure.

The tool lets an admin create users, assign projects to users, add tasks to projects, list saved data, and mark tasks as complete. Data is saved locally in a JSON file so it persists between CLI commands.

---

## Features

- Create and list users
- Add projects to specific users
- List projects assigned to a user
- Add tasks to projects
- List tasks for a project
- Mark tasks as complete
- Save and load data using local JSON file storage
- Handle missing or invalid JSON data with a safe default state
- Validate task due dates with `python-dateutil`
- Display cleaner CLI output with `rich`
- Includes automated tests for models, storage, and CLI behavior

---

## Tech Used

- Python 3.14
- argparse — command-line argument parsing
- JSON — local file persistence
- Pipenv — dependency management
- rich — styled CLI messages and table output
- python-dateutil — due date parsing and validation
- pytest — automated testing

---

## Project Structure

```text
project-management-cli/
│
├── data/
│   └── tracker_data.json
│
├── models/
│   ├── __init__.py
│   ├── project.py
│   ├── task.py
│   └── user.py
│
├── tests/
│   ├── __init__.py
│   ├── test_cli.py
│   ├── test_models.py
│   └── test_storage.py
│
├── utils/
│   ├── __init__.py
│   └── storage.py
│
├── .gitignore
├── main.py
├── Pipfile
├── Pipfile.lock
├── README.md
└── requirements.txt
```

## Setup Instructions

These steps assume you have Python 3.10+ installed. This project was built with Python 3.14.4.

### 1. Clone the repository

```bash
git clone https://github.com/amacken3/project-management-cli.git
cd project-management-cli
```

### 2. Check if Pipenv is installed

```bash
pipenv --version
```

If that command does not work, install Pipenv:

```bash
pip install pipenv
```

### 3. Install dependencies

```bash
pipenv install --dev
```

### 4. Activate the virtual environment

```bash
pipenv shell
```

### 5. Confirm the CLI works

```bash
python main.py --help
```

You should see the available commands:

```text
add-user
list-users
add-project
list-projects
add-task
list-tasks
complete-task
```