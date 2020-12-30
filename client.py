import socket as soc

HOST = '127.0.0.1'
PORT = 65432


with soc.socket(soc.AF_INET, soc.SOCK_STREAM) as socket:
	socket.connect((HOST,PORT))
	socket.sendall(b'Hello, world')
	data = socket.recv(1024)
	print(f"Recived data -> {repr(data)}")