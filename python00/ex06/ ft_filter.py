def isit_pair(x):
    return x % 2 == 0

def ft_filter(function, tab):
    if function:
        return [number for number in tab if function(number)]
    return [number for number in tab if number]

def main():
    tab = ["a", "e", "a", "r"]
    nombres_pairs = ft_filter(isit_pair, tab)
    print(nombres_pairs)

if __name__ == "__main__":
    main()