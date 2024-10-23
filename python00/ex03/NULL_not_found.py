import math

def isnan(object):
    if(object != object):
        return True
    return False

def NULL_not_found(object: any) -> int:
    type_names = {
        None: "Nothing : None",
        math.nan: "Cheese : nan",
        0: "Zero : 0",
        '': "Empty:  ",
        False: "Fake : False",
    }
    type_name = type_names.get(object, "Type not Found")
    if(type(object) == float and isnan(object)):
        print(f"{type_names[math.nan]} {type(object)}")
    elif(type_name == "Type not Found"):
        print(type_name)
        return 1
    elif(object == 0 and type(object) == int):
        print(f"Zero: {object} {type(object)}")
    else:
        print(f"{type_names[object]} {type(object)}")
    return 0

