def hlf(registers, pc, r):
    registers[r] >>= 1
    return pc + 1

def tpl(registers, pc, r):
    registers[r] *= 3
    return pc + 1

def inc(registers, pc, r):
    registers[r] += 1
    return pc + 1

def jmp(registers, pc, offset):
    return pc + offset

def jie(registers, pc, r, offset):
    if registers[r] % 2:
        return pc + 1
    else:
        return jmp(registers, pc, offset)

def jio(registers, pc, r, offset):
    if registers[r] == 1:
        return jmp(registers, pc, offset)
    else:
        return pc + 1

OPCODES = {
    "hlf": hlf,
    "tpl": tpl,
    "inc": inc,
    "jmp": jmp,
    "jie": jie,
    "jio": jio
}