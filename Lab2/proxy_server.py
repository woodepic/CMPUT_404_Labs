#Citations:
#I used components of client.py and echo_server.py to build this program

#to activate venv, use:     source myenv/bin/activate


import socket
from threading import Thread
import time #for validating multithreaded functionality

def start_server_st():
    while True:
        # Wait for a connection
        print("Waiting for a connection...")
        client_socket, client_address = proxy_server_socket.accept()
        handle_connection(client_socket, client_address)
    
def start_server_mt():
    while True:
        client_socket, client_address = proxy_server_socket.accept()
        thread = Thread(target=handle_connection, args=(client_socket, client_address))
        thread.start()

def handle_connection(client_socket, client_address):
    print(f"Accepted client connection from {client_address}")

    # Create a socket object for each client connection and connect to google
    google_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET indicated IPV4, and SOCK_STREAM indicates a TCP connection
    google_socket.connect((google_addr, 80))
    print(f"Connected client to {google_addr}...")

    time.sleep(10)

    #Echo text from client to google
    #Echo response from google to client
    request = b''
    while True:
        chunk = client_socket.recv(4096)
        if not chunk:
            break
        request += chunk

    google_socket.sendall(request)
    google_socket.shutdown(socket.SHUT_WR)

    response = b''
    while True:
        chunk = google_socket.recv(4096)
        if not chunk:
            break
        response += chunk
    client_socket.sendall(response)

    print("Proxy task completed. No more data. Closing connection.\n\n")
    client_socket.close()
    google_socket.close()







if __name__ == "__main__":
    google_addr = "www.google.com"

    #Create the socket used to talk to the client
    proxy_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_server_address = ('localhost', 8001)
    proxy_server_socket.bind(proxy_server_address)
    proxy_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    proxy_server_socket.listen(2)
    print("Proxy server is listening on port 8001...")

    start_server_st()
    #start_server_mt()