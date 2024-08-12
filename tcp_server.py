import socket
import threading


def tcp_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # define the server and adress
    
    server_adress = ('localhost', 12345)

    server_socket.bind(server_adress)

    # Enable the connections
    server_socket.listen(5)

    print("Server is starting...")

    while True:
        client_socket, client_adress = server_socket.accept()

        try:
            # Receive data from client
            data = client_socket.recv(1024)

            print(f"Received data {data.decode()}")


        # send a response to the client
            response = "This is a message."
            client_socket.sendall(response.encode())
            resp = input("Entre com a resposta: ")

        finally:
#           close the client socket
            client_socket.close()


if __name__ == "__main__":
    tcp_server()




