class Project:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)