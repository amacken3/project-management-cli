from models.project import Project

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "projects": [project.to_dict() for project in self.projects]
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(
            data["name"],
            data["email"]
        )

        for project_data in data["projects"]:
            project = Project.from_dict(project_data)
            user.add_project(project)

        return user