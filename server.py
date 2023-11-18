# Step 1: Import the socket module
import socket

# Step 2: Create a UDP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Step 3: Bind the socket to an address and port
server_socket.bind(('localhost', 12345))
print("UDP Server ready on port 12345")

# Step 4: Handle incoming messages and echo back
while True:
    data, address = server_socket.recvfrom(4096)
    print("Received message:", data.decode(), "from", address)

    # if data:
    #     sent = server_socket.sendto("Hi im replying from server".encode(), address)
    #     print("Sent message back to", address)

# Step 5: Close the socket (This will actually never be reached in this example, as the loop is infinite)
server_socket.close()
