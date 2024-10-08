# The Server running on RPi, listening for
# password auth sent by the ESP32 during Webcam initialization

import socket
import struct

# ENTER 192.168.0.18 FOR RASPBERRY PI
HOST = "192.168.0.20"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def getLine():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)       #Get Password from ESP
                if not data:
                    break
                # conn.sendall(bytes("Doorbell rung!", 'utf-8'))    # Send response to ESP32Cam
                print(f"Received", data.decode())               # Decode the password received
                # conn.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))
                # conn.close()
                s.shutdown(0)
                s.close()            # Close connection
              
                return data.decode()    # Returns the Message


def getPassword():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)       #Get Password from ESP
                if not data:
                    break
                conn.sendall(bytes("PW Received!", 'utf-8'))    # Send response to ESP32Cam
                print(f"Received PW", data.decode())               # Decode the password received
                # conn.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))
                # conn.close()
                s.shutdown(0)
                s.close()            # Close connection
              
                return data.decode(), addr    # Returns the Password and [IP Address, Port No]
