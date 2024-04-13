import socket
import threading

# สร้าง socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# กำหนด IP address และ port ที่จะให้ server ทำงาน
IP_ADDRESS = 'localhost'  # หรือ IP address ของเครื่องจริง
PORT = 1245

# ผูก socket กับ IP address และ port
server_socket.bind((IP_ADDRESS, PORT))

# เริ่มฟังก์ชันให้ server รอการเชื่อมต่อจาก client
server_socket.listen()

clients = []

def handle_client(client_socket):
    # รับชื่อจาก client
    username = client_socket.recv(1024).decode('utf-8') + ':'
    print(f'{username} เข้าร่วมแชท')
    
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f'{username} {message}')
                # ส่งข้อมูลกลับไปยัง client ทุกคน
                for client in clients:
                    # ตรวจสอบว่า client ที่รับข้อความนี้ไม่ใช่ client ที่ส่งข้อความ
                    if client is not client_socket:
                        client.send(f'{username} {message}'.encode('utf-8'))
            else: 
                # ถ้า client หลุดออกมาจากการเชื่อมต่อ
                print(f'{username} หลุดออกมาจากการเชื่อมต่อ')
                clients.remove(client_socket)
                client_socket.close()
                break
        except:
            clients.remove(client_socket)
            client_socket.close()  # ปิดการเชื่อมต่อ
            break
print("Server กำลังเปิดอยู่...")
# รอ client เข้ามาเชื่อมต่อ
while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    
    # เริ่ม thread ใหม่เพื่อจัดการการสื่อสารกับ client นี้
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
