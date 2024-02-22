import pyttsx3
from datetime import datetime

engine = pyttsx3.init()

voice = engine.getProperty('voices')

engine.setProperty('voice', voice[0].id)

hora = f'{datetime.now().hour}'
minuto = f'{datetime.now().minute}'
data  = f'{datetime.now().day} do {datetime.now().month}'
ano = f'{datetime.now().year}'

def cumprimentos():
    if hora >= '5' and hora < '12':
        engine.say(f'Bom dia doutor, agora são {hora} e {minuto}, hoje é dia {data}, em que posso ajuda-lo?')
        engine.runAndWait()
    
    if hora >= '12' and hora < '18':
        engine.say(f'Boa tarde doutor, agora são {hora} e {minuto}, hoje é dia {data}, em que posso ajuda-lo?')
        engine.runAndWait()
    
    if hora >= '18' and hora < '24':
        engine.say(f'Boa noite doutor, agora são {hora} e {minuto}, hoje é dia {data}, em que posso ajuda-lo?')
        engine.runAndWait()
    
    elif hora >= "24" and hora < "4":
        engine.say(f'Doutor, isso são {hora} e {minuto}, vai logo pra cama!!!')
        engine.runAndWait()

cumprimentos()