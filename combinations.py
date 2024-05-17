# import struct

# class QuaternionProcessor:
#     def __init__(self, file_path):
#         self.chunk_data = self.read_chunks_from_file(file_path)

#     @staticmethod
#     def read_chunks_from_file(file_path):
#         """ Reads a file in chunks of 8 bytes and returns a dictionary with chunk numbers as keys and decimal values as values. If the chunk size is less than 8 bytes, the missing elements are padded with zeros. """
#         chunk_dict = {}
#         chunk_number = 1
#         with open(file_path, 'rb') as file:  # Open in binary mode for byte reading
#             while True:
#                 chunk = file.read(8)  # Read 8 bytes
#                 if not chunk:
#                     break  # Exit if no more data to read
#                 if len(chunk) < 8:
#                     chunk += b'\0' * (8 - len(chunk))  # Pad missing elements with zeros
#                 decimal_values = list(struct.unpack('B' * len(chunk), chunk))
#                 chunk_dict[chunk_number] = decimal_values
#                 chunk_number += 1
#         return chunk_dict

#     def make_quaternion(self) -> list:
#         """ Process chunk data and calculate quaternion values.
#         Returns:
#             list: A list of quaternion parts (a, b, c, d)
#         """
#         quaternion_parts = []
#         quaternions = []
#         for decimal_values in self.chunk_data.values():
#             quaternion = 0
#             for index, data in enumerate(decimal_values, start=0):
#                 if data == 0:
#                     quaternion += data
#                 else:
#                     quaternion += data << 8 * index  # Use bitwise shift instead of pow
#                 print(f"Quaternion part noW --->  {quaternion}")
#             quaternion_parts.append(quaternion)
#             print(f"Created part --->  {quaternion}")
#             if len(quaternion_parts) == 4:
#                 quaternions.append(Quaternion(*quaternion_parts))
#                 quaternion_parts.clear()
#         return quaternions

    
# class Quaternion:
#     def __init__(self, a, b, c, d):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d

#     def __str__(self):
#         return f"{self.a} + ({self.b})i + ({self.c})j + ({self.d})k"

#     def __mul__(self, other):
#         a1, b1, c1, d1 = self.a, self.b, self.c, self.d
#         a2, b2, c2, d2 = other.a, other.b, other.c, other.d
#         modulus = 2**4


#         # Виділення молодших та старших частин для кожної операції множення
#         lower_64_bits_mask = (1 << 4) - 1
#         print(f"Lower bit mask ----> {lower_64_bits_mask}")
#         # Для операції частини а
#         a1a2_lower = (a1 * a2) & lower_64_bits_mask
#         print(f"Lower a1a2--> {a1a2_lower}")
#         a1a2_higher = (a1 * a2) >> 4
#         print(f"Higher a1a2--> {a1a2_higher}")
#         b1b2_lower = (b1 * b2) & lower_64_bits_mask
#         print(f"lower b1b2 --> {b1b2_lower}")
#         b1b2_higher = (b1 * b2) >> 4
#         print(f"Higher --> {b1b2_higher}")
#         c1c2_lower = (c1 * c2) & lower_64_bits_mask
#         c1c2_higher = (c1 * c2) >> 4
#         d1d2_lower = (d1 * d2) & lower_64_bits_mask
#         d1d2_higher = (d1 * d2) >> 4

#         #Отримання результату множення для частини a
#         a1a2_product = (a1a2_lower + a1a2_higher) % modulus
#         print(f"Producrt a1a2_product--> {a1a2_product}")
#         b1b2_product = (b1b2_lower + b1b2_higher) % modulus
#         print(f"Producrt  b1b2_product--> {b1b2_product}")
#         c1c2_product = (c1c2_lower + c1c2_higher) % modulus
#         print(f"Producrt c1c2_product--> {c1c2_product}")
#         d1d2_product = (d1d2_lower + d1d2_higher) % modulus
#         print(f"Producrt d1d2_product--> {d1d2_product}")

#         # Для операції частини b
#         a1b2_lower = (a1 * b2) & lower_64_bits_mask
#         a1b2_higher = (a1 * b2) >> 4
#         b1a2_lower = (b1 * a2) & lower_64_bits_mask
#         b1a2_higher = (b1 * a2) >> 4
#         c1d2_lower = (c1 * d2) & lower_64_bits_mask
#         c1d2_higher = (c1 * d2) >> 4
#         d1c2_lower = (d1 * c2) & lower_64_bits_mask
#         d1c2_higher = (d1 * c2) >> 4

#         #Отримання результату множення для частини b
#         a1b2_product = (a1b2_lower + a1b2_higher) % modulus
#         b1a2_product = (b1a2_lower + b1a2_higher) % modulus
#         c1d2_product = (c1d2_lower + c1d2_higher) % modulus
#         d1c2_product = (d1c2_lower + d1c2_higher) % modulus 
#         #print(f"Producrt a1b2_product--> {a1b2_product}")
#         #print(f"Producrt b1a2_product--> {b1a2_product}")
#         #print(f"Producrt c1d2_product--> {c1d2_product}")
#         #print(f"Producrt d1c2_product--> {d1c2_product}")

#         # Для операції частини c
#         a1c2_lower = (a1 * c2) & lower_64_bits_mask
#         a1c2_higher = (a1 * c2) >> 4
#         c1a2_lower = (c1 * a2) & lower_64_bits_mask
#         c1a2_higher = (c1 * a2) >> 4
#         d1b2_lower = (d1 * b2) & lower_64_bits_mask
#         d1b2_higher = (d1 * b2) >> 4
#         b1d2_lower = (b1 * d2) & lower_64_bits_mask
#         b1d2_higher = (b1 * d2) >> 4

#         #Отримання результату множення для частини c
#         a1c2_product = (a1c2_lower + a1c2_higher) % modulus
#         c1a2_product = (c1a2_lower + c1a2_higher) % modulus
#         d1b2_product = (d1b2_lower + d1b2_higher) % modulus
#         b1d2_product = (b1d2_lower + b1d2_higher) % modulus

#         # Для операції частини d
#         a1d2_lower = (a1 * d2) & lower_64_bits_mask
#         a1d2_higher = (a1 * d2) >> 4
#         d1a2_lower = (d1 * a2) & lower_64_bits_mask
#         d1a2_higher = (d1 * a2) >> 4
#         b1c2_lower = (b1 * c2) & lower_64_bits_mask
#         b1c2_higher = (b1 * c2) >> 4
#         c1b2_lower = (c1 * b2) & lower_64_bits_mask
#         c1b2_higher = (c1 * b2) >> 4

#         #Отримання результату множення для частини d
#         a1d2_product = (a1d2_lower + a1d2_higher) % modulus
#         d1a2_product = (d1a2_lower + d1a2_higher) % modulus
#         b1c2_product = (b1c2_lower + b1c2_higher) % modulus
#         c1b2_product = (c1b2_lower + c1b2_higher) % modulus

#         # Обчислення компонентів з виконанням операцій за модулем 2^64
#         #a = ((a1a2_product - b1b2_product) % modulus - c1c2_product % modulus - d1d2_product % modulus) % modulus
#         #b = ((a1b2_product + b1a2_product) % modulus + c1d2_product % modulus - d1c2_product % modulus) % modulus
#         #c = ((a1c2_product + c1a2_product) % modulus + d1b2_product % modulus - b1d2_product % modulus) % modulus
#         #d = ((a1d2_product + d1a2_product) % modulus + b1c2_product % modulus - c1b2_product % modulus) % modulus

#         a_temp = (((a1a2_product - b1b2_product) - c1c2_product) - d1d2_product)
#         print(f"A_temp ----> {a_temp}")
#         print(f"(a_temp [{a_temp}]  + modulus [{modulus}]) % modulus [{modulus}] ---> {(a_temp + modulus) % modulus}")
#         a = (a_temp + modulus) % modulus if a_temp < 0 else a_temp & lower_64_bits_mask

#         b_temp = ((a1b2_product + b1a2_product) % modulus + c1d2_product % modulus - d1c2_product % modulus) % modulus
#         b = (b_temp + modulus) % modulus if b_temp < 0 else b_temp & lower_64_bits_mask

#         c_temp = ((a1c2_product + c1a2_product) % modulus + d1b2_product % modulus - b1d2_product % modulus) % modulus
#         c = (c_temp + modulus) % modulus if c_temp < 0 else c_temp & lower_64_bits_mask

#         d_temp = ((a1d2_product + d1a2_product) % modulus + b1c2_product % modulus - c1b2_product % modulus) % modulus
#         d = (d_temp + modulus) % modulus if d_temp < 0 else d_temp & lower_64_bits_mask

#         return Quaternion(a,b,c,d)

# def multiply_quaternions(quaternions):
#     result = quaternions[0] * quaternions[1]
#     print(f"After multiplying quaternion 1 and 2: {result}")

#     for quaternion in quaternions[2:]:
#         result = result * quaternion
#         print(f"After multiplying with next quaternion: {result}")

#     return result

# #a1 2, b1 3, c1 5, d1 8
# #a2 3, b2 7, c2 11, d2 13
# #res 8 15 9 2

# def main():
#     """
#     Main entry point of the program.
#     """
#     file_path = 'test_str.txt'  # Replace with your file path
#     #processor = QuaternionProcessor(file_path)
#     quaternions = [
#     Quaternion(2, 3, 5, 8),
#     Quaternion(3, 7, 11, 13),
#     ]
#     #quaternions = processor.make_quaternion()
#     for data in quaternions:
#         print(data)
#     print("--------------------------------------------------")
#     print("Quaternion Multiplication")
#     print("--------------------------------------------------")
#     multiply_quaternions(quaternions)


#     #quaternion_multiply(chunk_data)


# if __name__ == '__main__':
#     main()

import itertools

# Основи та індекси
bases = ['a', 'b', 'c', 'd']
indices = [1, 2, 3, 4]

# Генеруємо всі можливі комбінації індексів
def generate_combinations(bases, indices):
    unique_combinations = set()
    # Для кожної довжини від 4 до 4 (або більше, якщо потрібно)
    for r in range(4, len(bases) + 1):
        # Генеруємо всі можливі комбінації основ з повторами
        for elements in itertools.product(bases, repeat=r):
            # Генеруємо всі можливі перестановки індексів для даної довжини
            for perm in itertools.permutations(indices, r):
                # Створюємо добуток з комбінації основ та перестановки індексів
                combination = tuple(sorted([f"{elements[i]}{perm[i]}" for i in range(r)]))
                unique_combinations.add(combination)
    return unique_combinations

# Отримуємо всі можливі унікальні комбінації
combinations = generate_combinations(bases, indices)

# Записуємо всі комбінації у файл
with open('combinations.txt', 'w') as file:
    for comb in combinations:
        file.write(" * ".join(comb) + '\n')

print("Комбінації успішно записані у файл combinations.txt")


def read_combinations(file_path):
    with open(file_path, 'r') as file:
        combinations = [line.strip() for line in file]
    return combinations

def combine_combinations(combinations, target_count):
    combined_combinations = []
    step = len(combinations) // target_count
    for i in range(0, len(combinations), step):
        combined_combinations.append(' * '.join(combinations[i:i + step]))
    return combined_combinations

def filter_combinations(combinations):
    filtered_combinations = []
    for comb in combinations:
        indices = set()
        valid_comb = True
        for item in comb.split(' * '):
            index = int(item[1:])
            if index in indices:
                valid_comb = False
                break
            else:
                indices.add(index)
        if valid_comb:
            filtered_combinations.append(comb)
    return filtered_combinations

# Читаємо комбінації з файлу
combinations = read_combinations('combinations.txt')

# Фільтруємо комбінації, щоб у кожному об'єднаному множенні не було значень з однаковим індексом
filtered_combinations = filter_combinations(combinations)

# Об'єднуємо комбінації в 16 груп
target_count = 16
combined_combinations = combine_combinations(filtered_combinations, target_count)

# Записуємо об'єднані комбінації у новий файл
with open('filtered_combined_combinations.txt', 'w') as file:
    for comb in combined_combinations:
        file.write(comb + '\n')

print("Об'єднані комбінації з фільтрацією успішно записані у файл filtered_combined_combinations.txt")





