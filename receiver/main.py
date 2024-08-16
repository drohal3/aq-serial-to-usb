import serial
import time

PORT = "/dev/ttyUSB0"

def read():
    port = serial.Serial(PORT, baudrate=9600)
    while True:
        x = port.readline()
        print(x)


if __name__ == '__main__':
    read()
