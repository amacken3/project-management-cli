from models.task import Task
from models.project import Project
    
# Task Tests
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