import socket as soc 
import sys

try:
    socket = soc.socket(soc.AF_INET,soc.SOCK_STREAM)
except sok.error as err:
    print(f"Socket creation failed with error {err}")

port = 80
host = "google.com" #--------> try host's as you want

try:
    host_ip = soc.gethostbyname(host)
except soc.gaierror:
    print("There is a error with resolving the host")
    sys.exit()

socket.connect((host_ip,port))
print(f"The socket has successfully connected to {host}")