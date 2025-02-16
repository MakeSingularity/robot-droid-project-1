import socket
import threading

class PiCommunication:
    def __init__(self, host='0.0.0.0', port=5000):
        self.host = host
        self.port = port
        self.server_socket = None
        self.client_socket = None

    def start_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        print(f"Server listening on {self.host}:{self.port}")
        self.client_socket, addr = self.server_socket.accept()
        print(f"Connection established with {addr}")

        threading.Thread(target=self.receive_data).start()

    def receive_data(self):
        while True:
            try:
                data = self.client_socket.recv(1024)
                if not data:
                    break
                print(f"Received data: {data.decode()}")
            except Exception as e:
                print(f"Error receiving data: {e}")
                break

    def send_data(self, message):
        try:
            self.client_socket.sendall(message.encode())
            print(f"Sent data: {message}")
        except Exception as e:
            print(f"Error sending data: {e}")

    def close_connection(self):
        if self.client_socket:
            self.client_socket.close()
        if self.server_socket:
            self.server_socket.close()
        print("Connection closed")