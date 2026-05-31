import index
import yaml
variables = {}
program_list = []

with open("instructions.yaml") as f: # Copied from my other project, Clide
    instructions = yaml.safe_load(f)


for i in instructions:
    program_list.append(i)


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

def add(a, b):
    global variables
    try:
        if isinstance(a, dict):
            # Literally the exact same code as everything else lol
            nested_name = list(a.keys())[0]
            nested_args = a[nested_name]
            
            result_a = index.findfunc(nested_name, nested_args)
        else:
            if type(a) == str:
                if a.startswith('$'):
                    a = variables[a]
            result_a = a
        if isinstance(b, dict):
            nested_name = list(b.keys())[0]
            nested_args = b[nested_name]
            
            result_b = index.findfunc(nested_name, nested_args)
        else:
            if type(b) == str:
                if b.startswith('$'):
                    b = variables[b]
            result_b = b
        return result_a + result_b
    except Exception as e:
        return e

def minus(a, b):
    global variables
    try:
        if isinstance(a, dict):
            # Hi Hack Club reviewer, how's your day going?
            nested_name = list(a.keys())[0]
            nested_args = a[nested_name]
            
            result_a = index.findfunc(nested_name, nested_args)
        else:
            if type(a) == str:
                if a.startswith('$'):
                    a = variables[a]
            result_a = a
        if isinstance(b, dict):
            nested_name = list(b.keys())[0]
            nested_args = b[nested_name]
            
            result_b = index.findfunc(nested_name, nested_args)
        else:
            if type(b) == str:
                if b.startswith('$'):
                    b = variables[b]
            result_b = b
        return result_a - result_b
    except Exception as e:
        return e

def multiply(a, b):
    global variables
    try:
        if isinstance(a, dict):
            # I've not made any input() (yet), so hope it's going good :)
            nested_name = list(a.keys())[0]
            nested_args = a[nested_name]
            
            result_a = index.findfunc(nested_name, nested_args)
        else:
            if type(a) == str:
                if a.startswith('$'):
                    a = variables[a]
            result_a = a
        if isinstance(b, dict):
            nested_name = list(b.keys())[0]
            nested_args = b[nested_name]
            
            result_b = index.findfunc(nested_name, nested_args)
        else:
            if type(b) == str:
                if b.startswith('$'):
                    b = variables[b]
            result_b = b
        return result_a * result_b
    except Exception as e:
        return e

def divide(a, b):
    global variables
    try:
        if isinstance(a, dict):
            # I'm writing this at 1am so idk if im even sentient rn
            nested_name = list(a.keys())[0]
            nested_args = a[nested_name]
            
            result_a = index.findfunc(nested_name, nested_args)
        else:
            if type(a) == str:
                if a.startswith('$'):
                    a = variables[a]
            result_a = a
        if isinstance(b, dict):
            nested_name = list(b.keys())[0]
            nested_args = b[nested_name]
            
            result_b = index.findfunc(nested_name, nested_args)
        else:
            if type(b) == str:
                if b.startswith('$'):
                    b = variables[b]
            result_b = b
        return result_a / result_b
    except Exception as e:
        return e

def goto(a):
    global variables, program_list
    try:
        if isinstance(a, dict):
            # Hello again ASM
            nested_name = list(a.keys())[0]
            nested_args = a[nested_name]
                
            result_a = index.findfunc(nested_name, nested_args)
        else:
            if type(a) == str:
                if a.startswith('$'):
                    a = variables[a]
        result_a = a
        position = next(i for i, k in enumerate(program_list) if k == result_a)
        index.pc = position
        return True
    except Exception as e:
        return e

def ify(a, b, c):
    global variables, program_list
    try:
        if isinstance(a, dict):
            # According to my calculations, this is now turing complete?
            nested_name = list(a.keys())[0]
            nested_args = a[nested_name]
                
            result_a = index.findfunc(nested_name, nested_args)
        else:
            if type(a) == str:
                if a.startswith('$'):
                    a = variables[a]
        result_a = a

        if isinstance(b, dict):
            # Well this is a long function
            nested_name = list(b.keys())[0]
            nested_args = b[nested_name]
                
            result_b = index.findfunc(nested_name, nested_args)
        else:
            if type(b) == str:
                if b.startswith('$'):
                    b = variables[b]
        result_b = b

        if isinstance(c, dict):
            # I should really make this into a function of it's own
            nested_name = list(c.keys())[0]
            nested_args = c[nested_name]
                
            result_c = index.findfunc(nested_name, nested_args)
        else:
            if type(c) == str:
                if c.startswith('$'):
                    c = variables[c]
        result_c = c
        if result_a == True:
            goto(result_b)
        else:
            goto(result_c)
        return True
    except Exception as e:
        return e