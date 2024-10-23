
def all_thing_is_obj(object: any) -> int:

    all_type = {
        list : "list",
        tuple : "tuple",
        set : "set",
        dict : "dict",
        str : "is in the kitchen"
    }
    ob = type(object)
    if (all_type.get(ob) == None):
        print("Type not found")
    elif(ob == str):
        print(f"{object} {all_type[ob]} : {ob}")
    else:
        print(f"{all_type[ob]} : {ob}")
    return 42
