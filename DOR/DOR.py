import socket

HOST = "127.0.0.1"

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, 6969))
        s.listen()
        conn, addr = s.accept()

    with conn:
        print(f"connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(bytes("Received from Scheduler: ", 'utf-8') + data)
            data += bytes(" received", "utf-8")
            conn.sendall(data)
