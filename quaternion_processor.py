import struct
from typing import Union




from typing import Union, List, Dict

class Quaternion:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

class QuaternionProcessor:
    """
    A class to process chunk data and calculate quaternion values.

    Attributes:
        chunk_data (Union[dict, list]): The input data to be processed, which can be a dictionary or a list.
    """

    def __init__(self, chunk_dict: Union[dict, list]):
        self.chunk_data = chunk_dict

    def make_quaternion(self, final_version=True) -> List[Quaternion]:
        """
        Processes the chunk data and calculates quaternion values.

        Args:
            final_version (bool, optional): Flag indicating if the final version of processing should be used. Defaults to True.

        Input data:
            List of Quaternions (using when processing at tree creation)
            Dict of data (using when program starting to extract data from file and make qaternions)
        Returns:
            List[Quaternion]: A list of Quaternion instances created from the processed data.
        """
        quaternion_parts = []
        quaternions = []

        # Type guard: if data is already processed (as a list), just return Quaternion instances
        if isinstance(self.chunk_data, list):
            for data in self.chunk_data:
                quaternion_parts.append(data)
                if len(quaternion_parts) == 4:
                    quaternions.append(Quaternion(*quaternion_parts))
                    quaternion_parts.clear()
            return quaternions

        # Process chunk data when it is in dictionary format
        for decimal_values in self.chunk_data.values():
            quaternion = 0
            for index, data in enumerate(decimal_values, start=0):
                if data != 0:
                    quaternion += data << (8 * index)  # Use bitwise shift for efficient calculation
            quaternion_parts.append(quaternion)
            if len(quaternion_parts) == 4:
                quaternions.append(Quaternion(*quaternion_parts))
                quaternion_parts.clear()
                
        return quaternions

    
class Quaternion:
    """
    A class to represent a quaternion and perform operations on quaternions.

    Attributes:
        a (int): The scalar part of the quaternion.
        b (int): The coefficient of the i component.
        c (int): The coefficient of the j component.
        d (int): The coefficient of the k component.
    """

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self):
        """
        Returns a string representation of the quaternion.

        Returns:
            str: A string in the form "a + (b)i + (c)j + (d)k".
        """
        return f"{self.a} + ({self.b})i + ({self.c})j + ({self.d})k"

    def __mul__(self, other):
        """
        Multiplies the quaternion by another quaternion using component-wise multiplication 
        with modular arithmetic to avoid overflow.

        Args:
            other (Quaternion): The other quaternion to multiply with.

        Returns:
            Quaternion: The resulting quaternion from the multiplication.
        """
        a1, b1, c1, d1 = self.a, self.b, self.c, self.d
        a2, b2, c2, d2 = other.a, other.b, other.c, other.d
        modulus = 2**64

        lower_64_bits_mask = (1 << 64) - 1

        # Calculate products and moduli for each component
        a1a2_product = ((a1 * a2) & lower_64_bits_mask + (a1 * a2) >> 64) % modulus
        b1b2_product = ((b1 * b2) & lower_64_bits_mask + (b1 * b2) >> 64) % modulus
        c1c2_product = ((c1 * c2) & lower_64_bits_mask + (c1 * c2) >> 64) % modulus
        d1d2_product = ((d1 * d2) & lower_64_bits_mask + (d1 * d2) >> 64) % modulus

        a1b2_product = ((a1 * b2) & lower_64_bits_mask + (a1 * b2) >> 64) % modulus
        b1a2_product = ((b1 * a2) & lower_64_bits_mask + (b1 * a2) >> 64) % modulus
        c1d2_product = ((c1 * d2) & lower_64_bits_mask + (c1 * d2) >> 64) % modulus
        d1c2_product = ((d1 * c2) & lower_64_bits_mask + (d1 * c2) >> 64) % modulus

        a1c2_product = ((a1 * c2) & lower_64_bits_mask + (a1 * c2) >> 64) % modulus
        c1a2_product = ((c1 * a2) & lower_64_bits_mask + (c1 * a2) >> 64) % modulus
        d1b2_product = ((d1 * b2) & lower_64_bits_mask + (d1 * b2) >> 64) % modulus
        b1d2_product = ((b1 * d2) & lower_64_bits_mask + (b1 * d2) >> 64) % modulus

        a1d2_product = ((a1 * d2) & lower_64_bits_mask + (a1 * d2) >> 64) % modulus
        d1a2_product = ((d1 * a2) & lower_64_bits_mask + (d1 * a2) >> 64) % modulus
        b1c2_product = ((b1 * c2) & lower_64_bits_mask + (b1 * c2) >> 64) % modulus
        c1b2_product = ((c1 * b2) & lower_64_bits_mask + (c1 * b2) >> 64) % modulus

        # Compute the components of the resulting quaternion with modular arithmetic
        a_temp = (((a1a2_product - b1b2_product) - c1c2_product) - d1d2_product)
        a = (a_temp + modulus) % modulus if a_temp < 0 else a_temp & lower_64_bits_mask

        b_temp = ((a1b2_product + b1a2_product) % modulus + c1d2_product % modulus - d1c2_product % modulus) % modulus
        b = (b_temp + modulus) % modulus if b_temp < 0 else b_temp & lower_64_bits_mask

        c_temp = ((a1c2_product + c1a2_product) % modulus + d1b2_product % modulus - b1d2_product % modulus) % modulus
        c = (c_temp + modulus) % modulus if c_temp < 0 else c_temp & lower_64_bits_mask

        d_temp = ((a1d2_product + d1a2_product) % modulus + b1c2_product % modulus - c1b2_product % modulus) % modulus
        d = (d_temp + modulus) % modulus if d_temp < 0 else d_temp & lower_64_bits_mask

        return Quaternion(a, b, c, d)



def multiply_quaternions(quaternions):
    """
    Multiplies a list of quaternions sequentially.

    Args:
        quaternions (list): A list of Quaternion objects to be multiplied.

    Returns:
        list: A list of intermediate Quaternion results after each multiplication.
    """
    mul = quaternions[0]
    result = []

    # Check if the first element is a list of quaternions and adjust accordingly
    if isinstance(mul, list):
        mul = mul[0]

    print(f"Initial quaternion: {mul}")

    # Multiply each quaternion sequentially
    for i in range(1, len(quaternions)):
        mul = mul * quaternions[i]
        print(f"After multiplying with quaternion {i}: {mul}")
        result.append(mul)
    
    return result

   
def perform_operations(quaternions):
    """
    Perform a series of operations on a list of quaternions.

    This function calculates specific results based on the elements of the four quaternions and 
    their interactions according to the defined algorithm. The operations involve modular arithmetic 
    and bitwise operations to handle 64-bit constraints.

    Args:
        quaternions (list): A list of quaternions. Each quaternion is expected to have attributes a, b, c, and d.

    Returns:
        list: A list containing the results of the performed operations.
    """
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

    final_result = sum_quaternion_parts_with_modulus(results)
    print(*final_result)

    return final_result


def sum_quaternion_parts_with_modulus(parts, modulus=2**64):
    """
    Sum the parts of quaternions with a specified modulus and return the result as a Quaternion.

    This function takes a list of parts of quaternions which we have after function perform_operations, sums each corresponding part using modular arithmetic, 
    and constructs a Quaternion from the results.

    Args:
        parts (list): A list containing parts of quaternions. Each element in the list represents a specific part 
                      (a, b, c, or d) of multiple quaternions.
        modulus (int, optional): The modulus to use for the summation. Defaults to 2**64.

    Returns:
        list: A list containing one Quaternion which is the sum of the input parts modulo the specified modulus.
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
   



