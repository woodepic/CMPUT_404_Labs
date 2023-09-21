import socket

google_addr = "www.google.com"

#Create the socket used to talk to the client
proxy_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxy_server_address = ('localhost', 8001)
proxy_server_socket.bind(proxy_server_address)
proxy_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
proxy_server_socket.listen()
print("Proxy server is listening on port 8001...")

while True:
    # Wait for a connection
    print("Waiting for a connection...")
    client_socket, client_address = proxy_server_socket.accept()
    print(f"Accepted client connection from {client_address}")

    # Create a socket object and connect to google
    google_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET indicated IPV4, and SOCK_STREAM indicates a TCP connection
    google_socket.connect((google_addr, 80))
    print(f"Connected client to {google_addr}...")


    #Echo text from client to google
    #Echo response from google to client
    while True:
        data = client_socket.recv(4096)
        if data:
            google_socket.send(data)
            google_socket.shutdown(socket.SHUT_WR)
            response = google_socket.recv(4096)
            client_socket.send(response)

        else:
            # If no data is received, close the connection
            print("No more data received. Closing connection.\n\n")
            client_socket.close()
            google_socket.close()
            break