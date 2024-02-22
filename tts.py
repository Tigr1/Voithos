import speech_recognition as sr
from speech_recognition.exceptions import UnknownValueError
import pyttsx3
import serial


porta = "COM3"
velocidade = 9600


conexao = serial.Serial(porta, velocidade);


r = sr.Recognizer()
engine = pyttsx3.init()
comando1 = "acender"
comando2 = "apagar"
comando3 = "piscar"
comando4 = "parar"
luzes = False
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[2].id)

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

    if comando1 in fala:
        conexao.write(b'a')
        print(True)
        print("Luz acesa")
        engine.say("Luz acesa")
        engine.runAndWait()

    elif comando2 in fala:
        conexao.write(b'A')
        print(luzes)
        print("Luz apagada")
        engine.say("Luz apagada")
        engine.runAndWait()

    elif comando3 in fala:
        conexao.write(b'b')
        print(luzes)
        print("Luzes piscando")
        engine.say("Luzes piscando")
        engine.runAndWait()

    elif comando4 in fala:
        conexao.write(b'B')
        print(luzes)
        print("Luzes desligadas")
        engine.say("Luzes desligadas")
        engine.runAndWait()    

    del fala
    del audio    

conexao.close()
