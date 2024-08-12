import socket


def tcp_client():

    # create a socket object

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # define the server and address

    server_adress = ("localhost", 12345)

    # connect to the server

    client_socket.connect(server_adress)

    try:
        # send a message to the server

        message = "Hello, Server !"
        client_socket.sendall(message.encode())


        # Receive the response from the server

        response = client_socket.recv(1024)
        print(f"Response from the server : {response.decode()}")

    finally:
        # close the socket

        client_socket.close()

if __name__ == "__main__":
    tcp_client()