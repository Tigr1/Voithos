import speech_recognition as sr
import webbrowser
from speech_recognition.exceptions import UnknownValueError
import pyttsx3
from datetime import datetime
import tkinter as tk
from tkinter import *
import wikipedia as wk
import pywhatkit
import serial
import pywhatkit as kt
import pyautogui
import subprocess
import requests
from googletrans import Translator
from pyfirmata import Arduino, SERVO, util
from time import sleep
from serial import Serial
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import random


engine = pyttsx3.init()

voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)

mamae = "+5547991211500"

def traduzir_texto_ingles(texto, destino='en'):
    translator = Translator()
    traducao = translator.translate(texto, dest=destino)
    return traducao.text

def traduzir_texto_portugues(texto, destino='pt'):
    translator = Translator()
    traducao = translator.translate(texto, dest=destino)
    return traducao.text

def abrir_notepad(notepad):
    try:
        # Abre o aplicativo usando o comando do sistema operacional
        subprocess.Popen([notepad], shell=True)
        print(f"{notepad} aberto com sucesso.")
        engine.say(f"{notepad} aberto com sucesso.")
        engine.runAndWait()
    except Exception as e:
        print(f"Erro ao abrir {notepad}: {e}")
        engine.say(f"Erro ao abrir {notepad}: {e}")
        engine.runAndWait()

notepad = "notepad.exe"


#porta = 'COM4'
#port = 'COM3'
velocidade = 9600

comando1 = "acender"
comando2 = "apagar"
comando3 = "pisca"
comando4 = "parar"
luzes = False

pin = 10
#board = Arduino(porta)

#board.digital[pin].mode = SERVO

#def rotate(pin, angle):
#    board.digital[pin].write(angle)
#    sleep(0.015)

#conexao = serial.Serial(port, velocidade)

hora = f'{datetime.now().hour}:{datetime.now().minute}'
data  = f'{datetime.now().day}/{datetime.now().month}'
ano = f'{datetime.now().year}'

#pergunta = "qual"
#pergunta2 = "onde"
#pergunta3 = "por que"
#pergunta4 = "como"
#pergunta5 = "o que"
#pergunta6 = "quem"
#pergunta7 = "quando"
toque = "toque"
tocar = "tocar"
ouvir = "eu quero ouvir"

new_text = "criar arquivo"



r = sr.Recognizer()
browser = webbrowser.get()
google = "google"
fechar = "fechar"
time = "horas"
dia = "dia"
year = "ano"
youtube = "youTube"
discord = "discord"
pausar = "pausar"

encerrar = "encerrar"

# Baixe os recursos necessários do NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Dados de treinamento
training_data = [
   ("Oi", "cumprimento"),
   ("Como você está?", "cumprimento"),
   ("Qual é o seu nome?", "identidade"),
   ("Me fale sobre você", "identidade"),
   ("O que você faz?", "identidade"),
   ("Olá", "cumprimento"),
   ("Estou bem, e você?", "pergunta"),
   ("Como vai você?", "pergunta"),
   ("Como voce está?", "pergunta"),
   ("Estou bem também", "afirmacao"),
   ("Eu estou ótimo", "afirmacao"),
   ("Não poderia estar melhor", "afirmacao"),
   # Adicione mais exemplos conforme necessário
]

# Respostas correspondentes a cada intenção
responses = {
    "cumprimento": ["Olá!", "Oi!", "Como vai?"],
    "identidade": ["Eu sou um chatbot.", "Me chamo Voithos.", "Sou um programa de computador."],
    "pergunta": ["Estou bem", "Eu estou bem, obrigado por perguntar, e você como está?"],
    "afirmacao": ["Que bom", "fico feliz que esteja bem"]
}

# Pré-processamento de texto
def preprocess_text(text):
   tokens = word_tokenize(text.lower())
   tokens = [token for token in tokens if token.isalnum()]
   # Mantenha "você" como uma palavra relevante
   tokens = [token for token in tokens if token not in stopwords.words('portuguese') or token == "você"]
   return tokens

# Extração de características
vectorizer = CountVectorizer(tokenizer=preprocess_text)
X_train = vectorizer.fit_transform([msg for msg, intent in training_data])

# Treinamento do modelo
y_train = [intent for msg, intent in training_data]
clf = MultinomialNB()
clf.fit(X_train, y_train)

# Função para classificar mensagens
def classify_message(message):
   X = vectorizer.transform([message])
   intent = clf.predict(X)[0]
   return intent

# Função para obter uma resposta com base na intenção
def get_response(intent):
    if intent in responses:
        return random.choice(responses[intent])
    else:
        return "Desculpe, não entendi."

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

    intent = classify_message(fala)
    response = get_response(intent)
    engine.say(response)
    engine.runAndWait()
    print(response)
            
    if google in fala:
        print("Abrindo o google")
        engine.say("Abrindo o google")
        engine.runAndWait()
        browser.open_new_tab("https://www.google.com.br/?hl=pt-BR")

    elif youtube in fala:
        print("Abrindo o youtube")
        engine.say("Abrindo o youtube")
        engine.runAndWait()
        browser.open_new_tab("http://www.youtube.com")
            
    elif discord in fala:
        print("Abrindo o Discord")
        engine.say("Abrindo o Discord")
        engine.runAndWait()
        browser.open_new_tab("https://discord.com/channels/@me/1170857980951015485")

    elif time in fala:
        print("São: ", hora)
        engine.say(f'São{hora}')
        engine.runAndWait()

    elif year in fala:
        print("Estamos no ano: ", ano)
        engine.say(f'Estamos no ano de{ano}')
        engine.runAndWait()

    elif dia in fala:
        print("hoje é dia: ", data)
        engine.say(f'hoje é dia{data}')
        engine.runAndWait()
    
    elif new_text in fala:
        print("Qual o nome do novo arquivo?")
        engine.say("Qual o nome do novo arquivo?")
        engine.runAndWait()
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            nome_arquivo = r.recognize_google(audio, language='pt')
            print("Nome do arquivo:", nome_arquivo)
        except UnknownValueError:
            print("Falha ao reconhecer o nome do arquivo.")
        
        print("O que desejas escrever?")
        engine.say("O que desejas escrever?")
        engine.runAndWait()
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            conteudo = r.recognize_google(audio, language='pt')
            print("Conteúdo do arquivo:", conteudo)
            with open(nome_arquivo + '.txt', 'a') as arquivo:
                arquivo.write(conteudo)
            print(f'Arquivo "{nome_arquivo}.txt" criado com sucesso!')
            nome_arquivo = ""  # Limpar o nome do arquivo após a criação
        except UnknownValueError:
            print("Falha ao reconhecer o conteúdo do arquivo.")

    if "adicionar" and "lista" in fala:
            with open("Lista de Compra.txt", "a") as lista:
                fala = fala.replace("adicionar", "")
                fala2 = fala.replace("lista", "")
                fala3 = fala2.replace("à", "")
                fala4 = fala3.replace("de", "")
                fala5 = fala4.replace("compras", "")
                fala6 = fala5.replace("compra", "")
                lista.write(fala6)


    #elif pergunta in fala:
     #   procurar = fala.replace(pergunta, '')
      #  wk.set_lang('pt')
       # result = wk.summary(procurar,2)
        #print(result)
        #engine.say(result)
        #engine.runAndWait()

    #elif pergunta2 in fala:
     #   procurar = fala.replace(pergunta2, '')
      #  wk.set_lang('pt')
       # result = wk.summary(procurar,2)
        #print(result)
        #engine.say(result)
        #engine.runAndWait()

    #elif pergunta3 in fala:
     #   procurar = fala.replace(pergunta3, '')
      #  wk.set_lang('pt')
       # result = wk.summary(procurar,2)
        #print(result)
        #engine.say(result)
        #engine.runAndWait()

    #elif pergunta4 in fala:
     #   procurar = fala.replace(pergunta4, '')
      #  wk.set_lang('pt')
       # result = wk.summary(procurar,2)
        #print(result)
        #engine.say(result)
        #engine.runAndWait()

    #elif pergunta5 in fala:
     #   procurar = fala.replace(pergunta5, '')
      #  wk.set_lang('pt')
       # result = wk.summary(procurar,2)
        #print(result)
        #engine.say(result)
        #engine.runAndWait()
    
    #elif pergunta6 in fala:
     #   procurar = fala.replace(pergunta6, '')
      #  wk.set_lang('pt')
       # result = wk.summary(procurar,2)
        #print(result)
        #engine.say(result)
        #engine.runAndWait()

    #elif pergunta7 in fala:
     #   procurar = fala.replace(pergunta7, '')
      #  wk.set_lang('pt')
       # result = wk.summary(procurar,2)
        #print(result)
        #engine.say(result)
        #engine.runAndWait()

    elif toque in fala:
        musica = fala.replace(toque, '')
        result = pywhatkit.playonyt(musica)
        engine.say(f'tocando {musica}')
        engine.runAndWait()

    elif tocar in fala:
        musica = fala.replace(tocar, '')
        result = pywhatkit.playonyt(musica)
        engine.say(f'tocando {musica}')
        engine.runAndWait()

    elif ouvir in fala:
        musica = fala.replace(ouvir, '')
        result = pywhatkit.playonyt(musica)
        engine.say(f'tocando {musica}')
        engine.runAndWait()

    elif pausar in fala:
        pyautogui.press('space')
        print("musica pausada")
        engine.say("musica pausada")
        engine.runAndWait()

    #elif comando1 in fala:
    #    conexao.write(b'a')
     #   print(True)
      #  print("Luz acesa")
       # engine.say("Luz acesa")
        #engine.runAndWait()

    #elif comando2 in fala:
     #   conexao.write(b'A')
      #  print(luzes)
       # print("Luz apagada")
        #engine.say("Luz apagada")
        #engine.runAndWait()

    #elif comando3 in fala:
     #   conexao.write(b'b')
      #  print(luzes) 
       # print("Luzes piscando")
        #engine.say("Luzes piscando")
        #engine.runAndWait()

    #elif comando4 in fala:
     #   conexao.write(b'B')
      #  print(luzes)
       # print("Luzes desligadas")
        #engine.say("Luzes desligadas")
        #engine.runAndWait()

    #if "esquerda" in fala:
     #   for i in range(0, 180):
      #      rotate(pin, i)

    #if "direita" in fala:
     #   for i in range(0, 90):
      #      rotate(pin, i)

    elif "bloco de notas" in fala:
            abrir_notepad(notepad)

    if "traduza" in fala or "traduzir" in fala:
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
                elif "português" in fala:  # Corrigindo a palavra 'português'
                    fala = r.recognize_google(audio, language='en').lower()
                    idioma = 'pt'
                    texto_traduzido = traduzir_texto_portugues(fala, idioma)
                    print(f'Texto original: {fala}')
                    print(f'Texto traduzido para {idioma}: {texto_traduzido}')
            except UnknownValueError:
                print(f'Failed recognizing voice from input {str(audio)}')
                continue
            break

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

    elif encerrar in fala:
        break

    del fala
    del audio