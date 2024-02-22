import random
from datetime import datetime

hora = f'{datetime.now().hour}:{datetime.now().minute}'

cumprimentos_voithos_manha = ['Bom dia senhor, com vai?', 'Olá senhor, como você está?', 'Bom dia senhor, dormiu bem?', f'Bom dia senhor, agora são: {hora}, o que o senhor deseja fazer?', 'Bom dia senhor, gostaria de ouvir uma música agora?']

cumprimentos_mestre_manha = ['bom dia voithos', 'olá voithos']

while True:
    digite = input("Tente dizer algo ao Voithos: ")

    for cumprimentos in cumprimentos_mestre_manha:
        if cumprimentos in digite:
            print(random.choice(cumprimentos_voithos_manha))