import tkinter as tk
import socket
import threading

# สร้าง socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# กำหนด IP address และ port ของ server
SERVER_IP = '17.ip.gl.ply.gg'  # หรือ IP address ของ server จริง
SERVER_PORT = 2059

client_socket.connect((SERVER_IP, SERVER_PORT))

Username = ""

# กำหนดตัวแปร flag เพื่อตรวจสอบว่าเป็นการส่งข้อความครั้งแรกหรือไม่
first_message = True

def send_message():
    global first_message
    global Username
    message = entry.get()
    client_socket.sendto(message.encode('utf-8'), (SERVER_IP, SERVER_PORT))
    if first_message:
        first_message = False
        Username = message
        text.insert(tk.END, message + "\n")
    else:
        response = f"{Username}: "+ message
        text.insert(tk.END, response + "\n")
    entry.delete(0, tk.END)

def receive_messages():
    while True:
        try:
            message, address = client_socket.recvfrom(1024)
            textToShow = message.decode('utf-8')
            text.insert(tk.END, textToShow + "\n")
        except Exception as e:
            print("Error receiving message:", e)
            break


receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

root = tk.Tk()
root.title("Messenger")

text = tk.Text(root)
text.pack()

label = tk.Label(root, text="Enter message:")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

text.insert(tk.END, "กรุณาใส่ชื่อของคุณ: ")

button = tk.Button(root, text="Send", command=send_message)
button.pack()

# เชื่อมต่อกับเหตุการณ์การกดปุ่ม Enter
entry.bind("<Return>", lambda event: send_message())

root.mainloop()