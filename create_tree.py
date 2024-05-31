from quaternion_processor import QuaternionProcessor, multiply_quaternions, perform_operations, convolution_three_elements
#from test import perform_operations
import struct,math




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
    print("\nPerforming operations\n")
    tree = []
    tree.append(data)
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
        tree.append(data)
   
    
    print(f"\nFinal state of data: {tree[2][0]}\n")  # Print the final state of data
    return tree


class Proof:
    def __init__(self, data, checked_transaction):
        self.tree = data
        self.checked_transaction = checked_transaction

    def number_of_elements(self):
        """
        Determines the number of elements in the list.
        """
        return len(self.tree[0])

    def complete_sets_of_4(self):
        """
        Determines the complete sets of 4 elements in the list.
        """
        return len(self.tree[0]) // 4

    def height_of_tree(self):
        """
        Determines the height of a tree.
        """
        log4_N = math.log(self.number_of_elements()) / math.log(4)  # log4(N)
        high = math.ceil(log4_N)
        return high
    

    def get_num_elements_for_next_level(self,curent_level, next_level_element):
        
        nums_of_elements_on_curent_level = len(self.tree[curent_level-1])
        full_four_sets_on_curent_level = nums_of_elements_on_curent_level // 4
        if next_level_element+1 <= full_four_sets_on_curent_level:
            return 4
        elif nums_of_elements_on_curent_level % 4 == 2:
            return 2
        elif nums_of_elements_on_curent_level % 4 == 3:
            return 3
        return 1
       

    def proof_transaction(self):
        curent_level = 1
        if self.checked_transaction == 0 or self.checked_transaction > self.number_of_elements():
                print("Checked transaction not a part of tree")
                return
        while curent_level != self.height_of_tree() + 1:
            print(f"\nChecked transaction ----> {self.checked_transaction}\n") 
            part_of_next_transaction = (self.checked_transaction // 4)
            print(f"Checked transaction part of --> {part_of_next_transaction}")
            max_k = self.get_num_elements_for_next_level(curent_level,part_of_next_transaction)
            print(f"Element on level {curent_level} with index {part_of_next_transaction} was created by {max_k} elements.")
            checked_tree = []
            k = 1
            for k in range(max_k):
                start_transaction = (part_of_next_transaction) * 4 + k
                print(f"Transaction {part_of_next_transaction} contain {self.tree[curent_level-1][start_transaction]}")
                checked_tree.append(self.tree[curent_level-1][start_transaction])
            for data in checked_tree:
                print(f"Data ---> {data}")

            print(f"Data length ---> {len(checked_tree)}")
            new_data = []
            i = 0
            while i < len(checked_tree):
                if i + 4 <= len(checked_tree):
                    print("\nStart performing operations to 4 Quaternions\n")
                    new_data.append(*perform_operations(checked_tree[i:i + 4]))
                    i += 4
                elif i + 3 <= len(checked_tree):
                    print("\nStart performing operations to 3 Quaternions\n")
                    new_data.append(*convolution_three_elements(checked_tree[i:i + 3]))
                    i += 3
                elif i + 2 <= len(checked_tree):
                    print("\nStart performing operations to 2 Quaternions\n")
                    new_data.append(*multiply_quaternions(checked_tree[i:i + 2]))
                    i += 2
                else:
                    new_data.append(checked_tree[i])
                    i += 1
            self.checked_transaction = part_of_next_transaction
            curent_level += 1

        print(new_data[0] == self.tree[self.height_of_tree()][0])

                
       
     

def main():
    """
    Main entry point of the program.
    """
    file_path = 'test_str.txt'  
    data = read_chunks_from_file(file_path)
    processor = QuaternionProcessor(data)
    quaternions = processor.make_quaternion()
    res = multiply_quaternions(quaternions)   
    i = 0
    for data in res:
        print(f"Zero level: {i} {data}")
        i+=1
    results = reduce_data(res)
    proof = Proof(results,67)

    print("Number of elements:", proof.number_of_elements())
    print("Complete sets of 4:", proof.complete_sets_of_4())
    print("Height of tree:", proof.height_of_tree())
    print("Transaction for proof", proof.proof_transaction())


if __name__ == '__main__':
    main()
