from task import Task

class Tasklist:
    """A class to manage a list of Task objects."""
    def __init__(self):
        self.tasklist = []
        try:
            with open("tasklist.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 3:
                        task = Task(*parts)
                        self.tasklist.append(task)
            self.tasklist.sort()
        except FileNotFoundError:
            pass

    def add_task(self, desc, date, time):
        self.tasklist.append(Task(desc, date, time))
        self.tasklist.sort()

    def get_current_task(self):
        return self.tasklist[0] if self.tasklist else None

    def mark_complete(self):
        return self.tasklist.pop(0) if self.tasklist else None

    def save_file(self):
        with open("tasklist.txt", "w") as file:
            for task in self.tasklist:
                file.write(repr(task) + "\n")

    def __len__(self):
        return len(self.tasklist)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.tasklist):
            result = self.tasklist[self.n]
            self.n += 1
            return result
        raise StopIteration
