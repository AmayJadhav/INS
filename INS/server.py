import socket
import threading

class IDS:
    def __init__(self):
        self.signatures = ['malware', 'exploit', 'attack']

    def detect(self, packet):
        for sig in self.signatures:
            if sig in packet:
                print(f"Detected {sig} in packet: {packet}")

def listen(ids):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', 5501))
        s.listen(5)
        print("Listening for traffic...")
        while True:
            conn, addr = s.accept()
            print(f"Connection from {addr}")
            packet = conn.recv(1024).decode('utf-8')
            ids.detect(packet)
            conn.close()

if __name__ == "__main__":
    threading.Thread(target=listen, args=(IDS(),)).start()
