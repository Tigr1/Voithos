from googletrans import Translator
import speech_recognition as sr
from speech_recognition.exceptions import UnknownValueError
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[2].id)

def traduzir_texto_ingles(texto, destino='en'):
    translator = Translator()
    traducao = translator.translate(texto, dest=destino)
    return traducao.text

def traduzir_texto_portugues(texto, destino='pt'):
    translator = Translator()
    traducao = translator.translate(texto, dest=destino)
    return traducao.text

# Exemplo de uso
while True:
    with sr.Microphone() as source:
        audio = r.listen(source)
        print(audio)
    try:
        fala = r.recognize_google(audio, language='pt').lower()
    except UnknownValueError:
        print(f'Failed recognizing voice from input {str(audio)}')
        continue
    print(fala)

    if "traduza" in fala:
        while True:
            with sr.Microphone() as source:
                audio = r.listen(source)
                print(audio)
            try:
                if "inglês" in fala:
                    fala = r.recognize_google(audio, language='pt').lower()
                    idioma = 'en'
                    texto_traduzido = traduzir_texto_ingles(fala, idioma)
                    print(f'Texto original: {fala}')
                    print(f'Texto traduzido para {idioma}: {texto_traduzido}')
                elif "portugês" in fala:
                    fala = r.recognize_google(audio, language='en').lower()
                    idioma = 'pt'
                    texto_traduzido = traduzir_texto_portugues(fala, idioma)
                    print(f'Texto original: {fala}')
                    print(f'Texto traduzido para {idioma}: {texto_traduzido}')
            except UnknownValueError:
                print(f'Failed recognizing voice from input {str(audio)}')
                continue