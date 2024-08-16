import serial
import time

PORT = "/dev/ttyS0"
def transmit(n: int = 1):
    port = serial.Serial(
        port=PORT,
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=3.0
    )
    for i in range(n):
        message = f"Hello {i}"
        port.write(message.encode("utf-8"))
    else:
        print("Transmission completed!")


if __name__ == '__main__':
    transmit()
