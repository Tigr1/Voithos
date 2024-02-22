import serial


porta = "COM3"
velocidade = 9600

conexao = serial.Serial(porta, velocidade)


while True:

    acao = input("Insira um comando: ")

    if 'a' in acao:
        conexao.write(b'a')

    elif 'A' in acao:
        conexao.write(b'A')

    elif 'b' in acao:
        conexao.write(b'b')

    elif 'B' in acao:
        conexao.write(b'B')

conexao.close()