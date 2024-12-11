import sys

def is_special_character(c):
    """
    Checks if a given character is a punctuation character.
    Args:
        c: The character to check.
    Returns:
        bool: True if the character is a special character,
        otherwise False.
    """
    punctuation_characters = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    if c in punctuation_characters:
        return True
    return False


def len_attribut(string, fonction):
    """
    Counts the number of characters in a string
    that satisfy a condition defined by a function.
    Args:
        string: The string to analyze.
        fonction: A function that takes a character
        and returns a boolean.
    Returns:
        int: The number of characters in the string that satisfy the condition.
    """
    counter = 0
    for c in string:
        if fonction(c):
            counter += 1
    return counter


def getInfos(string):
    """
    Prints statistical information about the given text,
    such as the number of characters,
    uppercase letters, lowercase letters,
    special characters, spaces, and digits.
    Args:
        string: The text string to analyze.
    """
    print(f"The text contains {len(string)} characters:")
    print(f"{len_attribut(string, str.isupper)} upper letters")
    print(f"{len_attribut(string, str.islower)} lower letters")
    print(f"{len_attribut(string, is_special_character)} punctuation marks")
    print(f"{len_attribut(string, str.isspace)} spaces")
    print(f"{len_attribut(string, str.isdigit)} digits")


def main():
    """
    The main function of the program.
    It handles text input either from the command line or
    from user input, then calls `getInfos`
    to display the statistics of the text.
    """
    text = ""
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        elif len(sys.argv) < 2:
            while not text.strip():
                try:
                    text = input("> ")
                except KeyboardInterrupt:
                    print("\nInput interrupted. Exiting...")
                    return
                except EOFError:
                    print("\nEnd of input detected. Exiting...")
                    return
        else:
            text = sys.argv[1]
        getInfos(text)

    except AssertionError as error:
        print(f"{AssertionError.__name__} : {error}")


if __name__ == "__main__":
    main()
