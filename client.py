import socket
from random import random

if __name__ == "__main__":

	HOST = 'localhost'
	PORT = 7777

	senha = int(random() * 1000)
	print(F"SENHA: {senha}\n")

	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((HOST, PORT))
	client.send(f'Eu sou o cliente com a senha {senha}, pode me prestar um serviço?!'.encode())
	response = client.recv(4096)
	print(response.decode())
	input("\nPressione qualquer botão para encerrar...")
