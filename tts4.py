import subprocess
import speech_recognition as sr
from speech_recognition.exceptions import UnknownValueError
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[2].id)

def abrir_app(app):
    try:
        # Abre o aplicativo usando o comando do sistema operacional
        subprocess.Popen([app], shell=True)
        print(f"{app} aberto com sucesso.")
    except Exception as e:
        print(f"Erro ao abrir {app}: {e}")

app = "notepad.exe"
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
    if "abrir bloco de notas" in fala:
        abrir_app(app)