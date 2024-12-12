def checkList(liste, type):
    """
    Checks if all elements in a given list are of a specified type.
    """
    return all(isinstance(element, type) for element in liste)


def checkElement(liste):
    """
    Checks if all elements in a given list are positive numbers.
    """
    return all(element > 0 for element in liste)


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calculates the Body Mass Index (BMI) for a list of heights and weights.
    Parameters:
    - height (list[int | float]): A list of heights in meters.
    - weight (list[int | float]): A list of weights in kilograms.
    Returns:
    - list[int | float]: A list of BMI values for each height-weight pair.
    - list: An empty list if an exception occurs.
    """
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
    """
    Compares BMI values to a specified limit and returns a boolean list.
    Parameters:
        - bmi (list[int | float]): A list of BMI values.
        - limit (int): The threshold limit for comparison.
    Returns:
        - list: A list of booleans indicating if each BMI is above the limit.
        - list: An empty list if an exception occurs.
    Exceptions:
        - TypeError: If the limit is not an integer.
        - AssertionError: If BMI elements are not integers or floats.
    """
    try:
        if not isinstance(limit, int):
            raise TypeError("Limit must be a int")
        if not checkList(bmi, (int, float)):
            raise AssertionError("bmi must be integers or floats.")
        return [i > limit for i in bmi]
    except Exception as error:
        print(f"{Exception.__name__} : {error}")
        return []
