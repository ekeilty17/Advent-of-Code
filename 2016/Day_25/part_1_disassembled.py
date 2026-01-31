from typing import Dict, Tuple, List

def disassembled(a: int, b: int, c: int, d: int, N: int=10) -> Tuple[int, int, int, int, List[int]]:
    output = []

    # chunk 1
    d = a
    c = 4

    # chunk 2
    while c != 0:
        b = 643
        while b != 0:
            d += 1
            b -= 1
        c -= 1

    # chunk 3
    #   Obviously I can't simulate an infinite loop, 
    #   so the variable N defines the number of times the `while True` runs
    # while True:
    for _ in range(N):
        a = d

        # chunk 3.1
        while a != 0:
            b = a
            a = 0
            
            # chunk 3.1.1
            c = 2
            while b != 0:
                b -= 1
                c -= 1
                if c == 0:
                    a += 1
                    c = 2

            # chunk 3.1.2
            b = 2
            while c != 0:
                b -= 1
                c -= 1

            # chunk 3.1.3
            output.append(b)
    
    return a, b, c, d, output

def efficient(a: int, b: int, c: int, d: int, N: int=10) -> Tuple[int, int, int, int, List[int]]:
    output = []
    
    # chunk 1, 2
    c = 4
    d = a + 4 * 643

    # chunk 3
    # while True:
    #   Obviously I can't simulate an infinite loop, 
    #   so the variable N defines the number of times the `while True` runs
    for _ in range(N):
        a = d

        # chunk 3.1
        while a != 0:
            b = a

            # chunk 3.1.1
            a = b // 2
            c = 1 if b % 2 else 2

            # chunk 3.1.2
            b = 2 - c
            c = 0

            # chunk 3.1.3
            output.append(b)
    
    return a, b, c, d, output

def more_efficient(a: int, b: int, c: int, d: int, N: int=10) -> Tuple[int, int, int, int, List[int]]:
    output = []
    
    # chunk 1, 2
    d = a + 4 * 643

    # chunk 3
    #   Obviously I can't simulate an infinite loop, 
    #   so the variable N defines the number of times the `while True` runs
    # while True:
    for _ in range(N):
        a = d

        # chunk 3.1
        while a != 0:
            output.append(a % 2)
            a >>= 1
    
    b = c = 0
    return a, b, c, d, output

def simulate(registers: Dict[str, int]) -> List[int]:
    # registers["a"], registers["b"], registers["c"], registers["d"], output = disassembled(**registers)
    # registers["a"], registers["b"], registers["c"], registers["d"], output = efficient(**registers)
    registers["a"], registers["b"], registers["c"], registers["d"], output = more_efficient(**registers)
    return output

if __name__ == "__main__":
    registers = {"a": 158, "b": 0, "c": 0, "d": 0}
    output = simulate(registers)
    print(output)