#Citations:
#I used chatGPT to provide a basic template for the structuring of this program.
#This template was modified to fit the requirements of the lab, and all code is
#fully understood. This is simply a time saving measure.

import socket

# Define the target host and port
target_host = "www.google.com"
target_port = 80  # Port 80 is the default HTTP port

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET indicated IPV4, and SOCK_STREAM indicates a TCP connection

# Connect to the server
client_socket.connect((target_host, target_port))

# Send a simple HTTP GET request using http 1.1
request = "GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n"
client_socket.send(request.encode())

client_socket.shutdown(socket.SHUT_WR)

response = client_socket.recv(4096)
while len(response) > 0:
    print(response)
    response = client_socket.recv(4096)


# Close the socket
client_socket.close()