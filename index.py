import functions as func



def handle_dependencies(args):
    if isinstance(args, dict):
    # For instances such as: {set: [$a, equality: [a, b]]}    This has broken far too many times
        nested_name = list(args.keys())[0]     # 'equality'
        nested_args = args[nested_name]        # ['Yes', 'Yes']
        
        result = findfunc(nested_name, nested_args, True)
    else:
        if type(args) == str:
            if args.startswith('$'):
                result = func.variables[args]
            else:
                result = args
        else:
            result = args
    return result

def handle_dependencies_set(args):
    if isinstance(args, dict):
    # For instances such as: {set: [$a, equality: [a, b]]}    This has broken far too many times
        nested_name = list(args.keys())[0]     # 'equality'
        nested_args = args[nested_name]        # ['Yes', 'Yes']
        
        result = findfunc(nested_name, nested_args, True)
    else:
        if type(args) == str:
            if not args.startswith('$'):
                result = '$' + args
            else:
                result = args
        else:
            result = args
    return result


def findfunc(keys: str | dict, values: any, is_nesting: bool) -> any:
    if keys.startswith("print_") or keys == "print": # Equal to python print() operator
        a = handle_dependencies(values[0])
        x = func.printy(a)
        if not isinstance(x, Exception):
            increment(is_nesting)
            return x
        else:
            print(f"Error in {keys}: {x}")
            return None
            increment(is_nesting)

    elif keys.startswith("set_") or keys == "set": # Equal to python assignment ( x = "value" )
        a = handle_dependencies_set(values[0])
        b = handle_dependencies(values[1])
        x = func.set(a, b)
        if not isinstance(x, Exception):
            increment(is_nesting)
            return x
        else:
            print(f"Error in {keys}: {x}")
            increment(is_nesting)
            return None

    elif keys.startswith("equality_") or keys == "equality":
        a = handle_dependencies(values[0])
        b = handle_dependencies(values[1])
        x = func.equality(a, b)
        if not isinstance(x, Exception):
            increment(is_nesting)
            return x
        else:
            print(f"Error in {keys}: {x}")
            increment(is_nesting)
            return None
    
    elif keys.startswith("greater_") or keys == "greater":
        a = handle_dependencies(values[0])
        b = handle_dependencies(values[1])
        x = func.greater(a, b)
        if not isinstance(x, Exception):
            increment(is_nesting)
            return x
        else:
            print(f"Error in {keys}: {x}")
            increment(is_nesting)
            return None

    elif keys.startswith("less_") or keys == "less":
        a = handle_dependencies(values[0])
        b = handle_dependencies(values[1])
        x = func.less(a, b)
        if not isinstance(x, Exception):
            increment(is_nesting)
            return x
        else:
            print(f"Error in {keys}: {x}")
            increment(is_nesting)
            return None

    elif keys.startswith("or_") or keys == "or":
        a = handle_dependencies(values[0])
        b = handle_dependencies(values[1])
        x = func.ory(a, b)
        if not isinstance(x, Exception):
            increment(is_nesting)
            return x
        else:
            print(f"Error in {keys}: {x}")
            increment(is_nesting)
            return None
    
    elif keys.startswith("and_") or keys == "and":
        a = handle_dependencies(values[0])
        b = handle_dependencies(values[1])
        x = func.andy(a, b)
        if not isinstance(x, Exception):
            increment(is_nesting)
            return x
        else:
            print(f"Error in {keys}: {x}")
            increment(is_nesting)
            return None

    elif keys.startswith("not_") or keys == "not":
        a = handle_dependencies(values[0])
        x = func.noty(a)
        if not isinstance(x, Exception):
            increment(is_nesting)
            return x
        else:
            print(f"Error in {keys}: {x}")
            increment(is_nesting)
            return None

    
    elif keys.startswith("plus_") or keys == "plus":
        a = handle_dependencies(values[0])
        b = handle_dependencies(values[1])
        x = func.add(a, b)
        if not isinstance(x, Exception):
            increment(is_nesting)
            return x
        else:
            print(f"Error in {keys}: {x}")
            increment(is_nesting)
            return None
        
    elif keys.startswith("minus_") or keys == "minus":
        a = handle_dependencies(values[0])
        b = handle_dependencies(values[1])
        x = func.minus(a, b)
        if not isinstance(x, Exception):
            increment(is_nesting)
            return x
        else:
            print(f"Error in {keys}: {x}")
            increment(is_nesting)
            return None
    
    elif keys.startswith("multiply_") or keys == "multiply":
        a = handle_dependencies(values[0])
        b = handle_dependencies(values[1])
        x = func.multiply(a, b)
        if not isinstance(x, Exception):
            increment(is_nesting)
            return x
        else:
            print(f"Error in {keys}: {x}")
            increment(is_nesting)
            return None
    
    elif keys.startswith("divide_") or keys == "divide":
        a = handle_dependencies(values[0])
        b = handle_dependencies(values[1])
        x = func.divide(a, b)
        if not isinstance(x, Exception):
            increment(is_nesting)
            return x
        else:
            print(f"Error in {keys}: {x}")
            increment(is_nesting)
            return None

    elif keys.startswith("goto_") or keys == "goto":
        a = handle_dependencies(values[0])
        x = func.goto(a)
        if not isinstance(x, Exception):
            increment(is_nesting)
            return x
        else:
            print(f"Error in {keys}: {x}")
            increment(is_nesting)
            return None

    elif keys.startswith("if_") or keys == "if":
        a = handle_dependencies(values[0])
        b = handle_dependencies(values[1])
        c = handle_dependencies(values[2])
        x = func.ify(a, b, c)
        if not isinstance(x, Exception):
            increment(is_nesting)
            return x
        else:
            print(f"Error in {keys}: {x}")
            increment(is_nesting)
            return None
    
    elif keys.startswith("input_") or keys == "input":
        a = handle_dependencies(values[0])
        x = func.inputy(a)
        if not isinstance(x, Exception):
            increment(is_nesting)
            return x
        else:
            print(f"Error in {keys}: {x}")
            increment(is_nesting)
            return None
    
    elif keys.startswith("cast_") or keys == "cast":
        a = handle_dependencies(values[0]) # What to cast into (int, str or float)
        b = handle_dependencies(values[1]) # the data
        x = func.cast(a, b)
        if not isinstance(x, Exception):
            increment(is_nesting)
            return x
        else:
            print(f"Error in {keys}: {x}")
            increment(is_nesting)
            return None

    else:
        if keys.startswith('^'): # Intended tag
            increment(is_nesting)
        else:
            increment
            print(f"Unknown Keyword: {keys}")


def increment(is_nesting):
    if is_nesting == False:
        func.pc += 1