import socket
import threading

class my_thread(threading.Thread):
	def __init__(self, addr, client):
		threading.Thread.__init__(self)
		self.client = client
		self.addr = addr

	def run(self):
		handle_client(self.client, self.addr)


def handle_client(client_socket, addr):
	
	print(f'[*] Conexões ativas: {threading.active_count() - 1}')
	print('\n\tRecebendo Solicitação...')

	index = threading.get_native_id()

	request = client_socket.recv(1024)

	print('\n--------------------SOLICITAÇÃO--------------------')
	
	msg = request.decode()
	print(f'[#] Mensagem: {msg[:34:]}\n{msg[34::]}')
	print('---------------------------------------------------\n')
	
	client_socket.send(f'--------------------RECIBO--------------------\n[#] Serviço prestado pela thread {index}\n----------------------------------------------'.encode())
	client_socket.close()



if __name__ == '__main__':

	HOST = 'localhost'
	PORT = 7777

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((HOST, PORT))
	server.listen(100)

	print(f'[*] Escutando {HOST}:{PORT}')

	while True:
		client, addr = server.accept()

		print(f'[*] Conexão aceita de {addr[0]}:{addr[1]}')
		
		client_handler = my_thread(addr, client)
		client_handler.start()