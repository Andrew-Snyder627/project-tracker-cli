import argparse
from models.user import User
from models.project import Project
from models.task import Task
from utils.file_io import load_data, save_data
from rich import print

users = []
projects = []
tasks = []

def add_user(args):
  user = User(args.name, args.email)
  users.append(user)
  print(f"[green]User added: [/green] {user}")

def list_users(args):
  for u in users:
    print(u)

def setup_parser():
  parser = argparse.ArgumentParser(description="Project Management CLI")
  subparsers = parser.add_subparsers()

  # add-user
  user_parser = subparsers.add_parser("add-user")
  user_parser.add_argument("--name", required=True)
  user_parser.add_argument("--email", required=True)
  user_parser.set_defaults(func=add_user)

  # list-users
  list_parser = subparsers.add_parser("list-users")
  list_parser.set_defaults(func=list_users)

  return parser

if __name__ == "__main__":
  parser = setup_parser()
  args = parser.parse_args()
  if hasattr(args, "func"):
    args.func(args)
  else:
    parser.print_help()