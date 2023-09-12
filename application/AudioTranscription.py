from tkinter import *
import os

app = Tk()
app.title("NExT-2023 - M01 Audio To Text")
app.geometry("500x300")
app.configure(background="#dde")

def semComando():
    print("")

barraDeMenus=Menu(app)
menuSpeechToText=Menu(barraDeMenus)
menuSpeechToText.add_command(label="Audio File (wav)", command=semComando)
menuSpeechToText.add_command(label="Microphne", command=semComando)
menuSpeechToText.add_command(label="Alexa", command=semComando)
menuSpeechToText.add_separator()
menuSpeechToText.add_command(label="Close", command=app.quit)

app.mainloop()
