from utils.solve import test, solve

def solution(num_presents: int) -> int:
    N = num_presents
    presents = [0] * (N+1)

    for f in range(1, N+1):
        for k in range(1, 51):
            if k*f > N:
                break 
            presents[k*f] += 11 * f

        if presents[f] >= N:
            return f

if __name__ == "__main__":
    example_num_presents = 100
    expected_answer = 6
    test(expected_answer, solution, example_num_presents)

    num_presents = 36000000
    solve(solution, num_presents)