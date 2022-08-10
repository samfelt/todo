import sys
import todo.cli as cli
import todo.config as config


def main():
    """Main entry point for todo.
    Read in the config file and parse the command line arguments."""

    # Check that dir and config exist
    # if not os.path.isdir(TODO_DIR):
    #    print("[*] No todo directroy found")
    #    os.mkdir(TODO_DIR, mode=0o760)
    #    print(f"    Created directory: {TODO_DIR}")

    # if not os.path.isfile(CONFIG):
    #    print(f"[ERROR] Config file, {CONFIG}, does not exist")
    #    return 1

    # Read config
    # config = configparser.ConfigParser()
    # config.read(CONFIG)

    config.read_configuration_file()

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
        cli.actions.list_tasks()
        return 0

    # Parse arguments
    argument_parser = {
        "a": cli.actions.add_task,
        "e": cli.actions.edit_task,
        "d": cli.actions.delete_task,
        "f": cli.actions.finish_task,
        "h": cli.actions.usage,
        "l": cli.actions.list_tasks,
        # "s" : sort_tasks,
        "u": cli.actions.unfinish_task,
        # "v" : Version,
        # "t" : testtesttest,
        # Long actions
        "add": cli.actions.add_task,
        "edit": cli.actions.edit_task,
        "delete": cli.actions.delete_task,
        "finish": cli.actions.finish_task,
        "unfinish": cli.actions.unfinish_task,
        "help": cli.actions.usage,
        "list": cli.actions.list_tasks,
        # "sort"  : sort_tasks,
        # "test"  : testtesttest,
        # "util"  : utilities,
        # "version": version,
    }

    # Check the first argument and default to Usage()
    argument_parser.get(sys.argv[1], cli.actions.usage)(sys.argv[2:])


if __name__ == "__main__":
    exit(main())
