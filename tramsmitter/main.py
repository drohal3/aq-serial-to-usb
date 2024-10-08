import serial
import time
import json

PORT = "/dev/ttyS0"

data = {
    "device_id": "test_0",
    "temperature": 25.6,
    "humidity": 70
}
def transmit(n: int = -1):
    ser = serial.Serial(
        port=PORT,
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=3.0
    )
    try:
        loop = 0
        while True:
            if loop == n:
                print("Transmission completed!")
                break
            message = {**data, "n": loop}
            print("Transmitting: ", json.dumps(message))
            json_message = json.dumps(message)
            ser.write((json_message + '\n').encode("utf-8"))
            time.sleep(1)
            loop += 1
    except KeyboardInterrupt:
        print("Transmission completed!")
    finally:
        ser.close()


if __name__ == '__main__':
    transmit()
