from cgi import print_directory
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import os
import subprocess as sub
from dictionaries import sites, files, programs

name = 'Eva'
listenner = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 145)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            print('Escuchando...')
            pc = listenner.listen(source)
            rec = listenner.recognize_google(pc, language='es')
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
    except:
        pass

    return rec


def playYT(rec):
    video = rec.replace('reproduce', '')
    video = video.replace('youtube', '')
    talk('Reproduciendo' + video + 'youtube')
    pywhatkit.playonyt(video)


def buscaWiki(rec):
    search = rec.replace('busca', '')
    wikipedia.set_lang('es')
    wiki = wikipedia.summary(search, 1)
    print(search + ': ' + wiki)
    talk(wiki)


def abrirSitio(rec):
    for site in sites:
        if site in rec:
            sub.call(
                f'start MicrosoftEdge.exe {sites[site]}', shell=True)
            talk(f'Abriendo {site}')


def abrirArchivo(rec):
    for file in files:
        if file in rec:
            sub.Popen([files[file]], shell=True)
            talk(f'Abriendo {file}')


def abrirPrograma(rec):
    for app in programs:
        if app in rec:
            talk(f'Abriendo {app}')
            os.startfile(programs[app])


def run():
    while True:
        rec = listen()
        if 'detente' in rec or 'gracias' in rec or 'adiós' in rec:
            despedida = '¡Adiós!'
            print(despedida)
            talk(despedida)
            break
        elif 'reproduce' in rec and 'youtube' in rec:
            playYT(rec)
        elif 'busca' in rec:
            buscaWiki(rec)
        elif 'abre' in rec:
            abrirSitio(rec)
            abrirPrograma(rec)
        elif 'archivo' in rec:
            abrirArchivo(rec)


if __name__ == '__main__':
    run()
