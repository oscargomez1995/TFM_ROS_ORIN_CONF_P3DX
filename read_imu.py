from smbus2 import SMBus
import time

bus = SMBus(7)
addr = 0x68

bus.write_byte_data(addr, 0x6B, 0x00)

def read_word(reg):
    high = bus.read_byte_data(addr, reg)
    low = bus.read_byte_data(addr, reg + 1)
    value = (high << 8) | low
    if value >= 0x8000:
        value -= 65536
    return value

while True:
    ax = read_word(0x3B)
    ay = read_word(0x3D)
    az = read_word(0x3F)

    gx = read_word(0x43)
    gy = read_word(0x45)
    gz = read_word(0x47)

    print(f"ACC: {ax:6d} {ay:6d} {az:6d} | GYRO: {gx:6d} {gy:6d} {gz:6d}")
    time.sleep(0.1)