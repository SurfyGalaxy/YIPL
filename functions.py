import index
variables = {}

def printy(args):
    global variables
    try:
        if args.startswith('$'):
                args = variables[args]
        print(args)
        return True
    except Exception as e:
        return e


def set(name, value):
    global variables
    try:
        if isinstance(value, dict): # e.g. {'equality': ['Yes', 'Yes]}
            # Extract function name and args
            nested_name = list(value.keys())[0]     # 'equality'
            nested_args = value[nested_name]        # ['Yes', 'Yes']
            
            result = index.findfunc(nested_name, nested_args)

            if not name.startswith('$'):
                name = '$' + name
            variables[name] = result
 
        else:
            if not name.startswith('$'):
                name = '$' + name
            variables[name] = value
        return True
    except Exception as e:
        return e
    

def equality(a, b):
    global variables
    try:
        if a.startswith('$'):
            a = variables[a]
        if b.startswith('$'):
            b = variables[b]
        return a == b
    except Exception as e:
        return e

def greater(a, b):
    global variables
    try:
        if a.startswith('$'):
            a = variables[a]
        if b.startswith('$'):
            b = variables[b]
        return a > b
    except Exception as e:
        return e

def less(a, b):
    global variables
    try:
        if a.startswith('$'):
            a = variables[a]
        if b.startswith('$'):
            b = variables[b]
        return a < b
    except Exception as e:
        return e

def ory(a, b):
    global variables
    try:
        if a.startswith('$'):
            a = variables[a]
        if b.startswith('$'):
            b = variables[b]
        return a or b
    except Exception as e:
        return e

def andy(a, b):
    global variables
    try:
        if a.startswith('$'):
            a = variables[a]
        if b.startswith('$'):
            b = variables[b]
        return a and b
    except Exception as e:
        return e

def noty(a):
    global variables
    try:
        if a.startswith('$'):
            a = variables[a]
        return not a
    except Exception as e:
        return e