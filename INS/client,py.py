import socket

def main():
    server_ip = '127.0.0.1'  # Change this to the IP address where the server is running
    server_port = 5501        # Change this to the port on which the server is listening
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect((server_ip, server_port))
        message = "This is a test packet with malware."
        client_socket.send(message.encode('utf-8'))
        print(f"Sent message to server: {message}")
    except ConnectionError:
        print("Failed to connect to the server.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
