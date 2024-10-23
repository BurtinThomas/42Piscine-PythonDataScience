import sys

def is_special_character(char: str) -> bool:
    punctuation_characters = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    if char in punctuation_characters:
        return True
    return False

def len_attribut(string, fonction) -> int:
    compteur = 0
    for char in string:
        if fonction(char):
            compteur+=1
    return compteur

def get_infos(string):
    print(f"The text contains {len(string)} characters:")
    print(f"{len_attribut(string, str.isupper)} upper letters")
    print(f"{len_attribut(string, str.islower)} lower letters")
    print(f"{len_attribut(string, is_special_character)} punctuation marks")
    print(f"{len_attribut(string, str.isspace)} spaces")
    print(f"{len_attribut(string, str.isdigit)}  digits")

def main():
    reponse = ""
    try:
        if(len(sys.argv) > 2):
            raise AssertionError("to much parametre")
        elif (len(sys.argv) < 2 ):
            try:
                reponse = input("What is the text to count?\n")
            except EOFError:
                pass
        else:
            reponse = sys.argv[1]
        get_infos(reponse)
            
    except AssertionError as error:
        print(f"{AssertionError.__name__} : {error}")


if __name__ == "__main__":
    main()