from quaternion_processor import QuaternionProcessor, multiply_quaternions, perform_operations
import struct





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

def reduce_data(data):
    #breakpoint()
    while len(data) > 1:
        if len(data) >= 4:
            reduced = []
            i = 0
            while i <= len(data) - 4:
                reduced.append(perform_operations(data[i:i+4]))
                i += 4
            # Додаємо залишок елементів, які не змогли згорнутися на цьому рівні
            data = reduced + data[i:]
        elif len(data) >= 2:
            reduced = []
            i = 0
            while i <= len(data) - 2:
                reduced.append(multiply_quaternions(data[i:i+2]))
                i += 2
            # Додаємо залишок елементів, які не змогли згорнутися на цьому рівні
            data = reduced + data[i:]
        else:
            break  # Якщо залишився лише один елемент, то зупиняємося
    return data[0][0]

def main():
    """
    Main entry point of the program.
    """
    file_path = 'test_str.txt'  # Replace with your file path
    data = read_chunks_from_file(file_path)
    # processor = QuaternionProcessor(data)
    # quaternions = processor.make_quaternion()
    # for data in quaternions:
    #     print(data)
    # print("--------------------------------------------------")
    # print("Quaternions After Multiplication")
    # print("--------------------------------------------------")
    
    processor = QuaternionProcessor(data)
    quaternions = processor.make_quaternion()
    for data in quaternions:
        print(f"Data ---> {data}")
    res = multiply_quaternions(quaternions)
    
    results = reduce_data(res)

    print(results)



    # operation_results = perform_operations(multiply_results)
    # # Виведення результатів операцій
    # for result in operation_results:
    #     print(f"Results after completed operations:")
    #     print(f"a1: {result[0]}")
    #     print(f"b1: {result[1]}")
    #     print(f"c1: {result[2]}")
    #     print(f"d1: {result[3]}")
    #     print("-----------------------")
    #     print(f"a2: {result[4]}")
    #     print(f"b2: {result[5]}")
    #     print(f"c2: {result[6]}")
    #     print(f"d2: {result[7]}")
    #     print("-----------------------")
    #     print(f"a3: {result[8]}")
    #     print(f"b3: {result[9]}")
    #     print(f"c3: {result[10]}")
    #     print(f"d3: {result[11]}")
    #     print("-----------------------")
    #     print(f"a4: {result[12]}")
    #     print(f"b4: {result[13]}")
    #     print(f"c4: {result[14]}")
    #     print(f"d4: {result[15]}")
    #     print("-----------------------")
    # data = sum_quaternion_parts_with_modulus(operation_results)
    # for q in data:
    #     print(f"Parts of new q  --> {q}\n")

    # processor = QuaternionProcessor(data)
    # new_q = processor.make_quaternion()
    # print (f"New quaternion from 16 results ---> {new_q}")
    


if __name__ == '__main__':
    main()
