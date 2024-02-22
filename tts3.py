import pywhatkit as kt
import speech_recognition as sr
from speech_recognition.exceptions import UnknownValueError
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[2].id)
mamae = "+5547999368853"

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

    if "mamãe" in fala or "mãe" in fala:
        engine.say("oque desejas enviar?")
        engine.runAndWait()
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

            kt.sendwhatmsg_instantly(mamae, fala)
