from entities.SpeechToText  import SpeechToText
from entities.SpeechToText_1 import SpeechToText1
from entities.TextTranslation import TextTranslator

stt = SpeechToText1()
filename = "audio_file_1.wav"
text = stt.convert_speech_to_text(audio_file_path=filename)
print("Recognized text: ", text)