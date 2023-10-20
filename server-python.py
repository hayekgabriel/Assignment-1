###############################################################################
# server-python.py
# Name: Gabriel Hayek
# EID: gah2475
###############################################################################

import sys
import socket

RECV_BUFFER_SIZE = 2048
QUEUE_LENGTH = 10

def server(server_port):
    """TODO: Listen on socket and print received message to sys.stdout"""
    a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    a.bind(('127.0.0.1', server_port))
    a.listen(QUEUE_LENGTH)
    conn, addr = a.accept()
    data = conn.recv(RECV_BUFFER_SIZE)
    sys.stdout.write(data)
    sys.stdout.flush()
    conn.close()
    


def main():
    """Parse command-line argument and call server function """
    if len(sys.argv) != 2:
        sys.exit("Usage: python server-python.py [Server Port]")
    server_port = int(sys.argv[1])
    server(server_port)

if __name__ == "__main__":
    main()
