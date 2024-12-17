
class calculator:
    def __init__(self, list):
        self.list = list

    def __add__(self, object) -> None:
        self.list = [i + object for i in self.list]
        print(self.list)

    def __mul__(self, object) -> None:
        self.list = [i * object for i in self.list]
        print(self.list)

    def __sub__(self, object) -> None:
        self.list = [i - object for i in self.list]
        print(self.list)

    def __truediv__(self, object) -> None:
        self.list = [i / object for i in self.list]
        print(self.list)
