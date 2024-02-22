import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import random
from datetime import datetime
import pywhatkit

hora = f'{datetime.now().hour}'
minuto = f'{datetime.now().minute}'

# Baixe os recursos necessários do NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Dados de treinamento
training_data = [
   ('Oi', 'cumprimento'),
   ('Como você esta?', 'cumprimento'),
   ('Qual e o seu nome?', 'identidade'),
   ('Me fale sobre voce', 'identidade'),
   ('O que você faz?', 'identidade'),
   ('Ola', 'cumprimento'),
   ('Estou bem, e voce?', 'pergunta'),
   ('Como vai voce?', 'pergunta'),
   ('Como voce esta', 'pergunta'),
   ('Estou bem tambem', 'afirmacao'),
   ('Eu estou otimo', 'afirmacao'),
   ('Nao poderia estar melhor', 'afirmacao'),
   ('Abrir', 'open'),
   ('Abra', 'open'),
   ('Que horas sao?', 'time'),
   ('Me diga as horas', 'time'),
   ('Toque', 'musica'),
   ('Quero ouvir', 'musica'),
   ('Tocar', 'musica'),
   ('Obrigado!', 'agradecimento'),
   ('Muito obrigado!', 'agradecimento'),
   ('Obrigado por sua ajuda', 'agradecimento'),
   ('Você foi muito util, obrigado', 'agradecimento'),
   ('Agradeço muito', 'agradecimento'),
]

# Pré-processamento de texto
def preprocess_text(text):
   tokens = word_tokenize(text.lower())
   tokens = [token for token in tokens if token.isalnum()]
   # Mantenha 'você' como uma palavra relevante
   tokens = [token for token in tokens if token not in stopwords.words('portuguese') or token == 'você']
   return tokens

# Extração de características
vectorizer = CountVectorizer(tokenizer=preprocess_text)
X_train = vectorizer.fit_transform([msg for msg, intent in training_data])

# Treinamento do modelo
y_train = [intent for msg, intent in training_data]
clf = MultinomialNB()
clf.fit(X_train, y_train)

def classify_message(message):
   X = vectorizer.transform([message])
   intent = clf.predict(X)[0]
   return intent

# Função para pré-processar a mensagem do usuário
def preprocess_user_input(user_input):
    tokens = preprocess_text(user_input)  # Chama a função preprocess_text para obter os tokens
    return ' '.join(tokens)

# Função para obter uma resposta com base na intenção
def get_response(intent, user_input):
    global musica
    if intent == 'musica':
        # Inicializa a música com a entrada do usuário
            
        data_training = dict(training_data)
        for msg, mensagem in data_training.items():
            if mensagem == 'musica':
                musica = user_input
                musica.replace(msg, '')
        
        response = random.choice(responses[intent]).format(musica=musica)
    elif intent in responses:
            response = random.choice(responses[intent])
    else:
            response = 'Desculpe, não entendi.'
    return response

# Função para reproduzir música no YouTube
def play_on_youtube(musica):
    pywhatkit.playonyt(musica)

# Dicionário de respostas
responses = {
    'cumprimento': ['Olá, em que posso ajudar?', 'Oi! Como vai você?'],
    'identidade': ['Eu sou um chatbot.', 'Me chamo Voithos.', 'Sou um programa de computador.'],
    'pergunta': ['Estou bem', 'Eu estou bem, obrigado por perguntar, e você como está?'],
    'afirmacao': ['Que bom', 'Fico feliz que esteja bem'],
    'open': ['Tudo bem', 'Sem problemas', 'Sim senhor'],
    'musica': ['Tocando {musica}', 'Certo, tocando {musica}'],
    'agradecimento': ['De nada!', 'Não há de quê.', 'Estou aqui para ajudar.', 'Sempre à disposição.', 'Foi um prazer ajudar.'],
    'despedida': ['Tchau!', 'Até logo!', 'Adeus!', 'Nos vemos depois.', 'Tenha um bom dia!'],
    'time': [f'São: {hora} horas e {minuto} minutos', f'Agora são: {hora} horas e {minuto} minutos', f'Nesse momento são: {hora} horas e {minuto} minutos']
}

# Interagindo com o chatbot
print('Chatbot: Olá! Como posso ajudar você hoje?')
while True:
    user_input = input('User: ')
    preprocessed_input = preprocess_user_input(user_input)
    intent = classify_message(preprocessed_input)
    response = get_response(intent, user_input)
    
    if intent == 'musica':
        print(f'Chatbot: {response}')
        play_on_youtube(musica)
    else:
        print('Chatbot:', response)
