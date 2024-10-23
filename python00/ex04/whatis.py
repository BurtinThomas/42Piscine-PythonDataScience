import sys

def even_or_odd(number) -> str:
    if(number % 2 == 0):
        return "I'm Even."
    else:
        return "I'm Odd"

def check_arg():
    if(len(sys.argv) > 2):
        raise AssertionError("more than one argument is provided")

def main():

    if(len(sys.argv) < 2):
        return
    try:
        check_arg()
        number = int(sys.argv[1])
        print(even_or_odd(number))
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        return
    except ValueError:
        print(AssertionError.__name__ + ": argument is not an integer")

main()