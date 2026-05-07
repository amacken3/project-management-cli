from models.task import Task

class Project:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
    
    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "tasks": [task.to_dict() for task in self.tasks]
        }
    
    @classmethod
    def from_dict(cls, data):
        project = cls(
            data["title"],
            data["description"]
        )

        for task_data in data["tasks"]:
            task = Task.from_dict(task_data)
            project.add_task(task)

        return project