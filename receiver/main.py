import serial
import time

PORT = "/dev/ttyUSB0"

def read():
    port = serial.Serial(
        port=PORT,
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=3.0
    )
    while True:
        x = port.readline()
        print(x)


if __name__ == '__main__':
    read()
