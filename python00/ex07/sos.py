import sys


def checkArgs(arg):
    """
    Checks that all characters are alphabetic letters or spaces.
    Parameters:
    - arg: The string to check.
    Return:
    - bool: True if all characters are letters or spaces, False otherwise.
    """
    return all(c == " " or c.isalpha() for c in arg)


def encodeInMorse(string):
    """
    Converts a string to its equivalent in Morse code.
    Parameters:
    - string: The string to convert to Morse code.
    Return:
    - list: A list of Morse code characters
    corresponding to each letter of the string.

    """
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/',
    }
    return [morse_code_dict[lettre.upper()] for lettre in string]


def main():
    """
    Checks the arguments passed to the script
    and performs the conversion to Morse code.
    If the arguments are incorrect, an error message is displayed.
    No return value.

    """
    try:
        if (len(sys.argv) != 2 or not checkArgs(sys.argv[1])):
            raise AssertionError("the arguments are bad")
        tab_morse = encodeInMorse(sys.argv[1])
        string_morse = ' '.join(tab_morse)
        print(string_morse)
    except AssertionError as error:
        print(f"{AssertionError.__name__} : {error}")


if __name__ == "__main__":
    main()
