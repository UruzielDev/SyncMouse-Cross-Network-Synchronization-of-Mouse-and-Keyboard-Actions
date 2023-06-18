import tkinter as tk
import requests


def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org').text
        return response
    except requests.exceptions.RequestException:
        return None


def copy_ip():
    ip_address = ip_label.cget("text")
    window.clipboard_clear()
    window.clipboard_append(ip_address)


# Create an instance of the Tkinter window
window = tk.Tk()
window.title("Server")

# Get the public IP address
ip_address_value = get_public_ip()

# Server IP label and copy button
ip_label = tk.Label(window, text="Server IP: " + ip_address_value)
ip_label.pack()

copy_ip_button = tk.Button(window, text="Copy IP", command=copy_ip)
copy_ip_button.pack()

# Server port label
port_label = tk.Label(window, text="Server Port: 5454")
port_label.pack()

# Set fixed window size
window.geometry("300x100")

# Run the main event loop
window.mainloop()
