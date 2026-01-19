from utils.solve import test, solve

def to_base3(n: int) -> str:
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        n, r = divmod(n, 3)
        digits.append(str(r))
    return "".join(reversed(digits))

def simulate(num_elves: int) -> int:
    elves = [n+1 for n in range(num_elves)]

    i = 0
    while len(elves) > 1:
        m = len(elves) // 2
        j = (i+m)%len(elves)
        print(elves, elves[j])
        
        del elves[j]
        if j > i:
            i += 1
        i %= len(elves)
    
    print(elves)
    return elves[0]

def compute(num_elves: int) -> int:
    if num_elves <= 0:
        return 0
    if num_elves == 1 or num_elves == 2:
        return 1
    
    t = to_base3(num_elves)
    MST = int(t[0], 3)      # Most Significant Trit = t // power_of_3_lower_bound
    tail = int(t[1:], 3)    # = (t - MST * power_of_3_lower_bound)
    power_of_3_lower_bound = 3**(len(t)-1)
    
    if num_elves == power_of_3_lower_bound:
        return num_elves
    
    return (MST - 1) * power_of_3_lower_bound + MST * tail
    

def solution(num_elves: int) -> int:
    # return simulate(num_elves)
    return compute(num_elves)

if __name__ == "__main__":
    example_num_elves = 5
    expected_answer = 2
    test(expected_answer, solution, example_num_elves)

    num_elves = 3017957
    solve(solution, num_elves)