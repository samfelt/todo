from enum import Enum, auto


class Project(object):
    """Contain all in information for a Project."""

    class State(Enum):
        """Define the possible states of a task."""

        NEW = auto()
        IN_PROGRESS = auto()
        COMPLETE = auto()

    def __init__(self, name):
        """Initialize a new, empty Project."""

        self.tasks = []
        self.name = name
        self.state = self.State.NEW

    def str_name(self, percentage=False):
        """Return a printable string with the name of the project. Include the
        percentage complete if required."""

        return_string = self.name
        if percentage:
            return_string += f" ({str(self.percent_finished())}%)"
        return return_string

    def str_in_file_format(self, print_tasks=False):
        """Return a string that can be printed to todo.txt. Include all tasks
        in project if required"""

        return_string = f"| {self.name} |"
        if print_tasks:
            for t in self.tasks:
                return_string += t.str_in_file_format()
        return return_string

    def add_task(self, t):
        """Add a task to list of tasks."""
        self.tasks.append(t)

    def set_state(self, s):
        """Set the stat of the project."""
        self.state = s

    def set_name(self, n):
        """Set the name of the project."""
        self.name = n

    def remove_task(self, index):
        """Remove task from list of tasks, based on index."""
        del self.tasks[index]

    def list_tasks(self, starting_number=None):
        """List the tasks in the tasks. Optionally number each task."""

        for t in self.tasks:
            if starting_number is not None:
                print(f"({starting_number:<2}) {t}")
                starting_number += 1
            else:
                print(f" {t}")

    def percent_finished(self):
        """Calculate the percetage of complete tasks as an integer."""

        if len(self.tasks) <= 0:
            return 0
        done = 0
        for t in self.tasks:
            if t.is_complete():
                done += 1
        return int(done / len(self.tasks) * 100)

    def get_number_of_tasks(self):
        """Return the number of task in the task list."""
        return len(self.tasks)

    def sort(self):
        """Sort the tasks in the task list to place all complete tasks at the
        end of the list."""

        if self.percent_finished != 0 and self.percent_finished != 100:
            completed_tasks = []
            index = 0
            for i in range(0, len(self.tasks)):
                if self.tasks[index].is_complete():
                    completed_tasks.append(self.tasks.pop(index))
                else:
                    index += 1

            for t in completed_tasks:
                self.tasks.append(t)
