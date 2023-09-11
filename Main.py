from stt_translator_tts_2  import SpeechToText

stt = SpeechToText()
texto = stt.convert_speech_to_text(microphone_input=True)
print("Texto reconhecido: ", texto)