import configparser
import os


TODO_DIR = os.path.expanduser("~/.todo")
CONFIG_NAME = "config_todo.ini"
CONFIG = os.path.join(TODO_DIR, CONFIG_NAME)
todo_file = os.path.join(TODO_DIR, "todo.txt")


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
    # COLORIZE = str_to_bool(config["Main"]["colorize_output"])


def first_run():
    """If there is no '~/.todo`, this is probably the first time this have been
    run. Offer to create the directroy and a sample configuration file."""

    print("[*] No todo directroy found")
    os.mkdir(TODO_DIR, mode=0o760)
    print(f"    Created directory: {TODO_DIR}")
