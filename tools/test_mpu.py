from smbus2 import SMBus

for bus_num in [0, 1, 2, 4, 5, 7]:
    print(f"\nBUS {bus_num}")
    for addr in [0x68, 0x69]:
        try:
            bus = SMBus(bus_num)
            value = bus.read_byte_data(addr, 0x75)
            print(f"  {hex(addr)} -> WHO_AM_I = {hex(value)}")
            bus.close()
        except Exception as e:
            print(f"  {hex(addr)} -> {e}")
