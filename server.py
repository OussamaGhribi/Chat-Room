import socket
import threading

def handle_client(client_socket, clients):
    try:
        while True:
            msg = client_socket.recv(1024).decode("utf-8")
            if msg == "quit":
                break
            else:
                print("Received:", msg)
                send_to_all_clients(msg, clients, client_socket)

    except Exception as e:
        print(f"Error handling client: {e}")

    finally:
        remove_client(client_socket, clients)
        client_socket.close()

def send_to_all_clients(message, clients, sender_socket):
    for client_socket in clients:
        if client_socket != sender_socket:
            try:
                client_socket.send(message.encode('utf-8'))
            except socket.error:
                pass

def remove_client(client_socket, clients):
    if client_socket in clients:
        clients.remove(client_socket)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 9999))
    server.listen()

    print("Server is listening for incoming connections...")

    clients = []

    while True:
        client, addr = server.accept()
        print("Accepted connection from [", addr, "]")
        clients.append(client)

        client_handler = threading.Thread(target=handle_client, args=(client, clients))
        client_handler.start()

if __name__ == "__main__":
    start_server()
