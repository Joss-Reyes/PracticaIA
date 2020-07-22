from tkinter import *
import speech_recognition as sr
import subprocess
import easygui

def clicked_dictar():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("You said: " + r.recognize_google(audio))

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def TextInput():
    #se obtiene el texto ingresado en la caja de texto
    texto_dictado = txtInput.get()
    print(texto_dictado)
    

def btnBuscar():
    #subprocess.Popen('Explorer /select,"C:Users/black/Documents/"')
    file = easygui.fileopenbox("C:Users/black/Documents/")

window = Tk()
window.title("Organizador de ideas")

window.geometry('900x500')

etiqueta = Label(window, text="          ")
etiqueta.grid(column=0, row=0)
etiqueta = Label(window, text="          ")
etiqueta.grid(column=0, row=2)

#Definicion de los botones en la interfaz
btnInputText = Button(window, text="Ingresa un texto", command=TextInput)
btnInputText.grid(column=2, row=1)

#Cargar un archivo de texto a el cuadro de texto
btnChargeDoc = Button(window, text="Buscar", command=btnBuscar)
btnChargeDoc.grid(column=4, row=1)

#Boton para iniciar el dictado
btnDicInputText = Button(window, text="Dicta un texto", command=clicked_dictar)
btnDicInputText.grid(column=2, row=3)


txtInput = Text(window)
txtInput.config(width=90, height=10, font=("Consolas",10))
txtInput.grid(column=3, row=4)

window.mainloop()


