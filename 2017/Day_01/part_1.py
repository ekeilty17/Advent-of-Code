from pathlib import Path

from Day_01.const import DAY, INPUT_FILE_NAME
from Day_01.load_input import load_input
from utils.solve import test, solve

def solution(captcha: str) -> str:
    N = len(captcha)
    total = 0
    for i in range(N):
        x, y = captcha[i], captcha[(i+1) % N]
        if x == y:
            total += int(x)
    
    return total

if __name__ == "__main__":
    example_1_captcha = "112"
    expected_1_answer = 1
    test(expected_1_answer, solution, example_1_captcha)

    example_2_captcha = "1111"
    expected_2_answer = 4
    test(expected_2_answer, solution, example_2_captcha)

    example_3_captcha = "1234"
    expected_3_answer = 0
    test(expected_3_answer, solution, example_3_captcha)

    example_4_captcha = "91212129"
    expected_4_answer = 9
    test(expected_4_answer, solution, example_4_captcha)

    captcha = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, captcha)