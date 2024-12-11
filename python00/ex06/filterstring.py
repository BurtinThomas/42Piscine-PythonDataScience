import sys

checkArgsNumber = lambda arguments: len(arguments) == 3


def correct_string():
    """
    Checks if the first argument is a valid string.
    Returns:
        True if the first argument is a valid string, False otherwise.
    """
    return all(c == " " or c.isalpha() for c in sys.argv[1])


def correct_int():
    """
    Checks if the second argument is a valid integer.
    Returns:
        True if the second argument is a valid integer, False otherwise.
    """
    return sys.argv[2].isdigit()


def filterstring(text, N):
    """
    Filters a string by removing words shorter than N characters.
    Args:
        text: The input string.
        N: The minimum word length.
    Returns:
        A list of words longer than N characters.
    """
    return [word for word in text.split() if len(word) > N]


def main():
    """
    Main function to execute the filtering process.
    Raises:
        AssertionError: If the arguments are invalid.
    """
    try:
        if not checkArgsNumber(sys.argv) or not correct_string() or not correct_int():
            raise AssertionError("the arguments are bad")
        result = filterstring(sys.argv[1], int(sys.argv[2]))
        print(result)
    except AssertionError as error:
        print(f"{AssertionError.__name__} : {error}")


if __name__ == "__main__":
    main()
