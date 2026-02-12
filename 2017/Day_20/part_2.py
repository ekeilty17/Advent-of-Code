from pathlib import Path
from typing import List, Tuple, Set, Dict
import math

from Day_20.const import DAY, INPUT_FILE_NAME
from Day_20.const import EXAMPLE_INPUT_FILE_NAME_PART_2 as EXAMPLE_INPUT_FILE_NAME
from Day_20.part_1 import Position, Velocity, Acceleration
from Day_20.load_input import load_input
from utils.solve import test, solve

def integer_quadratic_programming(a: int, b: int, c: int) -> Tuple[int | None, int | None]:
    """
    integer solutions for
        ax^2 + bx + c = 0
    """
    def is_square(n: int | float) -> bool:
        if n < 0:
            return False
        r = math.isqrt(int(n))
        return r * r == n

    discriminant_squared = b**2 - 4*a*c
    if not is_square(discriminant_squared):
        return None, None
    
    if discriminant_squared == 0:
        if b % (2*a) == 0:
            return -b // (2*a), None
        return None, None
    
    discriminant = math.isqrt(discriminant_squared)
    x1 = (-b + discriminant) // (2*a) if (-b + discriminant) % (2*a) == 0 else None
    x2 = (-b - discriminant) // (2*a) if (-b - discriminant) % (2*a) == 0 else None
    return x1, x2

def integer_linear_programming(b: int, c: int) -> int | None:
    """
    integer solutions for
        bx + c = 0
    """
    if b == 0:
        return None
    return -c // b if c % b == 0 else None
    
def get_all_collisions(particle_properties: List[Tuple[Position, Velocity, Acceleration]]) -> Dict[int, Set[int]]:

    def add_collision(collisions: Dict[int, Set[int]], t: int, i: int, j: int):
        if t is None:
            return
        if t < 0:
            return
        if t not in collisions:
            collisions[t] = {}
        
        if i not in collisions[t]:
            collisions[t][i] = set([])
        if j not in collisions[t]:
            collisions[t][j] = set([])
        
        collisions[t][i].add(j)
        collisions[t][j].add(i)

    def get_particle_pair_collisions(dP0: Position, dV0: Velocity, dA: Acceleration) -> Set[int]:
        pair_collisions_by_dimension = []
        
        for dp0, dv0, da in zip(dP0, dV0, dA):
            dimension_collisions = []
            if dp0 == dv0 == da == 0:
                continue

            if da == 0:
                t1 = integer_linear_programming(dv0, dp0)
                dimension_collisions.append(t1)
            else:
                t1, t2 = integer_quadratic_programming(da, da + 2*dv0, 2*dp0)
                dimension_collisions.append(t1)
                dimension_collisions.append(t2)
            
            dimension_collisions = set([t for t in dimension_collisions if t is not None])
            pair_collisions_by_dimension.append(dimension_collisions)

        return set.intersection(*pair_collisions_by_dimension)


    collisions = {}
    for i in range(len(particle_properties)):
        P0_1, V0_1, A_1 = particle_properties[i]
        for j in range(i+1, len(particle_properties)):
            P0_2, V0_2, A_2 = particle_properties[j]

            dP0 = tuple([p0_2 - p0_1 for p0_1, p0_2 in zip(P0_1, P0_2)])
            dV0 = tuple([v0_2 - v0_1 for v0_1, v0_2 in zip(V0_1, V0_2)])
            dA = tuple([a_2 - a_1 for a_1, a_2 in zip(A_1, A_2)])

            pair_collisions = get_particle_pair_collisions(dP0, dV0, dA)
            
            for t in pair_collisions:
                add_collision(collisions, t, i, j)
    
    return collisions

def compute_destroyed_particles(collisions_by_time: Dict[int, Set[int]]) -> Set[int]:
    destroyed = set([])
    for t, collisions_by_partical in sorted(collisions_by_time.items()):
        
        destroy_at_t = set([])
        for p, p_collisions in collisions_by_partical.items():
            if p not in destroyed:
                destroy_at_t.update(p_collisions)
        
        destroyed.update(destroy_at_t)
    
    return destroyed

def solution(particle_properties: List[Tuple[Position, Velocity, Acceleration]]) -> int:
    collisions_by_time = get_all_collisions(particle_properties)
    destroyed = compute_destroyed_particles(collisions_by_time)
    return len(particle_properties) - len(destroyed)

if __name__ == "__main__":
    example_particle_properties = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 1
    test(expected_answer, solution, example_particle_properties)

    particle_properties = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, particle_properties)