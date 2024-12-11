
def all_thing_is_obj(object: any) -> int:

    listDictionnary = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "str",
    }

    if type(object) not in listDictionnary:
        print("Type not found")
    elif(type(object) is str):
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print(f"{listDictionnary[type(object)]} : {type(object)}")
    return 42
