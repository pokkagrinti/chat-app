import socket
import threading

def create_server(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))
    return server

def listen_for_messages(server, buffer_size=1024):
    while True:
        data, addr = server.recvfrom(buffer_size)
        print(f"\nReceived message from User 1: {data.decode()} from {addr}")

def send_message(client, host, port):
    while True:
        message = input("Enter your message (User 2): ")
        client.sendto(message.encode(), (host, port))

# Configuration
host = 'localhost'
user1_port = 12345
user2_port = 12346

# Create server and client for user 2
user2_server = create_server(host, user2_port)
user2_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Start a thread to listen for messages from User 1
threading.Thread(target=listen_for_messages, args=(user2_server,), daemon=True).start()

# Send messages to User 1
send_message(user2_client, host, user1_port)

# The sockets do not need to be closed here since the send_message function will loop indefinitely