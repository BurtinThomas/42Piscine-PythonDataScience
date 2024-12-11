
def all_thing_is_obj(object: any) -> int:

    listDictionnary = {
        list: "list",
        tuple: "tuple",
        set: "set",
        dict: "dict",
        str: "str",
    }

    if type(object) not in listDictionnary:
        print("Type not found")
    elif(type(object) is str):
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print(f"{listDictionnary[type(object)]} : {type(object)}")
    return 42
