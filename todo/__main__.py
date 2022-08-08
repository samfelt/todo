import configparser
import os
import sys
import todo.cli as cli


def main():
    """Main entry point for todo.
    Read in the config file and parse the command line arguments."""

    TODO_DIR = os.path.expanduser("~/.todo")
    CONFIG_NAME = "config_todo.ini"
    CONFIG = os.path.join(TODO_DIR, CONFIG_NAME)

    # Check that dir and config exist
    if not os.path.isdir(TODO_DIR):
        print("[*] No todo directroy found")
        os.mkdir(TODO_DIR, mode=0o760)
        print(f"    Created directory: {TODO_DIR}")

    if not os.path.isfile(CONFIG):
        print(f"[ERROR] Config file, {CONFIG}, does not exist")
        return 1

    # Read config
    config = configparser.ConfigParser()
    config.read(CONFIG)

    # Main section of config
    # TODO_FILE = os.path.join(TODO_DIR, config["Main"]["file_name"])
    # ENCRYPTED = str_to_bool(config["Main"]["encryption"])
    # COLORIZE = str_to_bool(config["Main"]["colorize_output"])

    # Encryption
    """
    aes_passphrase = ""
    if ENCRYPTED:
        if str_to_bool(config["Encryption"]["store_password"]):
            aes_passphrase = config["Encryption"]["password"]
        else:
            aes_passphrase = getpass.getpass("Encryption Password: ")
    """

    # Colorize
    """
    color_table = ColorTable()
    if COLORED:
        color_table.import_config(config['Colors'])
    """

    # Check simple case
    if len(sys.argv) == 1:
        cli.actions.list_tasks(config)
        return 0

    # Parse arguments
    argument_parser = {
        # "a" : add_task,
        # "e" : edit_task,
        # "d" : delete_task,
        # "f" : finish_task,
        "h": cli.actions.usage,
        "l": cli.actions.list_tasks,
        # "s" : sort_tasks,
        # "u" : unfinish_task,
        # "v" : Version,
        # "t" : testtesttest,
        # Long actions
        # "add"   : add_task,
        # "edit"  : edit_task,
        # "delete": delete_task,
        # "finish": finish_task,
        "help": cli.actions.usage,
        "list": cli.actions.list_tasks,
        # "sort"  : sort_tasks,
        # "test"  : testtesttest,
        # "util"  : utilities,
        # "version": version,
    }

    # Check the first argument and default to Usage()
    argument_parser.get(sys.argv[1], cli.actions.usage)(config, sys.argv[2:])


if __name__ == "__main__":
    exit(main())
