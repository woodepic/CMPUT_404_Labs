#Citations:
#I used chatGPT to provide a basic template for the structuring of this program.
#This template was modified to fit the requirements of the lab, and all code is
#fully understood. This is simply a time saving measure.

#to activate venv, use:     source myenv/bin/activate

import socket



server_host = "localhost"
server_port = 8001

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 8001)
server_socket.bind(server_address)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Listen for incoming connections
server_socket.listen()
print("Server is listening on port 8001...")


while True:
    # Wait for a connection
    print("Waiting for a connection...")
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    while True:
        # Receive data from the client
        data = client_socket.recv(1024)

        if data:
            #If not empty byte string
            # Echo the received data back to the client
            print(f"Received: {data.decode()}")
            client_socket.send(data)
        else:
            # If no data is received, close the connection
            print("No more data received. Closing connection.\n\n")
            client_socket.close()
            break