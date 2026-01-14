from utils.solve import test, solve

def dragon(s: str, checksum_length: int) -> str:
    
    while len(s) < checksum_length:
        a = s
        b = s.translate(str.maketrans("01", "10"))[::-1]
        s = f"{a}0{b}"
    
    return s

def checksum(s: str, checksum_length: int) -> str:
    s = s[:checksum_length]
    while len(s) % 2 == 0:
        s = "".join(["1" if s[i] == s[i+1] else "0" for i in range(0, len(s)-1, 2)])

    return s

def solution(init_state: str, checksum_length: int) -> str:
    s = init_state
    s = dragon(s, checksum_length)
    s = checksum(s, checksum_length)
    return s

if __name__ == "__main__":
    example_init_state = "10000"
    example_checksum_length = 20
    expected_answer = "01100"
    test(expected_answer, solution, example_init_state, example_checksum_length)

    init_state = "01111010110010011"
    checksum_length = 272
    solve(solution, init_state, checksum_length)