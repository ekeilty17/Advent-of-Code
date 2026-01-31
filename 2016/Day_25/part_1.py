from utils.solve import solve

def solution() -> int:
    d_lower_bound = 4 * 643
    
    d = 0
    while d < d_lower_bound:
        d <<= 2
        d += 2
    
    a = d - d_lower_bound
    return a

if __name__ == "__main__":
    solve(solution)