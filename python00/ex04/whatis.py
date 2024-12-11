import sys

def even_or_odd(number):
    if number % 2 == 0:
        return "I'm Even."
    else:
        return "I'm Odd."

def main():
    if (len(sys.argv) < 2):
        return
    try:
        if(len(sys.argv) > 2):
            raise AssertionError("more than one argument is provided")
        number = int(sys.argv[1])
        print(even_or_odd(number))
    except AssertionError as error:
        print(f"{AssertionError.__name__} : {error}")
    except ValueError as error:
        print(f"{AssertionError.__name__} : argument is not an integer")

main()

