
def give_bmi(height: list[int | float], weight: list[int | float]) -> list[float]:
    try:
        if len(height) != len(weight):
            raise ValueError("height and weight must have same lenght")
        
        new_tab = []
        for h, w in zip(height, weight):
            if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
                raise TypeError("Height and weight must be integers or floats.")
            if h <= 0 or w <= 0:
                raise ValueError("Height and weight values must be positive.")
            bmi = w / (h ** 2)
            new_tab.append(bmi)
        return new_tab

    except Exception as error:
        print(f"{Exception.__name__} : {error}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        if not isinstance(limit, int):
            raise TypeError("Limit must be a int")
        new_tab = []
        for value in bmi:
            if not isinstance(value, (int, float)):
                raise TypeError("La liste dois contenir uniquement des entiers ou des flottants.")
            new_tab.append(value > limit)
        return new_tab

    except TypeError as error:
        print(error)
        return []