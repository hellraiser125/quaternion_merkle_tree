from quaternion_processor import QuaternionProcessor, multiply_quaternions,perform_operations, Quaternion

class Conveyor():
    def __init__(self):
        pass






# Приклад використання:
data = [1, 2, 3, 4, 5]  # Приклад даних (кватерніонів)
result = reduce_data(data)
print("Результат згортання:", result)



class Strategy:
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """
    def do_algorithm(self, data: List):
        pass


"""
Concrete Strategies implement the algorithm while following the base Strategy
interface. The interface makes them interchangeable in the Context.
"""


class TwoStrategy(Strategy):
    def process_quaterion(self, data: Quaternion) -> Quaternion
        return sorted(data)


class OtherStrategy(Strategy):
    def process_quaterion(self, data: Quaternion) -> Quaternion:
        return reversed(sorted(data))
    

class ZeroStrategy(Strategy):
    def process_quaterion(self, data: Quaternion) -> Quaternion:
        return sorted(data)

