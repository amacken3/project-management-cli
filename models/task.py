class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False
    
    def mark_complete(self):
        self.completed = True
    
    def to_dict(self):
        return {
            "title": self.title,
            "description":self.description,
            "due_date": self.due_date,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(
            data["title"],
            data["description"],
            data["due_date"]
        )

        task.completed = data["completed"]

        return task