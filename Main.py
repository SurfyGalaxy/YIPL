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
        if not func.printy(values[count][0]):
            print(f"ValueError in {keys[count]}: No varible called '{values[count][0]}'")

    elif keys[count].startswith("set_") or keys[count] == "set": # Equal to python assignment ( x = "value" )
        if not func.set(values[count][0], values[count][1]):
            print(f)
    count += 1