import os

from fastapi import FastAPI

from app.src.todoist import Todoist
from app.src.whisper import WhisperModel

app = FastAPI()

whsiper_model: WhisperModel = WhisperModel(model_type=os.getenv("MODEL_TYPE"))
todoist: Todoist = Todoist()


@app.post("/todoist/create_task/")
def create_todoist_task(audio_file: str, project_id: str):
    task_content: str = whsiper_model.convert_audio_to_text(audio_file=audio_file)
    todoist.create_task(task_content=task_content, project_id=project_id)
    return {"message": "Task created successfully!"}
