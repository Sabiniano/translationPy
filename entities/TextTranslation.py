from googletrans import Translator

class TextTranslator:
    def __init__(self):
        self.translator = Translator()

    def translate(self, text, src_lang='auto', dest_lang='en'):
        translation = self.translator.translate(text, src=src_lang, dest=dest_lang)
        return translation.text

# Exemplo de uso:
# if __name__ == "__main__":
#    translator = TextTranslator()
#    texto = "Por favor, transforme essas linhas numa classe python para traduzir texto."
#    texto_traduzido = translator.translate(texto, src_lang='pt', dest_lang='en')
#    print(f"Texto original: {texto}")
#    print(f"Texto traduzido: {texto_traduzido}")
