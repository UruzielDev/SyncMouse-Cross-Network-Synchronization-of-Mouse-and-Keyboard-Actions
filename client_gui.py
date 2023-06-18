import socket
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController

HOST = '127.0.0.1'  # Server IP address
PORT = 5454  # Port number

mouse = MouseController()
keyboard = KeyboardController()
client_socket = None


def send_message(message):
    client_socket.send(message.encode())


def simulate_mouse_action(action, x, y):
    if action == "left_click":
        mouse.position = (int(x), int(y))
        mouse.click(Button.left)
    elif action == "right_click":
        mouse.position = (int(x), int(y))
        mouse.click(Button.right)
    elif action == "move":
        mouse.position = (int(x), int(y))


def simulate_keyboard_action(keys):
    for key in keys:
        if key == "enter":
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        elif key == "space":
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        else:
            keyboard.press(key)
            keyboard.release(key)


try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print("Connected to the server.")

    # Receive the server's IP address
    server_ip = client_socket.recv(1024).decode()
    print("Server IP:", server_ip)

    while True:
        action_input = input("Enter action (left_click, right_click, move, key): ")

        if action_input == "exit":
            break

        if action_input == "left_click" or action_input == "right_click" or action_input == "move":
            x_input = input("Enter x-coordinate: ")
            y_input = input("Enter y-coordinate: ")
            message_to_send = f"{x_input},{y_input},{action_input}"
            send_message(message_to_send)
            simulate_mouse_action(action_input, x_input, y_input)
        elif action_input == "key":
            keys_input = input("Enter keys (comma-separated): ").split(",")
            message_to_send = f"0,0,key:{':'.join(keys_input)}"
            send_message(message_to_send)
            simulate_keyboard_action(keys_input)

except ConnectionRefusedError:
    print("Failed to connect to the server at", HOST)

except Exception as e:
    print("An error occurred:", str(e))

finally:
    if client_socket:
        client_socket.close()
