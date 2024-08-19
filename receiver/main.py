import serial
import time

PORT = "/dev/ttyUSB0"

def read():
    ser = serial.Serial(
        port=PORT,
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=3.0
    )
    try:
        while True:
            response = ser.readline()
            if not response:
                print("No response received")
            print(f"Received: {response.decode('utf-8')}")
    except KeyboardInterrupt:
        pass
    finally:
        ser.close()


if __name__ == '__main__':
    read()
