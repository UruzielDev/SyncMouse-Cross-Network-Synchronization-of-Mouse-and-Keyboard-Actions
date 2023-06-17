import socket
from pynput.keyboard import Controller as KeyboardController

HOST = '0.0.0.0'  # Server IP address
PORT = 5000  # Port number

keyboard = KeyboardController()


def client_thread(conn):
    while True:
        message = conn.recv(1024).decode()
        if not message:
            break

        x, y, action = message.split(',')

        if action == "left_click":
            print("Performing left-click action")
            # Perform left-click action here
        elif action == "right_click":
            print("Performing right-click action")
            # Perform right-click action here
        elif action == "move":
            print(f"Performing mouse move action to {x}, {y}")
            # Perform mouse move action here
        elif action.startswith("key"):
            keys = action.split(":")[1:]
            print(f"Simulating key presses: {keys}")
            for key in keys:
                keyboard.press(key)
                keyboard.release(key)


# Create a socket object to establish the server's connection
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the IP address and port number
server_socket.bind((HOST, PORT))
# Start listening for incoming connections:
server_socket.listen(1)
print("Server is listening...")
# Accept a client connection and print the client's address
client_socket, address = server_socket.accept()
print("Client connected:", address)

client_thread(client_socket)
