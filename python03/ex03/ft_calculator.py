
class calculator:
    def __init__(self, vector):
        self.vector = vector
    
    def __add__(self, object):
        self.vector = [i + object for i in self.vector]
        print(self.vector)
    
    def __mul__(self, object):
        self.vector = [i * object for i in self.vector]
        print(self.vector)
    
    def __sub__(self, object):
        self.vector = [i - object for i in self.vector]
        print(self.vector)
    
    def __truediv__(self, object):
        if object == 0:
            print("Division by zero is not allowed.")
            return
        self.vector = [i / object for i in self.vector]
        print(self.vector)