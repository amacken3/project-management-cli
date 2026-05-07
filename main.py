import argparse

from rich.console import Console
from rich.table import Table

from models.task import Task
from models.user import User
from models.project import Project
from utils.storage import load_users, save_users


console = Console()


def add_user(args):
    users = load_users()
    user = User(args.name, args.email)
    users.append(user)
    save_users(users)

    console.print(f"[green]User added:[/green] {args.name}")


def list_users(args):
    users = load_users()

    if len(users) == 0:
        console.print("[yellow]No users found.[/yellow]")
        return

    table = Table(title="Users")
    table.add_column("Name")
    table.add_column("Email")

    for user in users:
        table.add_row(user.name, user.email)

    console.print(table)


def add_project(args):
    users = load_users()

    for user in users:
        if user.name == args.user:
            project = Project(args.title, args.description)
            user.add_project(project)
            save_users(users)
            console.print(f"[green]Project added to {user.name}:[/green] {args.title}")
            return

    console.print(f"[red]User not found:[/red] {args.user}")


def list_projects(args):
    users = load_users()

    for user in users:
        if user.name == args.user:
            if len(user.projects) == 0:
                console.print(f"[yellow]No projects found for {user.name}.[/yellow]")
                return

            table = Table(title=f"Projects for {user.name}")
            table.add_column("Title")
            table.add_column("Description")

            for project in user.projects:
                table.add_row(project.title, project.description)

            console.print(table)
            return

    console.print(f"[red]User not found:[/red] {args.user}")


def add_task(args):
    users = load_users()

    for user in users:
        for project in user.projects:
            if project.title == args.project:
                task = Task(args.title, args.description, args.due_date)
                project.add_task(task)
                save_users(users)
                console.print(f"[green]Task added to {project.title}:[/green] {args.title}")
                return

    console.print(f"[red]Project not found:[/red] {args.project}")


def list_tasks(args):
    users = load_users()

    for user in users:
        for project in user.projects:
            if project.title == args.project:
                if len(project.tasks) == 0:
                    console.print(f"[yellow]No tasks found for {project.title}.[/yellow]")
                    return

                table = Table(title=f"Tasks for {project.title}")
                table.add_column("Title")
                table.add_column("Due Date")
                table.add_column("Status")

                for task in project.tasks:
                    status = "Complete" if task.completed else "Incomplete"
                    table.add_row(task.title, task.due_date, status)

                console.print(table)
                return

    console.print(f"[red]Project not found:[/red] {args.project}")


def complete_task(args):
    users = load_users()

    for user in users:
        for project in user.projects:
            if project.title == args.project:
                for task in project.tasks:
                    if task.title == args.task:
                        task.mark_complete()
                        save_users(users)
                        console.print(f"[green]Task completed:[/green] {task.title}")
                        return

                console.print(f"[red]Task not found:[/red] {args.task}")
                return

    console.print(f"[red]Project not found:[/red] {args.project}")


def main():
    parser = argparse.ArgumentParser(description="Project Management CLI")
    subparsers = parser.add_subparsers(dest="command")

    add_user_parser = subparsers.add_parser("add-user")
    add_user_parser.add_argument("--name", required=True)
    add_user_parser.add_argument("--email", required=True)
    add_user_parser.set_defaults(func=add_user)

    list_users_parser = subparsers.add_parser("list-users")
    list_users_parser.set_defaults(func=list_users)

    add_project_parser = subparsers.add_parser("add-project")
    add_project_parser.add_argument("--user", required=True)
    add_project_parser.add_argument("--title", required=True)
    add_project_parser.add_argument("--description", required=True)
    add_project_parser.set_defaults(func=add_project)

    list_projects_parser = subparsers.add_parser("list-projects")
    list_projects_parser.add_argument("--user", required=True)
    list_projects_parser.set_defaults(func=list_projects)

    add_task_parser = subparsers.add_parser("add-task")
    add_task_parser.add_argument("--project", required=True)
    add_task_parser.add_argument("--title", required=True)
    add_task_parser.add_argument("--description", required=True)
    add_task_parser.add_argument("--due-date", required=True)
    add_task_parser.set_defaults(func=add_task)

    list_tasks_parser = subparsers.add_parser("list-tasks")
    list_tasks_parser.add_argument("--project", required=True)
    list_tasks_parser.set_defaults(func=list_tasks)

    complete_task_parser = subparsers.add_parser("complete-task")
    complete_task_parser.add_argument("--project", required=True)
    complete_task_parser.add_argument("--task", required=True)
    complete_task_parser.set_defaults(func=complete_task)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()