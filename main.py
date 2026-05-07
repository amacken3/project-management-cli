import argparse

from models.user import User
from models.project import Project
from utils.storage import load_users, save_users


def add_user(args):
    users = load_users()
    user = User(args.name, args.email)
    users.append(user)
    save_users(users)

    print(f"User added: {args.name}")

def list_users(args):
    users = load_users()

    if len(users) == 0:
        print("No users found.")
        return

    for user in users:
        print(f"{user.name} - {user.email}")

def add_project(args):
    users = load_users()

    for user in users:
        if user.name == args.user:
            project = Project(args.title, args.description)
            user.add_project(project)
            save_users(users)
            print(f"Project added to {user.name}: {args.title}")
            return

    print(f"User not found: {args.user}")

def list_projects(args):
    users = load_users()

    for user in users:
        if user.name == args.user:
            if len(user.projects) == 0:
                print(f"No projects found for {user.name}.")
                return

            for project in user.projects:
                print(f"{project.title} - {project.description}")
            return

    print(f"User not found: {args.user}")

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

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()