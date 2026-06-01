import yaml
variables = {}
program_list = []
pc = 0
def init(lists):
    global program_list
    program_list = lists

def printy(args):
    global variables
    try:
        print(args)
        return True
    except Exception as e:
        return e


def set(name, value):
    global variables
    try:
        variables[name] = value
        return True
    except Exception as e:
        return e
        

def equality(a, b):
    global variables
    try:
        return a == b
    except Exception as e:
        return e

def greater(a, b):
    global variables
    try:
        return a > b
    except Exception as e:
        return e

def less(a, b):
    global variables
    try:
        return a < b
    except Exception as e:
        return e

def ory(a, b):
    global variables
    try:
        return a or b
    except Exception as e:
        return e

def andy(a, b):
    global variables
    try:
        return a and b
    except Exception as e:
        return e

def noty(a):
    global variables
    try:
        return not a
    except Exception as e:
        return e

def add(a, b):
    global variables
    try:
        return a + b
    except Exception as e:
        return e

def minus(a, b):
    global variables
    try:
        return a - b
    except Exception as e:
        return e

def multiply(a, b):
    global variables
    try:
        return a * b
    except Exception as e:
        return e

def divide(a, b):
    global variables
    try:
        return a / b
    except Exception as e:
        return e

def goto(a):
    global variables, program_list, pc
    try:
        position = next(i for i, k in enumerate(program_list) if k == a)
        pc = position
        return True
    except Exception as e:
        return e

def ify(a, b, c):
    global variables, program_list
    try:
        if a == True:
            return goto(b)
        else:
            return goto(c)
        return True
    except Exception as e:
        return e

def inputy(a):
    try:
        return input(a)
    except Exception as e:
        return e