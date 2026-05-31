import yaml
import functions as func
import index
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

    index.findfunc(keys[count], values[count])
    
    count += 1