from models.task import Task
from models.project import Project
from models.user import User
    
# Task Tests
# These confirm that a Task stores its own data
# and can update its completed status

def test_task_stores_attributes():
    task = Task("Finish README", "Write setup instructions", "2026-05-08")
    
    assert task.title == "Finish README"
    assert task.description == "Write setup instructions"
    assert task.due_date == "2026-05-08"

def test_task_starts_incomplete():
    task = Task("Finish README", "Write setup instructions", "2026-05-08")

    assert task.completed == False

def test_task_can_be_marked_complete():
    task = Task("Finish README", "Write setup instructions", "2026-05-08")

    task.mark_complete()

    assert task.completed == True

# Project Tests
# These confirm that a Project stores project data
# and can manage a list of Task objects

def test_project_stores_attributes():
    project = Project("Portfolio CLI", "Build a project management tool")

    assert project.title == "Portfolio CLI"
    assert project.description == "Build a project management tool"

def test_project_starts_with_empty_tasks():
    project = Project("Portfolio CLI", "Build a project management tool")

    assert project.tasks == []

def test_project_can_add_task():
    project = Project("Portfolio CLI", "Build a project management tool")
    task = Task("Finish README", "Write setup instructions", "2026-05-08")

    project.add_task(task)

    assert task in project.tasks

# User Tests
# These confirm that a User stores user data
# and can manage a list of Project objects

def test_user_stores_attributes():
    user = User("Aengus", "aengus@example.com")

    assert user.name == "Aengus"
    assert user.email == "aengus@example.com"

def test_user_starts_with_empty_projects():
    user = User("Aengus", "aengus@example.com")

    assert user.projects == []

def test_user_can_add_project():
    user = User("Aengus", "aengus@example.com")
    project = Project("Portfolio CLI", "Build a project management tool")

    user.add_project(project)

    assert project in user.projects

# JSON persistence tests
# These confirm that model objects can convert to dictionaries
# and rebuild from dictionaries for JSON save/load

def test_task_can_convert_to_dict():
    task = Task("Finish README", "Write setup instructions", "2026-05-08")

    task_dict = task.to_dict()

    assert task_dict == {
        "title": "Finish README",
        "description": "Write setup instructions",
        "due_date": "2026-05-08",
        "completed": False
    }

def test_task_can_be_created_from_dict():
    task_data = {
        "title": "Finish README",
        "description": "Write setup instructions",
        "due_date": "2026-05-08",
        "completed": True
    }

    task = Task.from_dict(task_data)

    assert task.title == "Finish README"
    assert task.description == "Write setup instructions"
    assert task.due_date == "2026-05-08"
    assert task.completed == True

def test_project_can_convert_to_dict():
    project = Project("Portfolio CLI", "Build a project management tool")
    task = Task("Finish README", "Write setup instructions", "2026-05-08")

    project.add_task(task)

    project_dict = project.to_dict()

    assert project_dict == {
        "title": "Portfolio CLI",
        "description": "Build a project management tool",
        "tasks": [
            {
                "title": "Finish README",
                "description": "Write setup instructions",
                "due_date": "2026-05-08",
                "completed": False
            }
        ]
    }

def test_project_can_be_created_from_dict():
    project_data = {
        "title": "Portfolio CLI",
        "description": "Build a project management tool",
        "tasks": [
            {
                "title": "Finish README",
                "description": "Write setup instructions",
                "due_date": "2026-05-08",
                "completed": True
            }
        ]
    }

    project = Project.from_dict(project_data)

    assert project.title == "Portfolio CLI"
    assert project.description == "Build a project management tool"
    assert len(project.tasks) == 1
    assert project.tasks[0].title == "Finish README"
    assert project.tasks[0].completed == True

def test_user_can_convert_to_dict():
    user = User("Aengus", "aengus@example.com")
    project = Project("Portfolio CLI", "Build a project management tool")
    task = Task("Finish README", "Write setup instructions", "2026-05-08")

    project.add_task(task)
    user.add_project(project)

    user_dict = user.to_dict()

    assert user_dict == {
        "name": "Aengus",
        "email": "aengus@example.com",
        "projects": [
            {
                "title": "Portfolio CLI",
                "description": "Build a project management tool",
                "tasks": [
                    {
                        "title": "Finish README",
                        "description": "Write setup instructions",
                        "due_date": "2026-05-08",
                        "completed": False
                    }
                ]
            }
        ]
    }

def test_user_can_be_created_from_dict():
    user_data = {
        "name": "Aengus",
        "email": "aengus@example.com",
        "projects": [
            {
                "title": "Portfolio CLI",
                "description": "Build a project management tool",
                "tasks": [
                    {
                        "title": "Finish README",
                        "description": "Write setup instructions",
                        "due_date": "2026-05-08",
                        "completed": True
                    }
                ]
            }
        ]
    }

    user = User.from_dict(user_data)

    assert user.name == "Aengus"
    assert user.email == "aengus@example.com"
    assert len(user.projects) == 1
    assert user.projects[0].title == "Portfolio CLI"
    assert len(user.projects[0].tasks) == 1
    assert user.projects[0].tasks[0].title == "Finish README"
    assert user.projects[0].tasks[0].completed == True
