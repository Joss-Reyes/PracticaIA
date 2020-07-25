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

#metodo para contar las palabras
def contar_palabras():
    #obtener el texto de la caja de texto
    global textoIngresado
    textoIngresado = txtInput.get('1.0', END).lower()
    #separamos el texto en palabras
    global palabras
    palabras = textoIngresado.replace('\n', ' ').split()

    
def contar_palabras_enlace():
    enlace = ['y', 'además', 'también', 'asi mismo', 'también', 'igualmente',
            'encima', 'es más', 'más aún', 'incluso', 'hasta', 'para colmo', 
            'con todo', 'a pesar de todo', 'aun así', 'ahora bien', 'de cualquier modo', 'al mismo tiempo',
            'pero', 'sin embargo', 'no obstante', 'en cierto modo', 'en cierta medida', 'hasta cierto punto', 'si bien',
            'por otra parte', 'por el contrario', 'en cambio', 'por tanto', 'por consiguiente', 'de ahí que',
            'en consecuencia', 'así pues', 'por lo tanto', 'por eso', 'por lo que sigue', 'por esta razón',
            'entonces', 'de manera que', 'porque', 'pues', 'puesto que', 'del mismo modo', 'igualmente', 
            'análogamente', 'de modo similar', 'es decir', 'o sea', 'esto es', 'en otras palabras',
            'en resumen', 'en resumidas' 'cuentas', 'total', 'en una palabra', 'dicho de otro modo',
            'en breve', 'en síntesis', 'por ejemplo', 'así', 'así como', 'particularmente',  'específicamente',
            'para ilustrar', 'mejor dicho', 'bueno', 'en fin', 'por último', 'finalmente', 'para resumir',
            'por otro lado', 'a continuación', 'acto seguido', 'después', 'por cierto', 'a propósito', 'a todo esto',
            'después de', 'después que', 'después de que', 'luego', 'desde', 'desde que', 'desde entonces',
            'a partir de', 'antes de', 'antes que', 'antes de que', 'hasta que', 'en cuanto', 'al principio',
            'en el comienzo', 'inmediatamente', 'temporalmente', 'actualmente', 'cuando', 'en ese momento',
            'la', 'que', 'los', 'más', 'este', 'lo', 'le', 'el', 'de', 'en', 'por', 'está', 'para', 'aqui', 'hemos',
            'un', 'una', 'se']
    global pal_enlace 
    pal_enlace = []
    cont=0
    for x in enlace:
        for y in palabras:
            if x == y:
                pal_enlace.append(x)

   
    

#metodo para generar el resumen del texto ingresado
def resumen():
    contar_palabras()
    contar_palabras_enlace()

    GenResumen1 = Entry(window)
    GenResumen2 = Entry(window)
    GenResumen3 = Entry(window)

    GenResumen1.grid(column=2, row=8)
    GenResumen2.grid(column=2, row=9)
    GenResumen3.grid(column=2, row=10)
    
    GenResumen1.insert(INSERT,"palabras: " + str(len(palabras)))
    GenResumen2.insert(INSERT,"palabras enlace: " + str(len(pal_enlace)))
    GenResumen3.insert(INSERT,"palabras clave: " + str(len(palabras)-len(pal_enlace)))
    
    GenResumen1.configure(state="normal")
    GenResumen2.configure(state="normal")
    GenResumen3.configure(state="normal")
    

def btnBuscar():
    #subprocess.Popen('Explorer /select,"C:Users/black/Documents/"')
    file = easygui.fileopenbox("C:Users/black/Documents/")

def nubePalabras():
    #text = 'Este recopilatorio adaptado por Mundo Primaria está pensado y desarrollado centrándose únicamente en el público infantil, por lo que hemos revisado, y preparado todas las historias que encontrarás aquí para que resulte asequible y sencillo de entender en los más pequeños y a su vez mantenga la atención y la intriga en los que son algo más mayores, incentivando así el hábito de la lectura desde la infancia.'
    text = txtInput.get('1.0', END).lower()
    wordcloud = WordCloud(font_path='C:/Windows/Fonts/Verdana.ttf',
                            relative_scaling = 0.1,
                            stopwords = { 'y', 'además', 'también', 'asi mismo', 'también', 'igualmente',
                            'encima', 'es más', 'más aún', 'incluso', 'hasta', 'para colmo', 
                            'con todo', 'a pesar de todo', 'aun así', 'ahora bien', 'de cualquier modo', 'al mismo tiempo',
                            'pero', 'sin embargo', 'no obstante', 'en cierto modo', 'en cierta medida', 'hasta cierto punto', 'si bien',
                            'por otra parte', 'por el contrario', 'en cambio', 'por tanto', 'por consiguiente', 'de ahí que',
                            'en consecuencia', 'así pues', 'por lo tanto', 'por eso', 'por lo que sigue', 'por esta razón',
                            'entonces', 'de manera que', 'porque', 'pues', 'puesto que', 'del mismo modo', 'igualmente', 
                            'análogamente', 'de modo similar', 'es decir', 'o sea', 'esto es', 'en otras palabras',
                            'en resumen', 'en resumidas' 'cuentas', 'total', 'en una palabra', 'dicho de otro modo',
                            'en breve', 'en síntesis', 'por ejemplo', 'así', 'así como', 'particularmente',  'específicamente',
                            'para ilustrar', 'mejor dicho', 'bueno', 'en fin', 'por último', 'finalmente', 'para resumir',
                            'por otro lado', 'a continuación', 'acto seguido', 'después', 'por cierto', 'a propósito', 'a todo esto',
                            'después de', 'después que', 'después de que', 'luego', 'desde', 'desde que', 'desde entonces',
                            'a partir de', 'antes de', 'antes que', 'antes de que', 'hasta que', 'en cuanto', 'al principio',
                            'en el comienzo', 'inmediatamente', 'temporalmente', 'actualmente', 'cuando', 'en ese momento',
                            'la', 'que', 'los', 'más', 'este', 'lo', 'le', 'el', 'de', 'en', 'por', 'está', 'para', 'aqui', 'hemos',
                            'un', 'una', 'se'}
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


