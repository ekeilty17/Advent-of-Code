import hashlib
from utils.solve import test, solve

def solution(door_id: str, num_zeros: int, password_length: int) -> int:
    password = [None] * password_length
    n = 0
    while not all(password):
        res = hashlib.md5(f"{door_id}{n}".encode()).hexdigest()
        if res[:num_zeros] == "0" * num_zeros:
            index = res[num_zeros]
            char = res[num_zeros+1]
            try:
                index = int(index)
                if 0 <= index < password_length and password[index] is None:
                    password[index] = char
            except:
                pass
        n += 1
    
    return "".join(password)

if __name__ == "__main__":
    num_zeros = 5
    password_length = 8

    example_door_id = "abc"
    expected_answer = "05ace8e3"
    test(expected_answer, solution, example_door_id, num_zeros, password_length)

    door_id = "ojvtpuvg"
    solve(solution, door_id, num_zeros, password_length)