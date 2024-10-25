def mean(args):
    return sum(args) / len(args)

def meadian(argsSort):
    if len(argsSort) % 2 == 0:
        first = len(argsSort) // 2 - 1
        seconde = len(argsSort) // 2
        result = (argsSort[first] + argsSort[seconde]) / 2
    else:
        indexResult = len(argsSort) // 2
        result = argsSort[indexResult]
    return result

def quartile(argsSort):
    q1_index = len(argsSort) // 4
    q3_index = q1_index * 3
    quartile = [float(argsSort[q1_index]), float(argsSort[q3_index])]
    return quartile

def variance(argsSort):
    variance_total = 0
    for value in argsSort:
        variance_total += (value - mean(argsSort)) ** 2
    variance = variance_total / len(argsSort)
    return variance

def check_error(args):
    if len(args) == 0:
        print("ERROR")
        return False
    return True


def ft_statistics(*args, **kwargs):
    argsSort = sorted(args)
    if "mean" in kwargs.values() and check_error(args):
        print(f"mean : {mean(args)}")

    if "median" in kwargs.values() and check_error(args):
        print(f"median : {meadian(argsSort)}")
    
    if "quartile" in kwargs.values() and check_error(args):
        print(f"quartile : {quartile(argsSort)}")
    
    if "std" in kwargs.values() and check_error(args):
        print(f"std : {variance(argsSort) ** 0.5}")
    
    if "var" in kwargs.values() and check_error(args):
        print(f"var : {variance(argsSort)}")

        
