
class calculator:
    def __init__(self, vector):
        self.vector = vector
    
    @staticmethod
    def dotproduct(l1, l2):
        result = sum([i * y for i, y in zip(l1, l2)])
        print(f"Dot product is: {result}")
    
    @staticmethod
    def add_vec(l1 : list[float], l2 : list[float]):
        result = [float(i + y) for i, y in zip(l1, l2)]
        print(f"Add Vector is : {result}")
    
    @staticmethod
    def sous_vec(l1, l2):
        result = [float(i - y) for i, y in zip(l1, l2)]
        print(f"Sous Vector is: {result}")
