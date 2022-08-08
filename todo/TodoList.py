import shutil
from .Task import Task
from .Project import Project


class TodoList(object):
    """An object to represent a 'todo.txt' file"""

    def __init__(
        self, filename="todo.txt", encrypted=False, aes_passphrase=""
    ):
        """Initialize a todo file. Nothing is read in during initialization."""
        self.filename = filename
        self.projects = []
        self.encrypted = encrypted
        self.passphrase = aes_passphrase
        self.color_table = None

    def import_from_file(self):
        """Import a todo.txt file into the TodoFile object."""

        if self.filename is None:
            print("[ERROR]: no filename to import")

        """
        if self.encrypted:
            decrypted_string = util.decrypt_file_to_string(self.filename,
                                                           self.passphrase)
        """

        temp_project = Project("Temp Project")
        with open(self.filename, "r") as f:
            for line in f:
                char_key = line[0]
                if char_key == "[":
                    temp_task = Task(line[4:-1])
                    if line[1] == "x":
                        temp_task.finish()
                    temp_project.add_task(temp_task)
                elif char_key == "|":
                    if temp_project.percent_finished() == 100:
                        temp_project.set_state(temp_project.State.COMPLETE)
                    if temp_project.percent_finished() > 0:
                        temp_project.set_state(temp_project.State.IN_PROGRESS)
                    if temp_project.get_number_of_tasks() != 0:
                        self.projects.append(temp_project)
                    temp_project = Project("Temp Project")
                    temp_project.set_name(line[1:-2].strip())
            self.projects.append(temp_project)

    def export_file(self):
        if self.filename is None:
            print("ERROR: no filename to export to")
            exit()

        shutil.copyfile(self.filename, f"{self.filename}.bak")

        with open(self.filename, mode="w", encoding="utf-8") as f:
            for p in self.projects:
                f.write(p.str_in_file_format(print_tasks=True, newline=True))

    def list_tasks(self, starting_number=None):
        for p in self.projects:
            print(p.str_name())
            p.list_tasks(starting_number)
            if starting_number is not None:
                starting_number += len(p.tasks)
            print()
