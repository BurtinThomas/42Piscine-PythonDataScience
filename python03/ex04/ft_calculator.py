class calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        result = sum([i * y for i, y in zip(V1, V2)])
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        result = [float(i + y) for i, y in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        result = [float(i - y) for i, y in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
