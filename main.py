import argparse

from models.user import User
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

def main():
    parser = argparse.ArgumentParser(description="Project Management CLI")
    subparsers = parser.add_subparsers(dest="command")

    add_user_parser = subparsers.add_parser("add-user")
    add_user_parser.add_argument("--name", required=True)
    add_user_parser.add_argument("--email", required=True)
    add_user_parser.set_defaults(func=add_user)

    list_users_parser = subparsers.add_parser("list-users")
    list_users_parser.set_defaults(func=list_users)
    
    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()