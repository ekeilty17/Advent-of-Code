
def _combo(operand, registers):
    if operand in [0, 1, 2, 3]:
        return operand
    if operand == 4:
        return registers["A"]
    if operand == 5:
        return registers["B"]
    if operand == 6:
        return registers["C"]
    raise ValueError(f"Expecting operand of [0, 6] inclusive, but got {operand} instead.")

def adv_func(operand, registers):
    operand = _combo(operand, registers)
    registers["A"] >>= operand
    # print(f"(0) adv: A >>= {operand}")

def bxl_func(operand, registers):
    registers["B"] ^= operand
    # print(f"(1) bxl: B ^= {operand}")

def bst_func(operand, registers):
    operand = _combo(operand, registers)
    registers["B"] = operand % 8
    # print(f"(2) bst: B = {operand} % 8")

def jnz_func(operand, registers):
    # print("(3) jnz: loop")
    if registers["A"] == 0:
        return
    return {"instruction_pointer": operand}

def bxc_func(operand, registers):
    registers["B"] ^= registers["C"]
    # print("(4) bxc: B ^= C")

def out_func(operand, registers):
    operand = _combo(operand, registers)
    # print("(5) out: output")
    return {"output": operand % 8}

def bdv_func(operand, registers):
    operand = _combo(operand, registers)
    registers["B"] = registers["A"] >> operand
    # print(f"(6) bdv: B = A >> {operand}")

def cdv_func(operand, registers):
    operand = _combo(operand, registers)
    registers["C"] = registers["A"] >> operand
    # print(f"(7) cdv: C = A >> {operand}")

OPCODES_FUNCS = [
    adv_func,
    bxl_func,
    bst_func,
    jnz_func,
    bxc_func,
    out_func,
    bdv_func,
    cdv_func,
]