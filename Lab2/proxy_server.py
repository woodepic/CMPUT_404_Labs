import socket

# Define the target host and port
target_host = "www.google.com"
target_port = 80  # Port 80 is the default HTTP port

# Create a socket object (to  connec to google)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET indicated IPV4, and SOCK_STREAM indicates a TCP connection

# Connect to the server
client_socket.connect((target_host, target_port))

#receive text from client
#echo text to google
#Receive response from google
#echo response to client
#repeat