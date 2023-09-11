import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def convert_speech_to_text(self, audio_file_path=None, microphone_input=False):
        try:
            if audio_file_path:
                with sr.AudioFile(audio_file_path) as source:
                    audio = self.recognizer.record(source)
            elif microphone_input:
                with sr.Microphone() as source:
                    print("Por favor, fale algo...")
                    audio = self.recognizer.listen(source)
            else:
                raise ValueError("Você deve fornecer um arquivo de áudio ou ativar o modo de entrada do microfone.")

            text = self.recognizer.recognize_google(audio, language="pt-BR")  # Reconhecimento usando o Google Web Speech API
            return text
        except sr.UnknownValueError:
            return "Não foi possível entender a fala."
        except sr.RequestError as e:
            return f"Erro na requisição para o serviço de reconhecimento de fala: {str(e)}"

# Exemplo de uso:
if __name__ == "__main__":
    stt = SpeechToText()
    # Para reconhecimento a partir de um arquivo de áudio:
    # texto = stt.convert_speech_to_text(audio_file_path="audio.wav")

    # Para reconhecimento a partir do microfone:
    texto = stt.convert_speech_to_text(microphone_input=True)
    print("Texto reconhecido: ", texto)
