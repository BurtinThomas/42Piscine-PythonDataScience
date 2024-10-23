import sys

checkArgs = lambda string : all(c == " " or c.isalpha() for c in string)

def encodeInMorse(string):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/',
    }
    return[morse_code_dict[lettre.upper()] for lettre in string]

def main():
    try:
        if(len(sys.argv) != 2 or not checkArgs(sys.argv[1])):
            raise AssertionError("the arguments are bad")
        tab_morse = encodeInMorse(sys.argv[1])
        string_morse = ' '.join(tab_morse)
        print(string_morse)
    except AssertionError as error:
        print(f"{AssertionError.__name__} : {error}")

if __name__ == "__main__":
    main()
    