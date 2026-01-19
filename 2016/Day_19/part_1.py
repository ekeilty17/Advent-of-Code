from utils.solve import test, solve

def simulate(num_elves: int) -> int:
    elves = [n+1 for n in range(num_elves)]

    while len(elves) > 1:
        # print(elves)
        is_odd = len(elves) % 2
        elves = elves[::2]
        if is_odd:
            elves = elves[1:]
    
    # print(elves)
    return elves[0]

def compute(num_elves: int) -> int:
    if num_elves <= 0:
        return 0
    if num_elves == 1:
        return 1
    
    mask = (1 << (num_elves.bit_length()-1))-1
    return 2 * (num_elves & mask) + 1

def solution(num_elves: int) -> int:
    # return simulate(num_elves)
    return compute(num_elves)

if __name__ == "__main__":
    example_num_elves = 5
    expected_answer = 3
    test(expected_answer, solution, example_num_elves)

    num_elves = 3017957
    solve(solution, num_elves)