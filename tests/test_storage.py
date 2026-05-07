from models.user import User
from models.project import Project
from models.task import Task
from utils.storage import load_data, save_data, save_users, load_users


def test_load_data_returns_dictionary():
    data = load_data()

    assert type(data) == dict


def test_load_data_has_required_keys():
    data = load_data()

    assert "users" in data
    assert "projects" in data
    assert "tasks" in data


def test_save_data_writes_to_json_file(tmp_path):
    test_file = tmp_path / "test_data.json"

    test_data = {
        "users": [],
        "projects": [],
        "tasks": []
    }

    save_data(test_data, test_file)
    loaded_data = load_data(test_file)

    assert loaded_data == test_data

def test_save_and_load_users_with_projects_and_tasks(tmp_path):
    test_file = tmp_path / "test_data.json"

    user = User("Aengus", "aengus@example.com")
    project = Project("Portfolio CLI", "Build a project management tool")
    task = Task("Finish README", "Write setup instructions", "2026-05-08")

    project.add_task(task)
    user.add_project(project)

    save_users([user], test_file)
    loaded_users = load_users(test_file)

    assert len(loaded_users) == 1
    assert loaded_users[0].name == "Aengus"
    assert loaded_users[0].email == "aengus@example.com"
    assert len(loaded_users[0].projects) == 1
    assert loaded_users[0].projects[0].title == "Portfolio CLI"
    assert len(loaded_users[0].projects[0].tasks) == 1
    assert loaded_users[0].projects[0].tasks[0].title == "Finish README"