# main() runs at boot

from machine import Pin
# from time import sleep
import webcam
# import servoControl
# import socket
# import usocket as soc
# from wifi import Sta

# pin_button = Pin(12, mode=Pin.IN, pull=Pin.PULL_UP)
print("Welcome")

# ENTER 192.168.0.18 FOR RASPBERRY PI
# HOST = "192.168.0.20" # Server address
# PORT = 65432

def main():
#     w = Sta()
#     # wait for wifi ready
#     w = Sta()
#     w.connect()
#     w.wait()
#     for i in range(5):
#         if w.wlan.isconnected(): break
#         else: print("WIFI not ready. Wait...");sleep(2)
#     else:
#         print("WIFI not ready. Can't continue!")
#         reset()
#     print("Waiting for button press..")
#     while(1):
#         if pin_button.value() != 1:
#             print("Button pushed down!")
#             s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             s.setsockopt(soc.SOL_SOCKET, soc.SO_REUSEADDR, 1)
#             s.connect((HOST, PORT))
#             sleep(1)
#             s.sendall(bytes('DINGDONG', 'utf-8'))
#             ## data = s.recv(1024)
#             s.close()
#             ## print(f"{data!r}")
#             # sleep(1)
#             print("Welcome to Webcam")
    webcam.main()

if __name__ == '__main__':
    main()


