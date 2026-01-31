import numpy as np
from numpy.typing import NDArray

from utils.solve import solve

def generate_spiral(k: int) -> NDArray[np.int_]:
    """
    Generates the spiral with k layers
    k == 0 --> [[1]]
    k == 1 --> [[5, 4, 3],
                [6, 1, 2],
                [7, 8, 9]]
    """

    spiral = np.array([[1]])

    for _ in range(k):
        n = spiral.shape[0]
        upper = spiral[-1, -1]

        # right
        line = np.arange(upper+1, upper+1+n)[::-1]
        spiral = np.column_stack((spiral, line))
        upper += n

        # top
        line = np.arange(upper+1, upper+1+n+1)[::-1]
        spiral = np.vstack((line, spiral))
        upper += n+1

        # left
        line = np.arange(upper+1, upper+1+n+1)
        spiral = np.column_stack((line, spiral))
        upper += n+1

        # bottom
        line = np.arange(upper+1, upper+1+n+2)
        spiral = np.vstack((spiral, line))
        upper += n+2

    return spiral

def brute_force(N: int) -> int:
    k = int(np.ceil( (np.sqrt(N)-1)/2 ))
    spiral = generate_spiral(k)
    # print(spiral)

    x1, y1 = list(zip(*np.where(spiral == 1)))[0]
    xN, yN = list(zip(*np.where(spiral == N)))[0]

    return abs(xN - x1) + abs(yN - y1)

def efficient(N: int) -> int:
    k = int(np.ceil( (np.sqrt(N)-1)/2 ))
    bottom_right = (2*k+1)**2
    
    offset = (bottom_right - N) // (2*k)
    upper_corner = bottom_right - offset*2*k
    lower_corner = bottom_right - (offset+1)*2*k
    # lower_corner < N <= upper_corner
    
    middle = (upper_corner + lower_corner) // 2
    return k + abs(N - middle)

def solution(N: int) -> int:
    # return brute_force(N)
    return efficient(N)

if __name__ == "__main__":
    N = 312051
    solve(solution, N)