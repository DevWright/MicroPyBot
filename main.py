#!/usr/bin/python3           # This is server.py file
import socket
import move              

DISCONNECT_TIMEOUT = 5
HOST = ""
PORT = 6563
BOT = move.MicroPyBotMove()


class MoveData(object):
	HIGH_VAL = 1023
	LOW_VAL = -1023

	def __init__(self, move, turn):
		self.move = int(float(MoveData.clip(move, MoveData.HIGH_VAL, MoveData.LOW_VAL)))
		self.turn = int(float(MoveData.clip(turn, MoveData.HIGH_VAL, MoveData.LOW_VAL)))


	@staticmethod
	def clip(val, high, low):
		if val > high:
			return high
		elif val < low:
			return low
		else:
			return val 


def parseMessage(data):
	msg = data.decode("utf-8") 

	params = msg.split(":")

	if len(params) != 2:
		print("incorrect num of params. Returning 0:0")
		return MoveData(0,0)

	try:
		move = int(float(params[0]))
		turn = int(float(params[1]))
		return MoveData(move, turn)
	except ValueError:
		print("bad values sent. Returning 0:0")
		return MoveData(0,0)

def doCommand(moveData):
	print("command received:\nMove: " + str(moveData.move) + "\nTurn: " + str(moveData.turn)) 
	BOT.drive(moveData.move, moveData.turn)

def serve(hostname, port):
	# create a socket object
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                                     

	# bind to the port
	sock.bind((hostname, port))       

	while True:
		connected = False                                  
		data, recvAddr = sock.recvfrom(1024)
		command = parseMessage(data)

		connected = True
		print("connected to " + recvAddr[0] + ":" + str(recvAddr[1]))
		
		doCommand(command)

		while connected:
		    # set timeout to disconnect
			sock.settimeout(DISCONNECT_TIMEOUT)

			try:
				data, addr = sock.recvfrom(1024)

				command = parseMessage(data)

				if addr[0] != recvAddr[0]:
					print("wrong client: " + addr[0])
				else:
					doCommand(command)
				
			except OSError:
				connected = False
				sock.settimeout(None)
				print("disconnected from " + recvAddr[0] + " due to timeout")


if __name__ == "__main__":
	print("starting server...")
	serve(HOST, PORT)
	

