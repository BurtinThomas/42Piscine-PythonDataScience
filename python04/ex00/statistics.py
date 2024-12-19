def mean(args):
    return (sum(args) / len(args))


def median(args):
    args.sort()
    if len(args) % 2 == 0:
        position_median1 = len(args) // 2 - 1
        position_median2 = position_median1 + 1
        return (mean((args[position_median1], args[position_median2])))
    else:
        position_median = len(args) // 2
        return (args[position_median])


def quartile(args):
    q1_index = len(args) // 4
    q3_index = q1_index * 3
    quartile = [float(args[q1_index]), float(args[q3_index])]
    return quartile


def standartDeviation(args):
    return variance(args) ** 0.5


def variance(args):
    variance_total = 0
    for value in args:
        variance_total += (value - mean(args)) ** 2
    variance = variance_total / len(args)
    return variance


def ft_statistics(*args, **kwargs) -> None:
    operations = {
        "mean": mean,
        "median": median,
        "quartile": quartile,
        "std": standartDeviation,
        "var": variance,
    }
    try:
        if len(args) == 0:
            for i in range(len(kwargs.keys())):
                print("ERROR")
            return
        if not all(isinstance(i, int) for i in args):
            raise AssertionError("bad type")

        args_sort = list(args)
        for operation_name in kwargs.values():
            if operation_name in operations:
                result = operations[operation_name](args_sort)
                print(f"{operation_name} : {result}")
    except Exception as error:
        print(f"{type(error).__name__} : {error}")
