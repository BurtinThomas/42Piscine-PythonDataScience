import sys

checkArgsNumber = lambda number : len(number) == 3

def correct_string():
    return all(c == " " or c.isalpha() for c in sys.argv[1])

def correct_int():
    return sys.argv[2].isdigit()

def filtrestring(string, N):
    return[word for word in string.split() if len(word) > N]
    
def main():
    try:
        if not checkArgsNumber(sys.argv) or not correct_string() or not correct_int():
            raise AssertionError("the arguments are bad")
        print(filtrestring(sys.argv[1], int(sys.argv[2])))
    except AssertionError as error:
        print(f"{AssertionError.__name__} : {error}")

if __name__ == "__main__":
    main()

