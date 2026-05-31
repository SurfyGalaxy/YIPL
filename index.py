import functions as func

pc = 0


def findfunc(keys, values):
    if keys.startswith("print_") or keys == "print": # Equal to python print() operator
        x = func.printy(values[0])
        if not isinstance(x, Exception):
            return x
        else:
            print(f"Error in {keys}: {x}")
            return None

    elif keys.startswith("set_") or keys == "set": # Equal to python assignment ( x = "value" )
        x = func.set(values[0], values[1])
        if not isinstance(x, Exception):
            return x
        else:
            print(f"Error in {keys}: {x}")
            return None

    elif keys.startswith("equality_") or keys == "equality":
        x = func.equality(values[0], values[1])
        if not isinstance(x, Exception):
            return x
        else:
            print(f"Error in {keys}: {x}")
            return None
    
    elif keys.startswith("greater_") or keys == "greater":
        x = func.greater(values[0], values[1])
        if not isinstance(x, Exception):
            return x
        else:
            print(f"Error in {keys}: {x}")
            return None

    elif keys.startswith("less_") or keys == "less":
        x = func.less(values[0], values[1])
        if not isinstance(x, Exception):
            return x
        else:
            print(f"Error in {keys}: {x}")
            return None

    elif keys.startswith("or_") or keys == "or":
        x = func.ory(values[0], values[1])
        if not isinstance(x, Exception):
            return x
        else:
            print(f"Error in {keys}: {x}")
            return None
    
    elif keys.startswith("and_") or keys == "and":
        x = func.andy(values[0], values[1])
        if not isinstance(x, Exception):
            return x
        else:
            print(f"Error in {keys}: {x}")
            return None

    elif keys.startswith("not_") or keys == "not":
        x = func.noty(values[0])
        if not isinstance(x, Exception):
            return x
        else:
            print(f"Error in {keys}: {x}")
            return None

    
    elif keys.startswith("plus_") or keys == "plus":
        x = func.add(values[0], values[1])
        if not isinstance(x, Exception):
            return x
        else:
            print(f"Error in {keys}: {x}")
            return None
        
    elif keys.startswith("minus_") or keys == "minus":
        x = func.minus(values[0], values[1])
        if not isinstance(x, Exception):
            return x
        else:
            print(f"Error in {keys}: {x}")
            return None
    
    elif keys.startswith("multiply_") or keys == "multiply":
        x = func.multiply(values[0], values[1])
        if not isinstance(x, Exception):
            return x
        else:
            print(f"Error in {keys}: {x}")
            return None
    
    elif keys.startswith("divide_") or keys == "divide":
        x = func.divide(values[0], values[1])
        if not isinstance(x, Exception):
            return x
        else:
            print(f"Error in {keys}: {x}")
            return None

    elif keys.startswith("goto_") or keys == "goto":
        x = func.goto(values[0])
        if not isinstance(x, Exception):
            return x
        else:
            print(f"Error in {keys}: {x}")
            return None

    elif keys.startswith("if_") or keys == "if":
        x = func.ify(values[0], values[1], values[2])
        if not isinstance(x, Exception):
            return x
        else:
            print(f"Error in {keys}: {x}")
            return None

    
    pc += 1