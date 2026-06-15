#!/usr/bin/env python3

import serial
import time

PORT = "/dev/pioneer"

BAUD_RATES = [
    115200,
    9600,
    19200,
    38400,
    57600,
    115200
]

TEST_BYTES = [
    b"\xFA\xFB",
    b"\xFA\xFB\x00",
    b"\x00",
    b"\r",
    b"\n"
]

for baud in BAUD_RATES:

    print(f"\n{'='*50}")
    print(f"Testing baudrate: {baud}")
    print(f"{'='*50}")

    try:
        ser = serial.Serial(PORT, baud, timeout=1)

        time.sleep(1)

        for test in TEST_BYTES:

            print(f"\nTX: {test.hex(' ')}")

            ser.reset_input_buffer()
            ser.reset_output_buffer()

            ser.write(test)
            ser.flush()

            time.sleep(0.5)

            data = ser.read(256)

            if data:
                print(f"RX ({len(data)} bytes): {data.hex(' ')}")
                print("\n*** POSSIBLE RESPONSE DETECTED ***")
            else:
                print("RX: <no data>")

        ser.close()

    except Exception as e:
        print(f"ERROR: {e}")

print("\nFinished testing.")
