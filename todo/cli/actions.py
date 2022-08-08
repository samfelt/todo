from ..Project import Project
from ..TodoList import TodoList
from ..Task import Task
import todo.config as config


def _str_to_bool(string):
    """Convert a string to a bool. Only return True is string is 'True'."""
    return string == "True"


def _import_todo_file():
    """Import the todo file based on the config. This is done by most (but not
    all) functions available on the command line."""

    file_data = TodoList(config.todo_file, config.encrypted, "")
    file_data.import_from_file()
    return file_data


def usage(args=None):
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


def list_tasks(args=[]):
    """List all tasks in the todo list"""

    todo_list = _import_todo_file()
    print("--------TODO List--------")

    # Check if only one project should be printed
    if len(args) > 0 and args[0] == "--project":
        todo_list.list_single_project(args[1])
    else:
        todo_list.list_tasks()


def add_task(args=[]):
    """Add a new task to a project. Prompt the user which project to add it too
    and create a new one if rquested."""

    todo_list = _import_todo_file()
    if args:
        desc = args[0]
    else:
        desc = input("Task description: ")
    temp_task = Task(desc)
    print("--------Projects--------")
    starting_number = 1
    todo_list.list_projects(starting_number)
    print("\n(N ) New Project")
    num = input("\nWhich project would you like to add this to? ")
    if num == "N":
        name = input("\nName of the new project? ")
        temp_proj = Project(name)
        temp_proj.add_task(temp_task)
        todo_list.add_project(temp_proj)
    else:
        selected_project = todo_list.projects[int(num) - starting_number]
        selected_project.add_task(temp_task)

    todo_list.export_file()


def finish_task(args=[]):
    """If not defined in the arguments, let the user choose which task they
    would like to mark as finished."""

    todo_list = _import_todo_file()
    if args and (args[0] == "--project" or args[0] == "-p"):
        print("--------Projects--------")
        starting_number = 1
        todo_list.list_projects(starting_number)
        index = int(input("Which project did you complete? "))
        if (index < 1) or (index > len(todo_list.projects)):
            print("Project number doesn't exist")
            exit()
        todo_list.projects[index - starting_number].finish()
    else:
        starting_number = 1
        todo_list.list_tasks(starting_number)
        index = int(input("Which task did you complete? "))
        if (index < 1) or (index > todo_list.get_number_of_tasks()):
            print("Task number doesn't exist")
            exit()
        todo_list.get_task_by_index(index - starting_number).finish()

    todo_list.export_file()


def unfinish_task(args=[]):
    """If not defined in the arguments, let the user choose which task they
    would like to mark as not finished."""

    todo_list = _import_todo_file()
    if args and (args[0] == "--project" or args[0] == "-p"):
        print("--------Projects--------")
        starting_number = 1
        todo_list.list_projects(starting_number)
        index = int(input("Which project did you un-finish? "))
        if (index < 1) or (index > len(todo_list.projects)):
            print("Project number doesn't exist")
            exit()
        todo_list.projects[index - starting_number].unfinish()
    else:
        starting_number = 1
        todo_list.list_tasks(starting_number)
        index = int(input("Which task did you un-finish? "))
        if (index < 1) or (index > todo_list.get_number_of_tasks()):
            print("Task number doesn't exist")
            exit()
        todo_list.get_task_by_index(index - starting_number).unfinish()

    todo_list.export_file()
