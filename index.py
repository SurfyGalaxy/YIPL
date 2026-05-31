import functions as func
def findfunc(keys, values):
    if keys.startswith("print_") or keys == "print": # Equal to python print() operator
        x = func.printy(values[0])
        if x:
            return x
        else:
            print(f"Error in {keys}: {x}")
            return None

    elif keys.startswith("set_") or keys == "set": # Equal to python assignment ( x = "value" )
        x = func.set(values[0], values[1])
        if x != True:
            print(f"Error in {keys}: {x}")

    elif keys.startswith("equality_") or keys == "equality":
        x = func.equality(values[0], values[1])
        if x:
            return x
        else:
            print(f"Error in {keys}: {x}")
            return None
    
    elif keys.startswith("greater_") or keys == "greater":
        x = func.greater(values[0], values[1])
        if x:
            return x
        else:
            print(f"Error in {keys}: {x}")
            return None

    elif keys.startswith("less_") or keys == "less":
        x = func.less(values[0], values[1])
        if x:
            return x
        else:
            print(f"Error in {keys}: {x}")
            return None

    elif keys.startswith("or_") or keys == "or":
        x = func.ory(values[0], values[1])
        if x:
            return x
        else:
            print(f"Error in {keys}: {x}")
            return None
    
    elif keys.startswith("and_") or keys == "and":
        x = func.andy(values[0], values[1])
        if x:
            return x
        else:
            print(f"Error in {keys}: {x}")
            return None

    elif keys.startswith("not_") or keys == "not":
        x = func.noty(values[0])
        if x:
            return x
        else:
            print(f"Error in {keys}: {x}")
            return None