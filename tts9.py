import serial
from pyfirmata import Arduino, SERVO, util
from time import sleep
from serial import Serial

port = 'COM3'
velocidade = 9600

comando1 = "acender"
comando2 = "apagar"
comando3 = "pisca"
comando4 = "parar"
luzes = False



conexao = serial.Serial(port, velocidade)

while True:
    comando = input("Insira 'a' para acender o led vermelho, insira 'c' para acender o led verde, insira 'b' para piscar o led vermelho, insira 'A' para apagar o led vermelho, insira 'C' para apagar o led verde, insira 'B' para parar de piscar o led vermelho: ")

    if comando == "a":
        conexao.write(b'a')

    elif comando == "A":
        conexao.write(b'A')

    elif comando == "c":
        conexao.write(b'c')

    elif comando == "C":
        conexao.write(b'C')

    elif comando == "b":
        conexao.write(b'b')

    elif comando == "B":
        conexao.write(b'B')

