import socket

HOST = socket.gethostbyname('google.com')  # The server's hostname or IP address
PORT = 80        # The port used by the server

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created successfully")
except:
    print("Socket creation failed")

s.connect((HOST, PORT))
print("Connected successfullygethostbyname")