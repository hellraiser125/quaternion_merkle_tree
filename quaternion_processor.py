import struct

class QuaternionProcessor:
    def __init__(self, file_path):
        self.chunk_data = self.read_chunks_from_file(file_path)

    @staticmethod
    def read_chunks_from_file(file_path):
        """ Reads a file in chunks of 8 bytes and returns a dictionary with chunk numbers as keys and decimal values as values. If the chunk size is less than 8 bytes, the missing elements are padded with zeros. """
        chunk_dict = {}
        chunk_number = 1
        with open(file_path, 'rb') as file:  # Open in binary mode for byte reading
            while True:
                chunk = file.read(8)  # Read 8 bytes
                if not chunk:
                    break  # Exit if no more data to read
                if len(chunk) < 8:
                    chunk += b'\0' * (8 - len(chunk))  # Pad missing elements with zeros
                decimal_values = list(struct.unpack('B' * len(chunk), chunk))
                chunk_dict[chunk_number] = decimal_values
                chunk_number += 1
        return chunk_dict

    def make_quaternion(self) -> list:
        """ Process chunk data and calculate quaternion values.
        Returns:
            list: A list of quaternion parts (a, b, c, d)
        """
        quaternion_parts = []
        quaternions = []
        for decimal_values in self.chunk_data.values():
            quaternion = 0
            for index, data in enumerate(decimal_values, start=0):
                if data == 0:
                    quaternion += data
                else:
                    quaternion += data << 8 * index  # Use bitwise shift instead of pow
                #print(f"Quaternion part now --->  {quaternion}")
            quaternion_parts.append(quaternion)
            #print(f"Created part --->  {quaternion}")
            if len(quaternion_parts) == 4:
                quaternions.append(Quaternion(*quaternion_parts))
                quaternion_parts.clear()
        return quaternions

    
class Quaternion:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self):
        return f"{self.a} + ({self.b})i + ({self.c})j + ({self.d})k"

    def __mul__(self, other):
        a1, b1, c1, d1 = self.a, self.b, self.c, self.d
        a2, b2, c2, d2 = other.a, other.b, other.c, other.d
        modulus = 2**64


        # Виділення молодших та старших частин для кожної операції множення
        lower_64_bits_mask = (1 << 64) - 1
        # Для операції частини а
        a1a2_lower = (a1 * a2) & lower_64_bits_mask
        a1a2_higher = (a1 * a2) >> 64
        b1b2_lower = (b1 * b2) & lower_64_bits_mask
        b1b2_higher = (b1 * b2) >> 64
        c1c2_lower = (c1 * c2) & lower_64_bits_mask
        c1c2_higher = (c1 * c2) >> 64
        d1d2_lower = (d1 * d2) & lower_64_bits_mask
        d1d2_higher = (d1 * d2) >> 64

        #Отримання результату множення для частини a
        a1a2_product = (a1a2_lower + a1a2_higher) % modulus
        b1b2_product = (b1b2_lower + b1b2_higher) % modulus
        c1c2_product = (c1c2_lower + c1c2_higher) % modulus
        d1d2_product = (d1d2_lower + d1d2_higher) % modulus


        # Для операції частини b
        a1b2_lower = (a1 * b2) & lower_64_bits_mask
        a1b2_higher = (a1 * b2) >> 64
        b1a2_lower = (b1 * a2) & lower_64_bits_mask
        b1a2_higher = (b1 * a2) >> 64
        c1d2_lower = (c1 * d2) & lower_64_bits_mask
        c1d2_higher = (c1 * d2) >> 64
        d1c2_lower = (d1 * c2) & lower_64_bits_mask
        d1c2_higher = (d1 * c2) >> 64

        #Отримання результату множення для частини b
        a1b2_product = (a1b2_lower + a1b2_higher) % modulus
        b1a2_product = (b1a2_lower + b1a2_higher) % modulus
        c1d2_product = (c1d2_lower + c1d2_higher) % modulus
        d1c2_product = (d1c2_lower + d1c2_higher) % modulus 
        #print(f"Producrt a1b2_product--> {a1b2_product}")
        #print(f"Producrt b1a2_product--> {b1a2_product}")
        #print(f"Producrt c1d2_product--> {c1d2_product}")
        #print(f"Producrt d1c2_product--> {d1c2_product}")

        # Для операції частини c
        a1c2_lower = (a1 * c2) & lower_64_bits_mask
        a1c2_higher = (a1 * c2) >> 64
        c1a2_lower = (c1 * a2) & lower_64_bits_mask
        c1a2_higher = (c1 * a2) >> 64
        d1b2_lower = (d1 * b2) & lower_64_bits_mask
        d1b2_higher = (d1 * b2) >> 64
        b1d2_lower = (b1 * d2) & lower_64_bits_mask
        b1d2_higher = (b1 * d2) >> 64

        #Отримання результату множення для частини c
        a1c2_product = (a1c2_lower + a1c2_higher) % modulus
        c1a2_product = (c1a2_lower + c1a2_higher) % modulus
        d1b2_product = (d1b2_lower + d1b2_higher) % modulus
        b1d2_product = (b1d2_lower + b1d2_higher) % modulus

        # Для операції частини d
        a1d2_lower = (a1 * d2) & lower_64_bits_mask
        a1d2_higher = (a1 * d2) >> 64
        d1a2_lower = (d1 * a2) & lower_64_bits_mask
        d1a2_higher = (d1 * a2) >> 64
        b1c2_lower = (b1 * c2) & lower_64_bits_mask
        b1c2_higher = (b1 * c2) >> 64
        c1b2_lower = (c1 * b2) & lower_64_bits_mask
        c1b2_higher = (c1 * b2) >> 64

        #Отримання результату множення для частини d
        a1d2_product = (a1d2_lower + a1d2_higher) % modulus
        d1a2_product = (d1a2_lower + d1a2_higher) % modulus
        b1c2_product = (b1c2_lower + b1c2_higher) % modulus
        c1b2_product = (c1b2_lower + c1b2_higher) % modulus

        # Обчислення компонентів з виконанням операцій за модулем 2^64
        #a = ((a1a2_product - b1b2_product) % modulus - c1c2_product % modulus - d1d2_product % modulus) % modulus
        #b = ((a1b2_product + b1a2_product) % modulus + c1d2_product % modulus - d1c2_product % modulus) % modulus
        #c = ((a1c2_product + c1a2_product) % modulus + d1b2_product % modulus - b1d2_product % modulus) % modulus
        #d = ((a1d2_product + d1a2_product) % modulus + b1c2_product % modulus - c1b2_product % modulus) % modulus

        a_temp = (((a1a2_product - b1b2_product) - c1c2_product) - d1d2_product) 
        a = (a_temp + modulus) % modulus if a_temp < 0 else a_temp & lower_64_bits_mask

        b_temp = ((a1b2_product + b1a2_product) % modulus + c1d2_product % modulus - d1c2_product % modulus) % modulus
        b = (b_temp + modulus) % modulus if b_temp < 0 else b_temp & lower_64_bits_mask

        c_temp = ((a1c2_product + c1a2_product) % modulus + d1b2_product % modulus - b1d2_product % modulus) % modulus
        c = (c_temp + modulus) % modulus if c_temp < 0 else c_temp & lower_64_bits_mask

        d_temp = ((a1d2_product + d1a2_product) % modulus + b1c2_product % modulus - c1b2_product % modulus) % modulus
        d = (d_temp + modulus) % modulus if d_temp < 0 else d_temp & lower_64_bits_mask

        return Quaternion(a,b,c,d)

# def multiply_quaternions(quaternions):
#     result = quaternions[0] * quaternions[1]
#     print(f"After multiplying quaternion 1 and 2: {result}")

#     for quaternion in quaternions[2:]:
#         result = result * quaternion
#         print(f"After multiplying with next quaternion: {result}")
        

#     return result
def multiply_quaternions(quaternions):
    mul = quaternions[0]
    result = []
    print(f"Initial quaternion: {mul}")

    for i in range(1, len(quaternions)):
        mul = mul * quaternions[i]
        print(f"After multiplying with quaternion {i}: {mul}")
        result.append(mul)
    return result



   


