import serial
import time

PORT = "/dev/ttyAMA0"
def transmit(n: int = 1):
    port = serial.Serial(PORT, baudrate=115200, timeout=3.0)
    for i in range(n):
        port.write(f"Hello {i}")
    else:
        print("Transmission completed!")


if __name__ == '__main__':
    transmit()
