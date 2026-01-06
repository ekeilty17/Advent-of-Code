from utils.test import test

def look_and_say_step(seed: str) -> str:
    if len(seed) == 1:
        return f"1{seed}"
    
    output = ""

    count = 1
    prev = seed[0]
    for char in seed[1:]:
        if char == prev:
            count += 1
            continue
        output += f"{count}{prev}"
        prev = char
        count = 1
    
    output += f"{count}{prev}"
    return output

def solution(seed: str, N: int) -> int:
    num = seed
    for _ in range(N):
        num = look_and_say_step(num)
    return len(num)

if __name__ == "__main__":
    
    example_seed = "1"
    seed = "1321131112"

    example_N = 5
    expected_answer = len("312211")
    test(expected_answer, solution, example_seed, example_N)

    N = 40
    total = solution(seed, N)
    print("Puzzle Answer:", total)