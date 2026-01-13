import hashlib
from utils.solve import test, solve

def solution(door_id: str, num_zeros: int, password_length: int) -> int:
    password = ""
    n = 0
    while len(password) < password_length:
        res = hashlib.md5(f"{door_id}{n}".encode()).hexdigest()
        if res[:num_zeros] == "0" * num_zeros:
            password += res[num_zeros]
        n += 1
    
    return password

if __name__ == "__main__":
    num_zeros = 5
    password_length = 8

    example_door_id = "abc"
    expected_answer = "18f47a30"
    test(expected_answer, solution, example_door_id, num_zeros, password_length)

    door_id = "ojvtpuvg"
    solve(solution, door_id, num_zeros, password_length)