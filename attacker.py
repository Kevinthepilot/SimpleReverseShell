import sys
import socket
import threading


def handleMsg(client, server):
    while True:
        msg = client.recv(1024).decode("utf-8")
        print(msg)
        if (msg == '::q'): break



    client.close()

def handleCmd(client, server):
    pass



def main():
    IP = "localhost"
    PORT = 5555
    command_line = sys.argv
    for i in range(0, len(command_line)):
        if (command_line[i] == "-p"): 
            PORT = command_line[i+1]

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((IP, PORT))

    s.listen(1)
    print(f"Listening on port {PORT}...")

    while True:
        c, addr = s.accept()
        print(f"Established connection with {addr}")

        cnn = threading.Thread(target=handleMsg, args=(c,s,))
        cnn.start()

    s.close()

main()
