import yaml
import functions as func
import index
with open("instructions.yaml") as f: # Copied from my other project, Clide
    instructions = yaml.safe_load(f)

keys = []
values = []

#print(instructions)

for i in instructions:
    keys.append(i)
    values.append(instructions[i])


while func.pc < len(keys): #iterate over every key in instructions
    index.findfunc(keys[func.pc], values[func.pc], False)