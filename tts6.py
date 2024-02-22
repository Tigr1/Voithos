from pyfirmata import Arduino
from pyfirmata import SERVO
from pyfirmata import util
from time import sleep
from serial import Serial

porta = 'COM3'
pin = 10
board = Arduino(porta)

board.digital[pin].mode = SERVO

def rotate(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.015)

while True:
    command = input('Digite para onde devo virar: ')
    if "esquerda" in command:
        for i in range(0, 180):
            rotate(pin, i)

    if "direita" in command:
        for i in range(0, 90):
            rotate(pin, i)


    