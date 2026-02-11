def set(registers, x, y):
    y = registers.get(y, 0) if isinstance(y, str) else y
    registers[x] = y

def add(registers, x, y):
    y = registers.get(y, 0) if isinstance(y, str) else y
    registers[x] = registers.get(x, 0) + y

def mul(registers, x, y):
    y = registers.get(y, 0) if isinstance(y, str) else y
    registers[x] = registers.get(x, 0) * y
    
def mod(registers, x, y):
    y = registers.get(y, 0) if isinstance(y, str) else y
    registers[x] = registers.get(x, 0) % y

def jgz(registers, x, y):
    x = registers.get(x, 0) if isinstance(x, str) else x
    y = registers.get(y, 0) if isinstance(y, str) else y
    if x > 0:
        return y

OPCODES = {
    "set": set,
    "add": add,
    "mul": mul,
    "mod": mod,
    "jgz": jgz
}