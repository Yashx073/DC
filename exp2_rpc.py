import pickle
import socket
import threading
import time


class RPCServer:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


def server_program():
    server = RPCServer()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 6000))
    s.listen(1)

    print("RPC Server: Waiting for client...")

    conn, addr = s.accept()
    print("RPC Server: Client connected from", addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break

        function_name, args = pickle.loads(data)
        print(f"RPC Server: Request -> {function_name}{args}")

        result = getattr(server, function_name)(*args)
        conn.send(pickle.dumps(result))

    conn.close()
    s.close()


def client_program():
    time.sleep(1)

    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(("127.0.0.1", 6000))

    request = ("add", (10, 20))
    c.send(pickle.dumps(request))
    result = pickle.loads(c.recv(1024))
    print("RPC Client: add(10,20) =", result)

    request = ("multiply", (5, 6))
    c.send(pickle.dumps(request))
    result = pickle.loads(c.recv(1024))
    print("RPC Client: multiply(5,6) =", result)

    c.close()


if __name__ == "__main__":
    server_thread = threading.Thread(target=server_program)
    client_thread = threading.Thread(target=client_program)

    server_thread.start()
    client_thread.start()

    server_thread.join()
    client_thread.join()

# Pip command for this file:
# python -m pip install --upgrade pip
# Note: This script uses only Python standard-library modules.
