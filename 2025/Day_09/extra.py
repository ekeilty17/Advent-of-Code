from typing import List, Tuple

# I think this aglorithm works, I just never used it in the final solution
# but it's kind of cool I think

def is_point_inside_polygon(vertices: List[Tuple[int, int]], coord: Tuple[int, int]) -> bool:
    x, y = coord

    intersections = 0
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]
        # In this problem, either x1 == x2 or y1 == y2

        # edge case, we are at one of the points
        if x == x1 and y == y1:
            return True

        # edge case, we are straight on a boundary line
        if y == y1 == y2:
            if (x1 <= x <= x2) or (x2 <= x <= x1):
                return True
            # want to continue because we don't want to count this case
            continue
        if x == x1 == x2:
            if (y1 <= y <= y2) or (y2 <= y <= y1):
                return True

        # I am sending a horizontal ray in one direction (right) and counting the intersections
        # ..............
        # .......#XXX#..
        # ...O---X---X--        <-- 2 intersections ==> outside
        # ..#XXXX#...X..
        # ..X...O----X--        <-- 1 intersectin ==> inside
        # ..#XXXXXX#.X..
        # .........X.X..
        # .........#X#..
        # ...O----------        <-- 0 intersections ==> outside

        # Summing all intersections, an odd number of crossings ==> point inside
        # an even number of crossings ==> point outside

        is_within_vertical_range = (y1 <= y <= y2) or (y2 <= y <= y1)
        horizontal_ray_intersects = (x <= x1)
        # print(x1, y1, x2, y2, is_within_vertical_range and horizontal_ray_intersects)
        if is_within_vertical_range and horizontal_ray_intersects:
            intersections += 1

    is_inside = intersections % 2 == 1
    return is_inside