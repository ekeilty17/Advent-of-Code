from utils.solve import solve

def solution(steps_per_insert: int, num_inserts: int) -> int:
    value_after_0 = 0

    i = 0
    for k in range(1, num_inserts+1):
        i = (i + steps_per_insert) % k + 1
        if i == 1:
            value_after_0 = k

    return value_after_0

if __name__ == "__main__":
    num_inserts = 50000000
    steps_per_insert = 363
    solve(solution, steps_per_insert, num_inserts)