import socket
import threading

def create_server(host, port):
    # udp server
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))
    return server

def listen_for_messages(server, buffer_size=1024):
    while True:
        data, addr = server.recvfrom(buffer_size)
        print(f"\nReceived message from User 2: {data.decode()} from {addr}")

def send_message(client, host, port, message):
        client.sendto(message.encode(), (host, port))

# Configuration
host = 'localhost'
user1_port = 12345
user2_port = 12346

# Create server and client for user 1
user1_server = create_server(host, user1_port)
user1_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Start a thread to listen for messages from User 2, will be ran in the background
threading.Thread(target=listen_for_messages, args=(user1_server,)).start()

# Example sending a message from user 1 to user 2
while True:
    message = input("Enter your message (User 1): ")
    send_message(user1_client, host, user2_port, message)

# Remember to close the sockets when done
# user1_server.close()
# user1_client.close()