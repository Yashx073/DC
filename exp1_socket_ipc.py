import socket
import threading
import time


def server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = "127.0.0.1"
    port = 43290

    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server: Waiting for connection...")

    conn, addr = server_socket.accept()
    print("Server: Connected to", addr)

    message = conn.recv(1024).decode()
    print("Server: Received ->", message)

    response = "Hello Client, your message is received!"
    conn.send(response.encode())

    conn.close()
    server_socket.close()


def client_program():
    time.sleep(1)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 43290

    client_socket.connect((host, port))

    message = "Hello Server, this is Client!"
    client_socket.send(message.encode())

    response = client_socket.recv(1024).decode()
    print("Client: Received ->", response)

    client_socket.close()


if __name__ == "__main__":
    server_thread = threading.Thread(target=server_program)
    client_thread = threading.Thread(target=client_program)

    server_thread.start()
    client_thread.start()

    server_thread.join()
    client_thread.join()
