import socket as soc

HOST = '127.0.0.1'  
PORT = 65432

try:
	with soc.socket(soc.AF_INET, soc.SOCK_STREAM) as socket:
		socket.bind((HOST,PORT))
		socket.listen()
		connection, address = socket.accept()
		with connection:
			print(f"Connect by -> {address}")
			while True:
				data = connection.recv(1024)
				if not data:
					print("No data :)")
					break
				connection.sendall(data)
except:
	print("Server Socket Error")