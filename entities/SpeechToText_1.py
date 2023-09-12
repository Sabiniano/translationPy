import speech_recognition as sr

class SpeechToText1:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def convert_speech_to_text(self, audio_file_path=None, microphone_input=False):
        try:
            if audio_file_path:
                with sr.AudioFile(audio_file_path) as source:
                    audio_data = self.recognizer.record(source)
                    text = self.recognizer.recognize_google(audio_data)
            elif microphone_input:
                with sr.Microphone() as source:
                    print("Please say aomething...")
                    audio = self.recognizer.listen(source)
                    text = self.recognizer.recognize_google(audio, language="pt-BR")  # Recognition using Google Web Speech API
            else:
                raise ValueError("You should select an audio file or activate your microphone.")

            #text = self.recognizer.recognize_google(audio, language="pt-BR")  # Recognition using Google Web Speech API
            return text
        except sr.UnknownValueError:
            return "It was not possible to understand the speech."
        except sr.RequestError as e:
            return f"Error in the request to speech recognition service: {str(e)}"

# Exemplo de uso:
if __name__ == "__main__":
    stt = SpeechToText()
    # Para reconhecimento a partir de um arquivo de áudio:
    # texto = stt.convert_speech_to_text(audio_file_path="audio.wav")

    # Para reconhecimento a partir do microfone:
    texto = stt.convert_speech_to_text(microphone_input=True)
    print("Texto reconhecido: ", texto)