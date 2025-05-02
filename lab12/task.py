class Task:
    """A class representing a single task."""
    def __init__(self, desc, date, time):
        self.description = desc
        self.date = date  # format: MM/DD/YYYY
        self.time = time  # format: HH:MM

    def __str__(self):
        return f"{self.description} - Due: {self.date} at {self.time}"

    def __repr__(self):
        return f"{self.description},{self.date},{self.time}"

    def __lt__(self, other):
        m1, d1, y1 = map(int, self.date.split('/'))
        m2, d2, y2 = map(int, other.date.split('/'))
        h1, min1 = map(int, self.time.split(':'))
        h2, min2 = map(int, other.time.split(':'))
        return (y1, m1, d1, h1, min1, self.description) < (y2, m2, d2, h2, min2, other.description)

