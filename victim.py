import socket
import sys

command_line = sys.argv

IP = "localhost"
PORT = 5555

for i in range(0, len(command_line)):
    if (command_line[i] == "-p"): 
        PORT = command_line[i+1]
    elif (command_line[i] == '-h'):
        IP = command_line[i+1]

print(f"Connecting to {IP} on port {PORT}...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
print(f"Connected!")

try:
    while True:
        msg = input("CMD: ")
        s.send(bytes(msg, "utf-8"))
except KeyboardInterrupt:
    s.send(bytes("::q", "utf-8"))   
