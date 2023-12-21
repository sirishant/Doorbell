# main() runs at boot

from machine import Pin
import time
import webcam
import servoControl

pin_button = Pin(12, mode=Pin.IN, pull=Pin.PULL_UP)
print("Welcome")

def main():
    while True:
        if pin_button.value() != 1:
            print("Button pushed down!")
            webcam.main()

if __name__ == '__main__':
    main()


