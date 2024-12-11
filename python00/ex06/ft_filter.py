def isItEven(number):
    """
    Checks if the given number is even.
    Args:
        number: The number to be checked.
    Returns:
        bool: True if the number is even, False otherwise.
    """
    if number % 2 == 0:
        return True
    else:
        return False


def ft_filter(function, list):
    """
    Filters a list based on a function.
    The function is applied to each element of the list,
    and only the elements for which the function returns True
    are included in the resulting list.
    Args:
        function: The function to be applied to each element.
                It should return a boolean value (True or False).
        list: The list or iterable to be filtered.
    Returns:
        list: A new list containing only the elements
        for which the function returned True.
    """
    newList = [n for n in list if function(n)]
    return newList


def main():
    """
    function to demonstrate the usage of the ft_filter function.
    It filters a list to find the even numbers using the isItEven function,
    then prints the resulting list.
    """
    tab = [1, 2, 3, 4, 5, 6]
    nombres_pairs = ft_filter(isItEven, tab)
    print(nombres_pairs)


if __name__ == "__main__":
    main()
