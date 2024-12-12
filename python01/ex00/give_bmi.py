
def checkList(liste, type):
    return all(isinstance(element, type) for element in liste)


def checkElement(liste):
    return all(element > 0 for element in liste)


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    try:
        if len(height) != len(weight):
            raise ValueError("height and weight must have same lenght.")
        if not checkList(height, (int, float)) or not checkList(weight, (int, float)):
            raise AssertionError("Height and weight must be integers or floats.")
        if not checkElement(height) or not checkElement(weight):
            raise ValueError("Element must be positive.")
        return [w / (h * h) for w, h in zip(weight, height)]
    except Exception as error:
        print(f"{Exception.__name__} : {error}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        if not isinstance(limit, int):
            raise TypeError("Limit must be a int")
        if not checkList(bmi, (int, float)):
            raise AssertionError("bmi must be integers or floats.")
        return [i > limit for i in bmi]
    except Exception as error:
        print(f"{Exception.__name__} : {error}")
        return []
