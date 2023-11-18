# Step 1: Import the socket module
import socket

# Step 2: Create a UDP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Step 3: Define server address and port
server_address = ('192.168.1.25', 12345)

# Step 4: Send data
message = 'This is the message. It will be echoed back.'
try:
    while True:
        # Ask user for input
        user_input = input("Enter Message:")
        
        # Send data
        sent = client_socket.sendto(user_input.encode(), server_address)

        # Step 5: Receive response
        print("Waiting to receive")
        data, server = client_socket.recvfrom(4096)
        print("Received:", data.decode())



finally:
    # Step 6: Close the socket
    print("Closing socket")
    client_socket.close()
