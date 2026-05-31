import yaml
import functions as func
from types import SimpleNamespace

with open("instructions.yaml") as f: # Copied from my other project, Clide
    instructions = yaml.safe_load(f)

keys = []
values = []

#print(instructions)

for i in instructions:
    keys.append(i)
    values.append(instructions[i])

count = 0
while count < len(keys): #iterate over every key in instructions
    #print(keys[count]) # current keyword
    #print(values[count]) # current args
    if keys[count].startswith("print_") or keys[count] == "print": # Equal to python print() operator
        x = func.printy(values[count][0])
        if x != True:
            print(f"Error in {keys[count]}: {x}")

    elif keys[count].startswith("set_") or keys[count] == "set": # Equal to python assignment ( x = "value" )
        x = func.set(values[count][0], values[count][1])
        if x != True:
            print(f"Error in {keys[count]}: {x}")

    elif keys[count].startswith("equality_") or keys[count] == "equality":
        x = func.equality(values[count][0], values[count][1])
        if x != True:
            print(f"Error in {keys[count]}: {x}")
    
    elif keys[count].startswith("greater_") or keys[count] == "greater":
        x = func.greater(values[count][0], values[count][1])
        if x != True:
            print(f"Error in {keys[count]}: {x}")

    elif keys[count].startswith("less_") or keys[count] == "less":
        x = func.less(values[count][0], values[count][1])
        if x != True:
            print(f"Error in {keys[count]}: {x}")

    elif keys[count].startswith("or_") or keys[count] == "or":
        x = func.ory(values[count][0], values[count][1])
        if x != True:
            print(f"Error in {keys[count]}: {x}")
    
    elif keys[count].startswith("and_") or keys[count] == "and":
        x = func.andy(values[count][0], values[count][1])
        if x != True:
            print(f"Error in {keys[count]}: {x}")

    elif keys[count].startswith("not_") or keys[count] == "not":
        x = func.noty(values[count][0])
        if x != True:
            print(f"Error in {keys[count]}: {x}")
    
    count += 1