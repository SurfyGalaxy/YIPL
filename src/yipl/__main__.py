import yaml
import sys
from . import functions as func
from . import index
if len(sys.argv) < 2:
    print("Usage: yipl <filename.yaml>")
    sys.exit()

file_path = sys.argv[1]
try:
    with open(file_path, "r") as f:
        instructions = yaml.safe_load(f)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    sys.exit(1)
except yaml.YAMLError as e:
    print(f"Error parsing YAML: {e}")
    sys.exit(1)

keys = []
values = []

for i in instructions:
    keys.append(i)
    values.append(instructions[i])

func.init(keys)

while func.pc < len(keys): #iterate over every key in instructions
    index.findfunc(keys[func.pc], values[func.pc], False)

sys.exit()