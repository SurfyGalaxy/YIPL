import index
variables = {}

def printy(args):
    global variables
    try:
        if isinstance(args, dict):
            # For instances such as: {set: [$a, equality: [a, b]]}
            nested_name = list(args.keys())[0]     # 'equality'
            nested_args = args[nested_name]        # ['Yes', 'Yes']
            
            result = index.findfunc(nested_name, nested_args)
        else:
            if args.startswith('$'):
                result = variables[args]
            else:
                result = args
        print(result)
        return True
    except Exception as e:
        return e


def set(name, value):
    global variables
    try:
        if isinstance(value, dict):
            # For instances such as: {set: [$a, equality: [a, b]]}
            nested_name = list(value.keys())[0]     # 'equality'
            nested_args = value[nested_name]        # ['Yes', 'Yes']
            
            result = index.findfunc(nested_name, nested_args)
            

            if not name.startswith('$'):
                name = '$' + name
            variables[name] = result
        else:
            if type(name) == str:
                if not name.startswith('$'):
                    name = '$' + name
                variables[name] = value
        return True
    except Exception as e:
        return e
    

def equality(a, b):
    global variables
    try:
        if isinstance(a, dict):
            # For instances such as: {set: [$a, equality: [a, b]]}
            nested_name = list(a.keys())[0]     # 'equality'
            nested_args = a[nested_name]        # ['Yes', 'Yes']
            result_a = index.findfunc(nested_name, nested_args)
        else:
            if type(a) == str:
                if a.startswith('$'):
                    a = variables[a]
            result_a = a
        if isinstance(b, dict):
            # For instances such as: {set: [$a, equality: [a, b]]}
            nested_name = list(b.keys())[0]     # 'equality'
            nested_args = b[nested_name]        # ['Yes', 'Yes']
            
            result_b = index.findfunc(nested_name, nested_args)
        else:
            if type(b) == str:
                if b.startswith('$'):
                    b = variables[b]
            result_b = b
        return result_a == result_b
    except Exception as e:
        return e

def greater(a, b):
    global variables
    try:
        if isinstance(a, dict):
            # For instances such as: {set: [$a, equality: [a, b]]}
            nested_name = list(a.keys())[0]     # 'equality'
            nested_args = a[nested_name]        # ['Yes', 'Yes']
            
            result_a = index.findfunc(nested_name, nested_args)
        else:
            if type(a) == str:
                if a.startswith('$'):
                    a = variables[a]
            result_a = a
        if isinstance(b, dict):
            # For instances such as: {set: [$a, equality: [a, b]]}
            nested_name = list(b.keys())[0]     # 'equality'
            nested_args = b[nested_name]        # ['Yes', 'Yes']
            
            result_b = index.findfunc(nested_name, nested_args)
        else:
            if type(b) == str:
                if b.startswith('$'):
                    b = variables[b]
            result_b = b
        return result_a > result_b
    except Exception as e:
        return e

def ory(a, b):
    global variables
    try:
        if isinstance(a, dict):
            # For instances such as: {set: [$a, equality: [a, b]]}
            nested_name = list(a.keys())[0]     # 'equality'
            nested_args = a[nested_name]        # ['Yes', 'Yes']
            
            result_a = index.findfunc(nested_name, nested_args)
        else:
            if type(a) == str:
                if a.startswith('$'):
                    a = variables[a]
            result_a = a
        if isinstance(b, dict):
            # For instances such as: {set: [$a, equality: [a, b]]}
            nested_name = list(b.keys())[0]     # 'equality'
            nested_args = b[nested_name]        # ['Yes', 'Yes']
            
            result_b = index.findfunc(nested_name, nested_args)
        else:
            if type(b) == str:
                if b.startswith('$'):
                    b = variables[b]
            result_b = b
        return result_a or result_b
    except Exception as e:
        return e

def andy(a, b):
    global variables
    try:
        if isinstance(a, dict):
            # For instances such as: {set: [$a, equality: [a, b]]}
            nested_name = list(a.keys())[0]     # 'equality'
            nested_args = a[nested_name]        # ['Yes', 'Yes']
            
            result_a = index.findfunc(nested_name, nested_args)
        else:
            if type(a) == str:
                if a.startswith('$'):
                    a = variables[a]
            result_a = a
        if isinstance(b, dict):
            # For instances such as: {set: [$a, equality: [a, b]]}
            nested_name = list(b.keys())[0]     # 'equality'
            nested_args = b[nested_name]        # ['Yes', 'Yes']
            
            result_b = index.findfunc(nested_name, nested_args)
        else:
            if type(b) == str:
                if b.startswith('$'):
                    b = variables[b]
            result_b = b
        return result_a and result_b
    except Exception as e:
        return e

def noty(a):
    global variables
    try:
        if isinstance(a, dict):
            # For instances such as: {set: [$a, equality: [a, b]]}
            nested_name = list(a.keys())[0]     # 'equality'
            nested_args = a[nested_name]        # ['Yes', 'Yes']
            
            result_a = index.findfunc(nested_name, nested_args)
        else:
            if type(a) == str:
                if a.startswith('$'):
                    a = variables[a]
            result_a = a
        return not result_a
    except Exception as e:
        return e