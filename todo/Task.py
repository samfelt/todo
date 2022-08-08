from enum import Enum, auto


class Task(object):
    """Contain all in information for a Task."""

    class State(Enum):
        """Define the possible states of a task."""

        NEW = auto()
        IN_PROGRESS = auto()
        COMPLETE = auto()

    def __init__(self, desc):
        """Initialize a new task with the given description."""

        self.state = self.State.NEW
        self.description = desc

    def __str__(self):
        """Return a formatted string to be printed to a terminal."""

        if self.is_complete():
            return f"[x] {self.description}"
        else:
            return f"[ ] {self.description}"

    def str_in_file_format(self, newline=False):
        """Return a string that can be placed directly in todo.txt."""
        return_string = ""
        if self.is_complete():
            return_string += f"[x] {self.description}"
        else:
            return_string += f"[ ] {self.description}"
        if newline:
            return_string += "\n"
        return return_string

    def set_derscription(self, desc):
        """Set the description of the task."""
        self.description = desc

    def finish(self):
        """Set the task as complete."""
        self.state = self.State.COMPLETE

    def unfinish(self):
        """Set the task as in progress."""
        self.state = self.State.IN_PROGESS

    def is_complete(self):
        """Return True if the task is complete."""
        if self.state == self.State.COMPLETE:
            return True
        else:
            return False

    def edit_description(self):
        """Interactively edit the description of the task."""
        print("edit_description still needs to be implimented.")
        """
        print(self.description)
        EDITOR = environ.get('EDITOR','vim')
        initial_description = self.description
        with tempfile.NamedTemporaryFile(suffix=".tmp") as tf:
            tf.write(initial_description.encode())
            tf.flush()
            call(
                [EDITOR, '+set backupcopy=yes', '+set nofixendofline', tf.name]
            )
            tf.seek(0)
            self.description=tf.read().decode()
        """
