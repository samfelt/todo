import os
from ..TodoList import TodoList


def _str_to_bool(string):
    """Convert a string to a bool. Only return True is string is 'True'."""
    return string == "True"


def usage(config=None, args=None):
    """Print the usage statement"""

    print(
        """
todo - A simple todo list manager to keep a readable todo.txt file

usage: todo [action] [argument]

Actions:
a | add     <task>      Add a task to todo list
f | finish  <task ID>   Finish a task
h | help                Print help
l | list                List tasks
s | sort                Sort finished taks to bottom
  | util    <utility>   Run a TODO Utility
v | version             Print todo version

Utilities:
    test                Tesk todo config and file structure
    encrypt             Encrypt todo file
    decrypt             Decrypt todo file

"""
    )


def list_tasks(config, args=[]):
    """List all tasks in the todo list"""

    todo_file = os.path.join(
        os.path.expanduser("~/.todo"), config["Main"]["file_name"]
    )
    encrypted = _str_to_bool(config["Main"]["encryption"])
    # colorize = _str_to_bool(config["Main"]["colorize_output"])

    print("--------TODO List--------")
    file_data = TodoList(todo_file, encrypted, "")
    file_data.import_from_file()

    # Check if only one project should be printed
    if len(args) > 0 and args[0] == "--project":
        file_data.list_single_project(args[1])
    else:
        file_data.list_tasks()
