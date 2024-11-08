import random
import struct
import datetime

def rotate_left(byte, n):
    return ((byte << n) & 0XFF | (byte >> (8 - n)))

def rotate_right(byte, n):
    return ((byte >> n) | (byte << (8 - n)) & 0XFF )

with open('flag.enc', 'rb') as flag:
    seed_bytes = flag.read(4)
    seed = struct.unpack('<I', seed_bytes)[0]
    print(seed)
    print(datetime.datetime.utcfromtimestamp(seed))
    random.seed(seed)
    file_data = flag.read()

decrypted_flag = bytearray()

for byte in file_data:
    print(byte)
    rand_num1 = random.randint(0, 2**31-1)
    print(rand_num1)
    rand_num2 = random.randint(0, 2**31-1)
    rand_num2 = rand_num2 & 7
    print(rand_num2)
    #byte = rotate_right(byte, rand_num2)
    byte = (byte >> rand_num2 | (byte << (8 - rand_num2)) & 0XFF )
    byte = (byte ^ rand_num1) & 0XFF
    decrypted_flag.append(byte)

try:
    processed_string = decrypted_flag.decode('utf-8')
except:
    processed_string = decrypted_flag.decode('latin-1')

print(processed_string)

