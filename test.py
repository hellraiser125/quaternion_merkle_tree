import threading
from typing import List
import concurrent.futures
from quaternion_processor import Quaternion

 
def perform_operations_chunk(quaternions, start_idx, end_idx):
    """
    Виконує операції над частиною кватерніонів.
 
    Аргументи:
        quaternions (list): Список об'єктів Quaternion.
        start_idx (int): Початковий індекс частини.
        end_idx (int): Кінцевий індекс частини.
 
    Повертає:
        list: Список результатів операцій.
    """
    results = []
    lower_64_bits_mask = (1 << 64) - 1
    modulus = 2**64
 
    def calc_result(q1, q2, q3, q4):
        result = {}
        lock = threading.Lock()  # Створення блокування для синхронізації доступу до result
 
        def calc_a():
            nonlocal result
            result_a = (((q1.a * q3.a) & lower_64_bits_mask) + ((q1.a * q3.a) >> 64)) % modulus
            result_a = (((result_a * q3.b) & lower_64_bits_mask) + ((result_a * q3.b) >> 64)) % modulus
            result_a = (((result_a * q3.c) & lower_64_bits_mask) + ((result_a * q3.c) >> 64)) % modulus
            result_a = (((result_a * q3.d) & lower_64_bits_mask) + ((result_a * q3.d) >> 64)) % modulus
            result_a = (((result_a * q4.a) & lower_64_bits_mask) + ((result_a * q4.a) >> 64)) % modulus
            result_a = (((result_a * q4.b) & lower_64_bits_mask) + ((result_a * q4.b) >> 64)) % modulus
            result_a = (((result_a * q4.c) & lower_64_bits_mask) + ((result_a * q4.c) >> 64)) % modulus
            result_a = (((result_a * q4.d) & lower_64_bits_mask) + ((result_a * q4.d) >> 64)) % modulus
            result_a = (((result_a * q2.a) & lower_64_bits_mask) + ((result_a * q2.a) >> 64)) % modulus
            with lock:  # Використання блокування для запису у словник
                result['a'] = result_a
 
        def calc_b():
            nonlocal result
            result_b = (((q1.b * q3.a) & lower_64_bits_mask) + ((q1.b * q3.a) >> 64)) % modulus
            result_b = (((result_b * q3.b) & lower_64_bits_mask) + ((result_b * q3.b) >> 64)) % modulus
            result_b = (((result_b * q3.c) & lower_64_bits_mask) + ((result_b * q3.c) >> 64)) % modulus
            result_b = (((result_b * q3.d) & lower_64_bits_mask) + ((result_b * q3.d) >> 64)) % modulus
            result_b = (((result_b * q4.a) & lower_64_bits_mask) + ((result_b * q4.a) >> 64)) % modulus
            result_b = (((result_b * q4.b) & lower_64_bits_mask) + ((result_b * q4.b) >> 64)) % modulus
            result_b = (((result_b * q4.c) & lower_64_bits_mask) + ((result_b * q4.c) >> 64)) % modulus
            result_b = (((result_b * q4.d) & lower_64_bits_mask) + ((result_b * q4.d) >> 64)) % modulus
            result_b = (((result_b * q2.b) & lower_64_bits_mask) + ((result_b * q2.b) >> 64)) % modulus
            with lock:  # Використання блокування для запису у словник
                result['b'] = result_b
 
        def calc_c():
            nonlocal result
            result_c = (((q1.c * q3.a) & lower_64_bits_mask) + ((q1.c * q3.a) >> 64)) % modulus
            result_c = (((result_c * q3.b) & lower_64_bits_mask) + ((result_c * q3.b) >> 64)) % modulus
            result_c = (((result_c * q3.c) & lower_64_bits_mask) + ((result_c * q3.c) >> 64)) % modulus
            result_c = (((result_c * q3.d) & lower_64_bits_mask) + ((result_c * q3.d) >> 64)) % modulus
            result_c = (((result_c * q4.a) & lower_64_bits_mask) + ((result_c * q4.a) >> 64)) % modulus
            result_c = (((result_c * q4.b) & lower_64_bits_mask) + ((result_c * q4.b) >> 64)) % modulus
            result_c = (((result_c * q4.c) & lower_64_bits_mask) + ((result_c * q4.c) >> 64)) % modulus
            result_c = (((result_c * q4.d) & lower_64_bits_mask) + ((result_c * q4.d) >> 64)) % modulus
            result_c = (((result_c * q2.c) & lower_64_bits_mask) + ((result_c * q2.c) >> 64)) % modulus
            with lock:  # Використання блокування для запису у словник
                result['c'] = result_c
 
        def calc_d():
            nonlocal result
            result_d = (((q1.d * q3.a) & lower_64_bits_mask) + ((q1.d * q3.a) >> 64)) % modulus
            result_d = (((result_d * q3.b) & lower_64_bits_mask) + ((result_d * q3.b) >> 64)) % modulus
            result_d = (((result_d * q3.c) & lower_64_bits_mask) + ((result_d * q3.c) >> 64)) % modulus
            result_d = (((result_d * q3.d) & lower_64_bits_mask) + ((result_d * q3.d) >> 64)) % modulus
            result_d = (((result_d * q4.a) & lower_64_bits_mask) + ((result_d * q4.a) >> 64)) % modulus
            result_d = (((result_d * q4.b) & lower_64_bits_mask) + ((result_d * q4.b) >> 64)) % modulus
            result_d = (((result_d * q4.c) & lower_64_bits_mask) + ((result_d * q4.c) >> 64)) % modulus
            result_d = (((result_d * q4.d) & lower_64_bits_mask) + ((result_d * q4.d) >> 64)) % modulus
            result_d = (((result_d * q2.d) & lower_64_bits_mask) + ((result_d * q2.d) >> 64)) % modulus
            with lock:  # Використання блокування для запису у словник
                result['d'] = result_d
 
        threads = []
        for func in [calc_a, calc_b, calc_c, calc_d]:
            thread = threading.Thread(target=func)
            thread.start()
            threads.append(thread)
 
        for thread in threads:
            thread.join()
 
        return (result['a'], result['b'], result['c'], result['d'])
 
    for i in range(start_idx, end_idx):
        for j in range(i + 1, len(quaternions)):
            result = calc_result(quaternions[j - 3], quaternions[j - 2], quaternions[j - 1], quaternions[i])
            results.append(result)
 
    return results
 
 
def perform_operations(quaternions, num_threads: int = 4):
    """
    Виконує серію операцій над списком кватерніонів з використанням багатопоточності.
 
    Аргументи:
        quaternions (list): Список кватерніонів. Кожен кватерніон повинен мати атрибути a, b, c та d.
        num_threads (int, optional): Кількість потоків для паралельної обробки. За замовчуванням 4.
 
    Повертає:
        list: Список, що містить кінцеві результати виконаних операцій.
    """
    chunk_size = len(quaternions) // num_threads
    futures = []
 
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        for i in range(num_threads):
            start_idx = i * chunk_size
            end_idx = (i + 1) * chunk_size if i < num_threads - 1 else len(quaternions)
            futures.append(executor.submit(perform_operations_chunk, quaternions, start_idx, end_idx))
 
    results = []
    for future in concurrent.futures.as_completed(futures):
        results.extend(future.result())
 
    final_result = sum_quaternion_parts_with_modulus(results)
    print(*final_result)
 
    return final_result
 
 
def sum_quaternion_parts_with_modulus(parts, modulus=2**64):
    """
    Підсумовує частини кватерніонів з використанням заданого модуля та повертає результат як кватерніон.
 
    Ця функція приймає список частин кватерніонів, підсумовує кожну відповідну частину з використанням модульної арифметики
    та будує кватерніон з результатів.
 
    Аргументи:
        parts (list): Список, що містить частини кватерніонів. Кожен елемент у списку представляє конкретну частину 
                      (a, b, c або d) декількох кватерніонів.
        modulus (int, optional): Модуль для підсумовування. За замовчуванням 2**64.
 
    Повертає:
        list: Список, що містить один кватерніон, який є сумою вхідних частин за модулем.
    """
    result = []
    tmp = []
    for i in range(4):
        test = parts[0][i::4]
        tmp.append(sum_with_modulus(test))
    result.append(Quaternion(*tmp))
    return result
 
 
def sum_with_modulus(values, modulus=2**64):
    result = 0
    for value in values:
        result = (result + value) % modulus
    return result
 
# Приклад використання:

 