from cgi import print_directory
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia

name = 'Eva'
listenner = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


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


def run():
    while True:
        rec = listen()
        if 'reproduce' in rec and 'youtube' in rec:
            video = rec.replace('reproduce', '')
            video = video.replace('youtube', '')
            talk('Reproduciendo' + video + 'youtube')
            pywhatkit.playonyt(video)
        elif 'busca' in rec:
            search = rec.replace('busca', '')
            wikipedia.set_lang('es')
            wiki = wikipedia.summary(search, 1)
            print(search + ': ' + wiki)
            talk(wiki)
        elif 'alarma' in rec:
            num = rec.replace('alarma', '')
            num = num.strip()
            talk('Alarma activada a las ' + num + 'horas')
        elif 'detente' in rec or 'gracias' in rec:
            despedida = '¡Adiós!'
            print(despedida)
            talk(despedida)
            break


if __name__ == '__main__':
    run()
