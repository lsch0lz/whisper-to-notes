import os

from todoist_api_python.api import TodoistAPI


class Todoist:
    def __init__(self):
        self.api = TodoistAPI(os.getenv("TODOIST_API_KEY"))

    def create_task(self, task_content: str, project_id: str):
        try:
            task = self.api.add_task(content=task_content, project_id=project_id)
            print(task)
        except Exception as error:
            print(error)
