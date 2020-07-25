from tkinter import *
import speech_recognition as sr
import easygui
import numpy as np
from os import path
import matplotlib.pyplot as plt
import random
from wordcloud import WordCloud, STOPWORDS

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
        text = r.recognize_google(audio)
        print("You said: " + text)
        #se imprime en la caja de texto lo dictado
        txtInput.insert(INSERT,text + " ")

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

#metodo para crear el cuadro de texto para poder escribir
def TextInput():
    txtInput.configure(state="normal")

#metodo para leer el texto de la caja de texto
def leer_texto():
    global textoIngresado
    textoIngresado = txtInput.get('1.0', END).lower()
    separar_palabras()

#metodo para separar el texto en palabras
def separar_palabras():
    palabras = textoIngresado.replace('\n', ' ').split()
    contar_palabras(palabras)

#metodo para contar las palabras
def contar_palabras(lista_palabras):
    frecuenciaPalabras = []
    for w in lista_palabras:
        frecuenciaPalabras.append(lista_palabras.count(w))
    
    print("Pares\n" + str(list(zip(lista_palabras, frecuenciaPalabras))))

    

#metodo para generar el resumen del texto ingresado
def resumen():
    leer_texto()

    GenResumen1 = Entry(window)
    GenResumen2 = Entry(window)
    GenResumen3 = Entry(window)

    GenResumen1.grid(column=2, row=8)
    GenResumen2.grid(column=2, row=9)
    GenResumen3.grid(column=2, row=10)
    
    GenResumen1.insert(INSERT,"palabras: ")
    GenResumen2.insert(INSERT,"palabras enlace: ")
    GenResumen3.insert(INSERT,"palabras clave: ")
    
    GenResumen1.configure(state="disabled")
    GenResumen2.configure(state="disabled")
    GenResumen3.configure(state="disabled")
    

def btnBuscar():
    #subprocess.Popen('Explorer /select,"C:Users/black/Documents/"')
    file = easygui.fileopenbox("C:Users/black/Documents/")

def nubePalabras():
    #text = 'Este recopilatorio adaptado por Mundo Primaria está pensado y desarrollado centrándose únicamente en el público infantil, por lo que hemos revisado, y preparado todas las historias que encontrarás aquí para que resulte asequible y sencillo de entender en los más pequeños y a su vez mantenga la atención y la intriga en los que son algo más mayores, incentivando así el hábito de la lectura desde la infancia.'
    text = txtInput.get('1.0', END).lower()
    wordcloud = WordCloud(font_path='C:/Windows/Fonts/Verdana.ttf',
                            relative_scaling = 0.1,
                            stopwords = {'que', 'y', 'en', 'el', 'por', 'las', 'a', 'la', 'de', 'lo', 'más', 'este'} # set or space-separated string
                            ).generate(text)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

window = Tk()
window.title("Organizador de ideas")

window.geometry('1000x500')

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

global txtInput
txtInput = Text(window)
txtInput.config(width=90, height=10, font=("Consolas",10))
txtInput.grid(column=3, row=4)
txtInput.configure(state="disabled")

btnResumen = Button(window, text="Generar resumen del texto anterior", command=resumen)
btnResumen.grid(column=2, row=7)

btnNubePalabras = Button(window, text="Generar nube de palabras", command=nubePalabras)
btnNubePalabras.grid(column=4, row=7)

window.mainloop()


