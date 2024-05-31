# import math





# class Proof:
#     def __init__(self, data):
#         self.tree = data

#     def number_of_elements(self):
#         """
#         Determines the number of elements in the list.
#         """
#         return len(self.tree[0])

#     def complete_sets_of_4(self):
#         """
#         Determines the complete sets of 4 elements in the list.
#         """
#         return len(self.tree[0]) // 4

#     def height_of_tree(self):
#         """
#         Determines the height of a tree.
#         """
#         log4_N = math.log(self.number_of_elements) / math.log(4) #log4(N)
#         high = math.ceil(log4_N) 
#         return high


#     def proof_transaction(self):
#         pass


# data = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],[1,2,3,4,5,6],[1,2],[1]]
# proof = Proof(data)

# print("Number of elements:", proof.number_of_elements())
# print("Complete sets of 4:", proof.complete_sets_of_4())