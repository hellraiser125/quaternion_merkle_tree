import struct
from typing import Union
"""

1. Создать клас который с полученого списка делает кватернион
2. Создать клас с вычислениями над кватернионом
3. Отдельный который определяет поведения програми в зависимости от количчества входных данных

Input:

n amount of Quaterion --> call 1st func
E.G

2 - first func
3 -

"""


# class Process

class QuaternionProcessor:
    def __init__(self, chunk_dict: Union[dict, list]):
        self.chunk_data = chunk_dict

    def make_quaternion(self, final_version=True) -> list:
        """ Process chunk data and calculate quaternion values.
        Returns:
            list: A list of quaternion parts (a, b, c, d)
        """
        # if final_version:
        #     return Quaternion()
        quaternion_parts = []
        quaternions = []

        # Type Guard if we have already processed data, just return `Quaternion` instance already
        if isinstance(self.chunk_data, (list,)):
            for data in self.chunk_data:
                quaternion_parts.append(data)
                if len(quaternion_parts) == 4:
                    #breakpoint()
                    quaternions.append(Quaternion(*quaternion_parts))
                    quaternion_parts.clear()
            return quaternions
            
        
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
    if isinstance(mul, (list,)):
        mul = mul[0]

    print(f"Initial quaternion: {mul}")

    for i in range(1, len(quaternions)):
        mul = mul * quaternions[i]
        print(f"After multiplying with quaternion {i}: {mul}")
        result.append(mul)
    return result

def perform_operations(quaternions):
    results = []
    lower_64_bits_mask = (1 << 64) - 1
    modulus = 2**64
    #print(f"Len: {len(quaternions)}")
    for i in range(len(quaternions)):
        a4, b4, c4, d4 = quaternions[i].a, quaternions[i].b, quaternions[i].c, quaternions[i].d
        
        # Перебираємо решту кватерніонів
        for j in range(i+1, len(quaternions)):
            a3, b3, c3, d3 = quaternions[j-1].a, quaternions[j-1].b, quaternions[j-1].c, quaternions[j-1].d
            a2, b2, c2, d2 = quaternions[j-2].a, quaternions[j-2].b, quaternions[j-2].c, quaternions[j-2].d
            a1, b1, c1, d1 = quaternions[j-3].a, quaternions[j-3].b, quaternions[j-3].c, quaternions[j-3].d
    
    # print(f"Quaternion 1 parts : {a1} -- {b1} -- {c1} -- {d1}")
    # print(f"Quaternion 2 parts : {a2} -- {b2} -- {c2} -- {d2}")
    # print(f"Quaternion 3 parts : {a3} -- {b3} -- {c3} -- {d3}")
    # print(f"Quaternion 4 parts : {a4} -- {b4} -- {c4} -- {d4}")
            
    # Виконуємо операції для частини a
    #result_b_1 = a1 * a3 * b3 * c3 * d3 * a4 * b4 * c4 * d4 * a2
    #result_a_2 = a1 * a3 * b3 * c3 * d3 * a4 * b4 * c4 * d4 * b2
    #result_b_1 = a1 * a3 * b3 * c3 * d3 * a4 * b4 * c4 * d4  * c2
    #result_a_4 = a1 * a3 * b3 * c3 * d3 * a4 * b4 * c4 * d4  * d24


    result_a_1 = (((a1 * a3) & lower_64_bits_mask) + ((a1 * a3) >>64)) % modulus
    result_a_1 = (((result_a_1 * b3) & lower_64_bits_mask) + ((result_a_1 * b3) >> 64)) % modulus
    result_a_1 = (((result_a_1 * c3) & lower_64_bits_mask) + ((result_a_1 * c3) >> 64)) % modulus
    result_a_1 = (((result_a_1 * d3) & lower_64_bits_mask) + ((result_a_1 * d3) >> 64)) % modulus
    result_a_1 = (((result_a_1 * a4) & lower_64_bits_mask) + ((result_a_1 * a4) >> 64)) % modulus
    result_a_1 = (((result_a_1 * b4) & lower_64_bits_mask) + ((result_a_1 * b4) >> 64)) % modulus
    result_a_1 = (((result_a_1 * c4) & lower_64_bits_mask) + ((result_a_1 * c4) >> 64)) % modulus
    result_a_1 = (((result_a_1 * d4) & lower_64_bits_mask) + ((result_a_1 * d4) >> 64)) % modulus
    result_a_1 = (((result_a_1 * a2) & lower_64_bits_mask) + ((result_a_1 * a2) >> 64)) % modulus

    result_a_2 = (((a1 * a3) & lower_64_bits_mask) + ((a1 * a3) >> 64)) % modulus
    result_a_2 = (((result_a_2 * b3) & lower_64_bits_mask) + ((result_a_2 * b3) >> 64)) % modulus
    result_a_2 = (((result_a_2 * c3) & lower_64_bits_mask) + ((result_a_2 * c3) >> 64)) % modulus
    result_a_2 = (((result_a_2 * d3) & lower_64_bits_mask) + ((result_a_2 * d3) >> 64)) % modulus
    result_a_2 = (((result_a_2 * a4) & lower_64_bits_mask) + ((result_a_2 * a4) >> 64)) % modulus
    result_a_2 = (((result_a_2 * b4) & lower_64_bits_mask) + ((result_a_2 * b4) >> 64)) % modulus
    result_a_2 = (((result_a_2 * c4) & lower_64_bits_mask) + ((result_a_2 * c4) >> 64)) % modulus
    result_a_2 = (((result_a_2 * d4) & lower_64_bits_mask) + ((result_a_2 * d4) >> 64)) % modulus
    result_a_2 = (((result_a_2 * b2) & lower_64_bits_mask) + ((result_a_2 * b2) >> 64)) % modulus
    
    result_a_3 = (((a1 * a3) & lower_64_bits_mask) + ((a1 * a3) >> 64)) % modulus
    result_a_3 = (((result_a_3 * b3) & lower_64_bits_mask) + ((result_a_3 * b3) >> 64)) % modulus
    result_a_3 = (((result_a_3 * c3) & lower_64_bits_mask) + ((result_a_3 * c3) >> 64)) % modulus
    result_a_3 = (((result_a_3 * d3) & lower_64_bits_mask) + ((result_a_3 * d3) >> 64)) % modulus
    result_a_3 = (((result_a_3 * a4) & lower_64_bits_mask) + ((result_a_3 * a4) >> 64)) % modulus
    result_a_3 = (((result_a_3 * b4) & lower_64_bits_mask) + ((result_a_3 * b4) >> 64)) % modulus
    result_a_3 = (((result_a_3 * c4) & lower_64_bits_mask) + ((result_a_3 * c4) >> 64)) % modulus
    result_a_3 = (((result_a_3 * d4) & lower_64_bits_mask) + ((result_a_3 * d4) >> 64)) % modulus
    result_a_3 = (((result_a_3 * c2) & lower_64_bits_mask) + ((result_a_3 * c2) >> 64)) % modulus

    result_a_4 = (((a1 * a3) & lower_64_bits_mask) + ((a1 * a3) >> 64)) % modulus
    result_a_4 = (((result_a_4 * b3) & lower_64_bits_mask) + ((result_a_4 * b3) >> 64)) % modulus
    result_a_4 = (((result_a_4 * c3) & lower_64_bits_mask) + ((result_a_4 * c3) >> 64)) % modulus
    result_a_4 = (((result_a_4 * d3) & lower_64_bits_mask) + ((result_a_4 * d3) >> 64)) % modulus
    result_a_4 = (((result_a_4 * a4) & lower_64_bits_mask) + ((result_a_4 * a4) >> 64)) % modulus
    result_a_4 = (((result_a_4 * b4) & lower_64_bits_mask) + ((result_a_4 * b4) >> 64)) % modulus
    result_a_4 = (((result_a_4 * c4) & lower_64_bits_mask) + ((result_a_4 * c4) >> 64)) % modulus
    result_a_4 = (((result_a_4 * d4) & lower_64_bits_mask) + ((result_a_4 * d4) >> 64)) % modulus
    result_a_4 = (((result_a_4 * d2) & lower_64_bits_mask) + ((result_a_4 * d2) >> 64)) % modulus
    
    #Операції для частини b
    #result_b_1 = b1 * a3 * b3 * c3 * d3 * a4 * b4 * c4 * d4 * a2
    #result_b_2 = b1 * a3 * b3 * c3 * d3 * a4 * b4 * c4 * d4 * b2
    #result_b_3 = b1 * a3 * b3 * c3 * d3 * a4 * b4 * c4 * d4 * c2
    #result_b_4 = b1 * a3 * b3 * c3 * d3 * a4 * b4 * c4 * d4 * d2

    result_b_1 = (((b1 * a3) & lower_64_bits_mask) + ((b1 * a3) >> 64)) % modulus
    result_b_1 = (((result_b_1 * b3) & lower_64_bits_mask) + ((result_b_1 * b3) >> 64)) % modulus
    result_b_1 = (((result_b_1 * c3) & lower_64_bits_mask) + ((result_b_1 * c3) >> 64)) % modulus
    result_b_1 = (((result_b_1 * d3) & lower_64_bits_mask) + ((result_b_1 * d3) >> 64)) % modulus
    result_b_1 = (((result_b_1 * a4) & lower_64_bits_mask) + ((result_b_1 * a4) >> 64)) % modulus
    result_b_1 = (((result_b_1 * b4) & lower_64_bits_mask) + ((result_b_1 * b4) >> 64)) % modulus
    result_b_1 = (((result_b_1 * c4) & lower_64_bits_mask) + ((result_b_1 * c4) >> 64)) % modulus
    result_b_1 = (((result_b_1 * d4) & lower_64_bits_mask) + ((result_b_1 * d4) >> 64)) % modulus
    result_b_1 = (((result_b_1 * a2) & lower_64_bits_mask) + ((result_b_1 * a2) >> 64)) % modulus

    result_b_2 = (((b1 * a3) & lower_64_bits_mask) + ((b1 * a3) >> 64)) % modulus
    result_b_2 = (((result_b_2 * b3) & lower_64_bits_mask) + ((result_b_2 * b3) >> 64)) % modulus
    result_b_2 = (((result_b_2 * c3) & lower_64_bits_mask) + ((result_b_2 * c3) >> 64)) % modulus
    result_b_2 = (((result_b_2 * d3) & lower_64_bits_mask) + ((result_b_2 * d3) >> 64)) % modulus
    result_b_2 = (((result_b_2 * a4) & lower_64_bits_mask) + ((result_b_2 * a4) >> 64)) % modulus
    result_b_2 = (((result_b_2 * b4) & lower_64_bits_mask) + ((result_b_2 * b4) >> 64)) % modulus
    result_b_2 = (((result_b_2 * c4) & lower_64_bits_mask) + ((result_b_2 * c4) >> 64)) % modulus
    result_b_2 = (((result_b_2 * d4) & lower_64_bits_mask) + ((result_b_2 * d4) >> 64)) % modulus
    result_b_2 = (((result_b_2 * b2) & lower_64_bits_mask) + ((result_b_2 * b2) >> 64)) % modulus
    
    result_b_3 = (((b1 * a3) & lower_64_bits_mask) + ((b1 * a3) >> 64)) % modulus
    result_b_3 = (((result_b_3 * b3) & lower_64_bits_mask) + ((result_b_3 * b3) >> 64)) % modulus
    result_b_3 = (((result_b_3 * c3) & lower_64_bits_mask) + ((result_b_3 * c3) >> 64)) % modulus
    result_b_3 = (((result_b_3 * d3) & lower_64_bits_mask) + ((result_b_3 * d3) >> 64)) % modulus
    result_b_3 = (((result_b_3 * a4) & lower_64_bits_mask) + ((result_b_3 * a4) >> 64)) % modulus
    result_b_3 = (((result_b_3 * b4) & lower_64_bits_mask) + ((result_b_3 * b4) >> 64)) % modulus
    result_b_3 = (((result_b_3 * c4) & lower_64_bits_mask) + ((result_b_3 * c4) >> 64)) % modulus
    result_b_3 = (((result_b_3 * d4) & lower_64_bits_mask) + ((result_b_3 * d4) >> 64)) % modulus
    result_b_3 = (((result_b_3 * c2) & lower_64_bits_mask) + ((result_b_3 * c2) >> 64)) % modulus

    result_b_4 = (((b1 * a3) & lower_64_bits_mask) + ((b1 * a3) >> 64)) % modulus
    result_b_4 = (((result_b_4 * b3) & lower_64_bits_mask) + ((result_b_4 * b3) >> 64)) % modulus
    result_b_4 = (((result_b_4 * c3) & lower_64_bits_mask) + ((result_b_4 * c3) >> 64)) % modulus
    result_b_4 = (((result_b_4 * d3) & lower_64_bits_mask) + ((result_b_4 * d3) >> 64)) % modulus
    result_b_4 = (((result_b_4 * a4) & lower_64_bits_mask) + ((result_b_4 * a4) >> 64)) % modulus
    result_b_4 = (((result_b_4 * b4) & lower_64_bits_mask) + ((result_b_4 * b4) >> 64)) % modulus
    result_b_4 = (((result_b_4 * c4) & lower_64_bits_mask) + ((result_b_4 * c4) >> 64)) % modulus
    result_b_4 = (((result_b_4 * d4) & lower_64_bits_mask) + ((result_b_4 * d4) >> 64)) % modulus
    result_b_4 = (((result_b_4 * d2) & lower_64_bits_mask) + ((result_b_4 * d2) >> 64)) % modulus

    #операції для частини c
    #result_c_1 = c1 * a3 * b3 * c3 * d3 * a4 * b4 * c4 * d4 * a2
    #result_c_2 = c1 * a3 * b3 * c3 * d3 * a4 * b4 * c4 * d4 * b2
    #result_c_3 = c1 * a3 * b3 * c3 * d3 * a4 * b4 * c4 * d4 * c2
    #result_c_4 = c1 * a3 * b3 * c3 * d3 * a4 * b4 * c4 * d4 * d2


    result_c_1 = (((c1 * a3) & lower_64_bits_mask) + ((c1 * a3) >> 64)) % modulus
    result_c_1 = (((result_c_1 * b3) & lower_64_bits_mask) + ((result_c_1 * b3) >> 64)) % modulus
    result_c_1 = (((result_c_1 * c3) & lower_64_bits_mask) + ((result_c_1 * c3) >> 64)) % modulus
    result_c_1 = (((result_c_1 * d3) & lower_64_bits_mask) + ((result_c_1 * d3) >> 64)) % modulus
    result_c_1 = (((result_c_1 * a4) & lower_64_bits_mask) + ((result_c_1 * a4) >> 64)) % modulus
    result_c_1 = (((result_c_1 * b4) & lower_64_bits_mask) + ((result_c_1 * b4) >> 64)) % modulus
    result_c_1 = (((result_c_1 * c4) & lower_64_bits_mask) + ((result_c_1 * c4) >> 64)) % modulus
    result_c_1 = (((result_c_1 * d4) & lower_64_bits_mask) + ((result_c_1 * d4) >> 64)) % modulus
    result_c_1 = (((result_c_1 * a2) & lower_64_bits_mask) + ((result_c_1 * a2) >> 64)) % modulus

    result_c_2 = (((c1 * a3) & lower_64_bits_mask) + ((c1 * a3) >> 64)) % modulus
    result_c_2 = (((result_c_2 * b3) & lower_64_bits_mask) + ((result_c_2 * b3) >> 64)) % modulus
    result_c_2 = (((result_c_2 * c3) & lower_64_bits_mask) + ((result_c_2 * c3) >> 64)) % modulus
    result_c_2 = (((result_c_2 * d3) & lower_64_bits_mask) + ((result_c_2 * d3) >> 64)) % modulus
    result_c_2 = (((result_c_2 * a4) & lower_64_bits_mask) + ((result_c_2 * a4) >> 64)) % modulus
    result_c_2 = (((result_c_2 * b4) & lower_64_bits_mask) + ((result_c_2 * b4) >> 64)) % modulus
    result_c_2 = (((result_c_2 * c4) & lower_64_bits_mask) + ((result_c_2 * c4) >> 64)) % modulus
    result_c_2 = (((result_c_2 * d4) & lower_64_bits_mask) + ((result_c_2 * d4) >> 64)) % modulus
    result_c_2 = (((result_c_2 * b2) & lower_64_bits_mask) + ((result_c_2 * b2) >> 64)) % modulus
    
    result_c_3 = (((c1 * a3) & lower_64_bits_mask) + ((c1 * a3) >> 64)) % modulus
    result_c_3 = (((result_c_3 * b3) & lower_64_bits_mask) + ((result_c_3 * b3) >> 64)) % modulus
    result_c_3 = (((result_c_3 * c3) & lower_64_bits_mask) + ((result_c_3 * c3) >> 64)) % modulus
    result_c_3 = (((result_c_3 * d3) & lower_64_bits_mask) + ((result_c_3 * d3) >> 64)) % modulus
    result_c_3 = (((result_c_3 * a4) & lower_64_bits_mask) + ((result_c_3 * a4) >> 64)) % modulus
    result_c_3 = (((result_c_3 * b4) & lower_64_bits_mask) + ((result_c_3 * b4) >> 64)) % modulus
    result_c_3 = (((result_c_3 * c4) & lower_64_bits_mask) + ((result_c_3 * c4) >> 64)) % modulus
    result_c_3 = (((result_c_3 * d4) & lower_64_bits_mask) + ((result_c_3 * d4) >> 64)) % modulus
    result_c_3 = (((result_c_3 * c2) & lower_64_bits_mask) + ((result_c_3 * c2) >> 64)) % modulus

    result_c_4 = (((c1 * a3) & lower_64_bits_mask) + ((c1 * a3) >> 64)) % modulus
    result_c_4 = (((result_c_4 * b3) & lower_64_bits_mask) + ((result_c_4 * b3) >> 64)) % modulus
    result_c_4 = (((result_c_4 * c3) & lower_64_bits_mask) + ((result_c_4 * c3) >> 64)) % modulus
    result_c_4 = (((result_c_4 * d3) & lower_64_bits_mask) + ((result_c_4 * d3) >> 64)) % modulus
    result_c_4 = (((result_c_4 * a4) & lower_64_bits_mask) + ((result_c_4 * a4) >> 64)) % modulus
    result_c_4 = (((result_c_4 * b4) & lower_64_bits_mask) + ((result_c_4 * b4) >> 64)) % modulus
    result_c_4 = (((result_c_4 * c4) & lower_64_bits_mask) + ((result_c_4 * c4) >> 64)) % modulus
    result_c_4 = (((result_c_4 * d4) & lower_64_bits_mask) + ((result_c_4 * d4) >> 64)) % modulus
    result_c_4 = (((result_c_4 * d2) & lower_64_bits_mask) + ((result_c_4 * d2) >> 64)) % modulus

    #Операції для частини d
    #result_d_1 = d1 * a3 * b3 * c3 * d3 * a4 * b4 * c4 * d4 * a2
    #result_d_2 = d1 * a3 * b3 * c3 * d3 * a4 * b4 * c4 * d4 * b2
    #result_d_3 = d1 * a3 * b3 * c3 * d3 * a4 * b4 * c4 * d4 * c2
    #result_d_4 = d1 * a3 * b3 * c3 * d3 * a4 * b4 * c4 * d4 * d2

    result_d_1 = (((d1 * a3) & lower_64_bits_mask) + ((d1 * a3) >> 64)) % modulus
    result_d_1 = (((result_d_1 * b3) & lower_64_bits_mask) + ((result_d_1 * b3) >> 64)) % modulus
    result_d_1 = (((result_d_1 * c3) & lower_64_bits_mask) + ((result_d_1 * c3) >> 64)) % modulus
    result_d_1 = (((result_d_1 * d3) & lower_64_bits_mask) + ((result_d_1 * d3) >> 64)) % modulus
    result_d_1 = (((result_d_1 * a4) & lower_64_bits_mask) + ((result_d_1 * a4) >> 64)) % modulus
    result_d_1 = (((result_d_1 * b4) & lower_64_bits_mask) + ((result_d_1 * b4) >> 64)) % modulus
    result_d_1 = (((result_d_1 * c4) & lower_64_bits_mask) + ((result_d_1 * c4) >> 64)) % modulus
    result_d_1 = (((result_d_1 * d4) & lower_64_bits_mask) + ((result_d_1 * d4) >> 64)) % modulus
    result_d_1 = (((result_d_1 * a2) & lower_64_bits_mask) + ((result_d_1 * a2) >> 64)) % modulus

    result_d_2 = (((d1 * a3) & lower_64_bits_mask) + ((d1 * a3) >> 64)) % modulus
    result_d_2 = (((result_d_2 * b3) & lower_64_bits_mask) + ((result_d_2 * b3) >> 64)) % modulus
    result_d_2 = (((result_d_2 * c3) & lower_64_bits_mask) + ((result_d_2 * c3) >> 64)) % modulus
    result_d_2 = (((result_d_2 * d3) & lower_64_bits_mask) + ((result_d_2 * d3) >> 64)) % modulus
    result_d_2 = (((result_d_2 * a4) & lower_64_bits_mask) + ((result_d_2 * a4) >> 64)) % modulus
    result_d_2 = (((result_d_2 * b4) & lower_64_bits_mask) + ((result_d_2 * b4) >> 64)) % modulus
    result_d_2 = (((result_d_2 * c4) & lower_64_bits_mask) + ((result_d_2 * c4) >> 64)) % modulus
    result_d_2 = (((result_d_2 * d4) & lower_64_bits_mask) + ((result_d_2 * d4) >> 64)) % modulus
    result_d_2 = (((result_d_2 * b2) & lower_64_bits_mask) + ((result_d_2 * b2) >> 64)) % modulus
    
    result_d_3 = (((d1 * a3) & lower_64_bits_mask) + ((d1 * a3) >> 64)) % modulus
    result_d_3 = (((result_d_3 * b3) & lower_64_bits_mask) + ((result_d_3 * b3) >> 64)) % modulus
    result_d_3 = (((result_d_3 * c3) & lower_64_bits_mask) + ((result_d_3 * c3) >> 64)) % modulus
    result_d_3 = (((result_d_3 * d3) & lower_64_bits_mask) + ((result_d_3 * d3) >> 64)) % modulus
    result_d_3 = (((result_d_3 * a4) & lower_64_bits_mask) + ((result_d_3 * a4) >> 64)) % modulus
    result_d_3 = (((result_d_3 * b4) & lower_64_bits_mask) + ((result_d_3 * b4) >> 64)) % modulus
    result_d_3 = (((result_d_3 * c4) & lower_64_bits_mask) + ((result_d_3 * c4) >> 64)) % modulus
    result_d_3 = (((result_d_3 * d4) & lower_64_bits_mask) + ((result_d_3 * d4) >> 64)) % modulus
    result_d_3 = (((result_d_3 * c2) & lower_64_bits_mask) + ((result_d_3 * c2) >> 64)) % modulus

    result_d_4 = (((d1 * a3) & lower_64_bits_mask) + ((d1 * a3) >> 64)) % modulus
    result_d_4 = (((result_d_4 * b3) & lower_64_bits_mask) + ((result_d_4 * b3) >> 64)) % modulus
    result_d_4 = (((result_d_4 * c3) & lower_64_bits_mask) + ((result_d_4 * c3) >> 64)) % modulus
    result_d_4 = (((result_d_4 * d3) & lower_64_bits_mask) + ((result_d_4 * d3) >> 64)) % modulus
    result_d_4 = (((result_d_4 * a4) & lower_64_bits_mask) + ((result_d_4 * a4) >> 64)) % modulus
    result_d_4 = (((result_d_4 * b4) & lower_64_bits_mask) + ((result_d_4 * b4) >> 64)) % modulus
    result_d_4 = (((result_d_4 * c4) & lower_64_bits_mask) + ((result_d_4 * c4) >> 64)) % modulus
    result_d_4 = (((result_d_4 * d4) & lower_64_bits_mask) + ((result_d_4 * d4) >> 64)) % modulus
    result_d_4 = (((result_d_4 * d2) & lower_64_bits_mask) + ((result_d_4 * d2) >> 64)) % modulus

    

    results.append((result_a_1,result_a_2,result_a_3,result_a_4,result_b_1,result_b_2,result_b_3,result_b_4,result_c_1,result_c_2,result_c_3,result_c_4,result_d_1,result_d_2,result_d_3,result_d_4))

    final = sum_quaternion_parts_with_modulus(results)

    return final


def sum_quaternion_parts_with_modulus(parts, modulus=2**64):
    result = []
    tmp = []
    #print(parts)
    for i in range(4):
        test = parts[0][i::4]
        #print(test)
        tmp.append(sum_with_modulus(test))
    result.append(Quaternion(*tmp))
    return result

def sum_with_modulus(values, modulus=2**64):
    result = 0
    for value in values:
        result = (result + value) % modulus
    return result
   

handlers = {
    2: multiply_quaternions,
    4: perform_operations
}



# If we
# result = handlers[len(quaternions)()]

# if len(2):
    # result = handlers[2]()


