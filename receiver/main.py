import serial
import time

PORT = "/dev/ttyAMA0"

def readline_cr(port):
    rv = ""
    while True:
        ch = port.read()
        rv += ch
        if ch == '\r' or ch == '':
            return rv

def read():
    port = serial.Serial(PORT, baudrate=9600)
    while True:
        rcv = readline_cr(port)
        print(rcv)


if __name__ == '__main__':
    read()
