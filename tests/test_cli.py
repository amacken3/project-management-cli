from argparse import Namespace

import main
from models.user import User
from utils.storage import load_users as storage_load_users
from utils.storage import save_users as storage_save_users


def setup_test_storage(monkeypatch, tmp_path, users=None):
    test_file = tmp_path / "test_data.json"

    if users is None:
        users = []

    storage_save_users(users, test_file)

    monkeypatch.setattr(main, "load_users", lambda: storage_load_users(test_file))
    monkeypatch.setattr(main, "save_users", lambda users: storage_save_users(users, test_file))

    return test_file


def test_add_user_command_saves_user(monkeypatch, tmp_path, capsys):
    test_file = setup_test_storage(monkeypatch, tmp_path)

    args = Namespace(name="Aengus", email="aengus@example.com")

    main.add_user(args)

    captured = capsys.readouterr()
    users = storage_load_users(test_file)

    assert "User added: Aengus" in captured.out
    assert len(users) == 1
    assert users[0].name == "Aengus"
    assert users[0].email == "aengus@example.com"


def test_add_project_command_adds_project_to_user(monkeypatch, tmp_path, capsys):
    user = User("Aengus", "aengus@example.com")
    test_file = setup_test_storage(monkeypatch, tmp_path, [user])

    args = Namespace(
        user="Aengus",
        title="Portfolio CLI",
        description="Build a project management tool"
    )

    main.add_project(args)

    captured = capsys.readouterr()
    users = storage_load_users(test_file)

    assert "Project added to Aengus: Portfolio CLI" in captured.out
    assert len(users[0].projects) == 1
    assert users[0].projects[0].title == "Portfolio CLI"


def test_add_task_command_adds_task_to_project(monkeypatch, tmp_path, capsys):
    user = User("Aengus", "aengus@example.com")
    test_file = setup_test_storage(monkeypatch, tmp_path, [user])

    main.add_project(
        Namespace(
            user="Aengus",
            title="Portfolio CLI",
            description="Build a project management tool"
        )
    )

    args = Namespace(
        project="Portfolio CLI",
        title="Finish README",
        description="Write setup instructions",
        due_date="2026-05-08"
    )

    main.add_task(args)

    captured = capsys.readouterr()
    users = storage_load_users(test_file)
    project = users[0].projects[0]

    assert "Task added to Portfolio CLI: Finish README" in captured.out
    assert len(project.tasks) == 1
    assert project.tasks[0].title == "Finish README"
    assert project.tasks[0].completed == False


def test_complete_task_command_marks_task_complete(monkeypatch, tmp_path, capsys):
    user = User("Aengus", "aengus@example.com")
    test_file = setup_test_storage(monkeypatch, tmp_path, [user])

    main.add_project(
        Namespace(
            user="Aengus",
            title="Portfolio CLI",
            description="Build a project management tool"
        )
    )

    main.add_task(
        Namespace(
            project="Portfolio CLI",
            title="Finish README",
            description="Write setup instructions",
            due_date="2026-05-08"
        )
    )

    main.complete_task(
        Namespace(
            project="Portfolio CLI",
            task="Finish README"
        )
    )

    captured = capsys.readouterr()
    users = storage_load_users(test_file)
    task = users[0].projects[0].tasks[0]

    assert "Task completed: Finish README" in captured.out
    assert task.completed == True