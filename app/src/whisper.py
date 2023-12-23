import whisper
import base64


class WhisperModel:
    def __init__(self, model_type: str):
        self.model = whisper.load_model(model_type)

    def convert_base64_to_audio(self, base64_string: str):
        decoded_data = base64.b64decode(base64_string)

        temp_file_path = "./audio_file.mp4"
        with open(temp_file_path, 'wb') as temp_file:
            temp_file.write(decoded_data)

    def convert_audio_to_text(self, audio_file: str) -> str:
        self.convert_base64_to_audio(base64_string=audio_file)
        return self.model.transcribe("./audio_file.mp4")["text"]