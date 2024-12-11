import math

def isnan(object):
    if(object != object):
        return True
    return False

def NULL_not_found(object: any) -> int:
    listDictionnary = {
        None: "Nothing: None",
        math.nan: "Cheese: nan",
        float: "Cheese: nan",
        0: "Zero: 0",
        '': "Empty: ",
        False: "Fake: False",
    }
    if(type(object) == float and isnan(object)):
        print(f"{listDictionnary[math.nan]} {type(object)}")
    elif object not in listDictionnary:
        print("Type not found")
        return 1
    elif object == 0 and type(object) == int:
        print(f"Zero: {object} {type(object)}")
    else:
        print(f"{listDictionnary[object]} {type(object)}")
    return 0