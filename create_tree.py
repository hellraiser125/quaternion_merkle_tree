from quaternion_processor import QuaternionProcessor, multiply_quaternions



def perform_operations(quaternions):
    results = []
    lower_64_bits_mask = (1 << 64) - 1
    modulus = 2**64
    # Перебираємо кватерніони
    for i in range(len(quaternions)):
        a1, b1, c1, d1 = quaternions[i].a, quaternions[i].b, quaternions[i].c, quaternions[i].d
        
        # Перебираємо решту кватерніонів
        for j in range(i+1, len(quaternions)):
            a2, b2, c2, d2 = quaternions[j].a, quaternions[j].b, quaternions[j].c, quaternions[j].d
            a3, b3, c3, d3 = quaternions[j-1].a, quaternions[j-1].b, quaternions[j-1].c, quaternions[j-1].d
            a4, b4, c4, d4 = quaternions[j-2].a, quaternions[j-2].b, quaternions[j-2].c, quaternions[j-2].d
    print(f"Quaternion 1 parts : {a1} -- {b1} -- {c1} -- {d1}")
    print(f"Quaternion 2 parts : {a2} -- {b2} -- {c2} -- {d2}")
    print(f"Quaternion 3 parts : {a3} -- {b3} -- {c3} -- {d3}")
    print(f"Quaternion 4 parts : {a4} -- {b4} -- {c4} -- {d4}")
            
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

    

    results.append((result_b_1,result_a_2,result_b_1,result_a_4,result_b_1,result_b_2,result_b_3,result_b_4,result_c_1,result_c_2,result_c_3,result_c_4,result_d_1,result_d_2,result_d_3,result_d_4))
           
    return results


def main():
    """
    Main entry point of the program.
    """
    file_path = 'test_str.txt'  # Replace with your file path
    processor = QuaternionProcessor(file_path)
    quaternions = processor.make_quaternion()
    for data in quaternions:
        print(data)
    print("--------------------------------------------------")
    print("Quaternions After Multiplication")
    print("--------------------------------------------------")
    multiply_results = multiply_quaternions(quaternions)
    operation_results = perform_operations(multiply_results)

    # Виведення результатів операцій
    for result in operation_results:
        print(f"Results after completed operations:")
        print(f"a1: {result[0]}")
        print(f"b1: {result[1]}")
        print(f"c1: {result[2]}")
        print(f"d1: {result[3]}")
        print("-----------------------")
        print(f"a2: {result[4]}")
        print(f"b2: {result[5]}")
        print(f"c2: {result[6]}")
        print(f"d2: {result[7]}")
        print("-----------------------")
        print(f"a3: {result[8]}")
        print(f"b3: {result[9]}")
        print(f"c3: {result[10]}")
        print(f"d3: {result[11]}")
        print("-----------------------")
        print(f"a4: {result[12]}")
        print(f"b4: {result[13]}")
        print(f"c4: {result[14]}")
        print(f"d4: {result[15]}")
        print("-----------------------")
    


if __name__ == '__main__':
    main()
