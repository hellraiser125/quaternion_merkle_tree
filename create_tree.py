from quaternion_processor import QuaternionProcessor, multiply_quaternions, perform_operations, convolution_three_elements
#from test import perform_operations
import struct





def read_chunks_from_file(file_path):
    """
    Reads a file in chunks of 8 bytes and returns a dictionary with chunk numbers as keys 
    and decimal values as values. If the chunk size is less than 8 bytes, the missing elements 
    are padded with zeros.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        dict: A dictionary where keys represent chunk numbers and values represent lists of decimal values.
              Each list contains decimal values extracted from a chunk of 8 bytes.
    """
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
    #breakpoint()
    return chunk_dict

def reduce_data(data):
    """
    Reduces a list of quaternions by performing operations on chunks of quaternions iteratively until only one quaternion remains.

    Args:
        data (list): A list of quaternions.

    Returns:
        Quaternion: The final reduced quaternion obtained after performing operations on the input data.
    """

    while len(data) > 1:
        new_data = []
        i = 0
        while i < len(data):
            if i + 4 <= len(data):
                print("\nStart performing operations to 4 Quaternions\n")
                new_data.append(*perform_operations(data[i:i + 4]))
                i += 4
            elif i + 3 <= len(data):
                print("\nStart performing operations to 3 Quaternions\n")
                new_data.append(*convolution_three_elements(data[i:i + 3]))
                i += 3
            elif i + 2 <= len(data):
                print("\nStart performing operations to 2 Quaternions\n")
                new_data.append(*multiply_quaternions(data[i:i + 2]))
                i += 2
            else:
                new_data.append(data[i])
                i += 1
        data = new_data

    for final in data:
        print(f"\nFinal state of data: {final}")  # Print the final state of data
    return data[0]



# def reduce_data(data):
#     """
#     Reduces a list of quaternions by performing operations on chunks of quaternions iteratively until only one quaternion remains.

#     Args:
#         data (list): A list of quaternions.

#     Returns:
#         Quaternion: The final reduced quaternion obtained after performing operations on the input data.
#     """
#     while len(data) > 1:
#         new_data = []
#         i = 0
#         while i < len(data):
#             if i + 4 <= len(data):
#                 print("\nStart performing operations to 4 Quaternions\n")
#                 new_data.append(*perform_operations(data[i:i + 4]))
#                 i += 4
#             elif i + 3 <= len(data):
#                 print("\nStart performing operations to 3 Quaternions\n")
#                 new_data.append(*convolution_three_elements(data[i:i + 3]))
#                 i += 3
#             elif i + 2 <= len(data):
#                 print("\nStart performing operations to 2 Quaternions\n")
#                 new_data.append(*multiply_quaternions(data[i:i + 2]))
#                 i += 2
#             else:
#                 new_data.append(data[i])
#                 i += 1
#         data = new_data

#     for final in data:
#         print(f"\nFinal state of data: {final}")  # Print the final state of data
#     return data[0]




def main():
    """
    Main entry point of the program.
    """
    file_path = 'test_str.txt'  
    data = read_chunks_from_file(file_path)
    processor = QuaternionProcessor(data)
    quaternions = processor.make_quaternion()
    print(len(quaternions))
    res = multiply_quaternions(quaternions)   
    results = reduce_data(res)



if __name__ == '__main__':
    main()
