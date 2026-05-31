variables = {}

def printy(args):
    global variables
    if args.startswith('$'):
        try:
            args = variables[args]
        except KeyError:
            return False
    print(args)
    return True

def set(name, value):
    global variables
    if not name.startswith('$'):
        name = '$' + name
    variables[name] = value