from KeyPressMap import KEYS
import time
import socket

SERVER_ADDRESS = "192.168.1.4"
SERVER_PORT = 6563

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

SEND_FREQUENCY = 5
MAX_SEND_VALUE = 1023


def getMovement():
    move = 0
    turn = 0

    if KEYS.isPressed("w") or KEYS.isPressed("Up"):
        move += MAX_SEND_VALUE

    if KEYS.isPressed("s") or KEYS.isPressed("Down"):
        move -= MAX_SEND_VALUE

    if KEYS.isPressed("d") or KEYS.isPressed("Right"):
        turn += MAX_SEND_VALUE

    if KEYS.isPressed("a") or KEYS.isPressed("Left"):
        turn -= MAX_SEND_VALUE

    return (move, turn)


def sendMovement(movement):
    #encode movement
    movementString = str(movement[0]) + ":" + str(movement[1])

    print("sending:", movementString)

    #send
    SOCKET.sendto(movementString.encode(), (SERVER_ADDRESS, SERVER_PORT))

def SendingThread():

    delay = 1.0 / SEND_FREQUENCY
    
    while True:

        movement = getMovement()

        sendMovement(movement)

        time.sleep(delay)
    
