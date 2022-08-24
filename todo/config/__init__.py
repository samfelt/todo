import configparser
import os
from todo.config.Colors import ColorTable


TODO_DIR = os.path.expanduser("~/.todo")
CONFIG_NAME = "config_todo.ini"
CONFIG = os.path.join(TODO_DIR, CONFIG_NAME)
COLORS = ColorTable()
todo_file = os.path.join(TODO_DIR, "todo.txt")
sample_config = """[Main]
file_name           = todo.txt
colorize_output     = True
encryption          = False
store_externally    = False

[Encryption]
store_password      = False
password            = test

[Store Externally]

[Colors]
project_complete    = Green
project_in_progress = White
project_new         = NoC

task_complete       = Cyan
task_in_progress    = NoC
task_new            = NoC
"""


def read_configuration_file():
    """Read the configuration file and set proper variables."""

    if not os.path.isdir(TODO_DIR):
        first_run()

    config = configparser.ConfigParser()
    config.read(CONFIG)

    # Main section of config
    global todo_file
    global encrypted
    todo_file = os.path.join(TODO_DIR, config["Main"]["file_name"])
    encrypted = config["Main"]["encryption"]

    if config["Main"]["colorize_output"] == "True":
        COLORS.import_config(config["Colors"])


def todo_dir_exists():
    """Check if this is the todo directory exists."""

    if os.path.isdir(TODO_DIR):
        return True
    return False


def first_run():
    """If there is no '~/.todo`, this is probably the first time this have been
    run. Offer to create the directroy and a sample configuration file.
    """

    """
    TODO
    X 1. Create ~/.todo directory
    X 2. Create config file with sample config
      3. Test config file
      4. Create todo file? Maybe a temp project with one task that says
         "Create a todo list". Or just make a blank file
    """
    if not os.path.isdir(TODO_DIR):
        print("[*] No todo directroy found")
        os.mkdir(TODO_DIR, mode=0o760)
        print(f"    Created directory: {TODO_DIR}")
    else:
        print(f"[*] Todo directroy found at {TODO_DIR}")

    if not os.path.isfile(CONFIG):
        print("[*] No config file found")
        with open(CONFIG, "w") as f:
            f.write(sample_config)
        print(f"    Sample config written to {CONFIG_NAME}")
    else:
        print(f"[*] Config file found, {CONFIG_NAME}")

    if not os.path.isfile(todo_file):
        print("[*] No todo file found")
        with open(todo_file, "w") as f:
            f.write("|Temporary Project |\n[ ] Add to your todo list\n")
        print("    Sample todo file written")
    else:
        print("[*] Todo file found")
