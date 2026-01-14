def cpy(registers, x, y):
    x = registers[x] if x in registers else x
    registers[y] = x

def inc(registers, x):
    registers[x] += 1

def dec(registers, x):
    registers[x] -= 1

def jnz(registers, x, y):
    x = registers[x] if x in registers else x
    y = registers[y] if y in registers else y
    if x:
        return y
    
OPCODES = {
    "cpy": cpy,
    "inc": inc,
    "dec": dec,
    "jnz": jnz
}