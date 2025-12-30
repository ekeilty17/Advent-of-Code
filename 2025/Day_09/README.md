# Day 9: Movie Theater

[Problem Link](https://adventofcode.com/2025/day/9)

## Part 1

Iterate through every pair of locations and compute the area of the corresponding rectangle. Return the maximum area. 

## Part 2

If we imagine that the locations as vertices, then connecting each location in sequence will create a **polygon**. Part 2 adds an additional requirement that our rectangles must be fully inside the given polygon to be included in the max area calculation.

Conceptually this is exactly the same as part 1, but with an additional filter. So the problem reduces down to finding an efficient enough algorithm to determine when a rectangle is fully contained inside the given polygon.

### Brute Force is Too Slow

It's always good to try to brute force way first. To me, this means constructing a bitmap of polygon and a bitmap of the rectangle, and using a bitwise `AND` to determine if they fully intersect, i.e.

```
if (rectangle & polygon == rectangle) then (rectangle is fully contained by the polygon)
```

Computing the boundary of the polygon is easy, we just connect up the vertices in sequence. Computing the interior is more complicated. I used [Ray-Casting Algorithm](https://rosettacode.org/wiki/Ray-casting_algorithm) to find all of the interior points.

The problem is that this is too slow. Constructing the boundary and interior of the polygon is actually not too bad. But it turns out doing `rectangle & polygon` for all of the rectangles was really slow. This was surprising to me.

### My Final Solution

There is one things we did not really take advantage of in the brute force solution. That all edges of the polygon are either fully vertical or fully horizontal.

I reframed the problem as, when do the rectangle and polygon intersect? Since we are always dealing with vertical and horizontal lines, the solution is actually very short to code. All the edge cases somehow just reduce into a few equations.

Suppose we are considering a horizontal edge in the polygon intersecting a rectangle.
```
    +--------+
    |        |
----+-----   |
    +--------+
```

Let `R` be the rectangle and its interior. Let `E` by an edge of the polygon. Let these be defined by
```
R = {(x, y): x1 <= x <= x2 and y1 <= y <= y2}
E = {(x, y): X1 <= x <= X2 and y = Y}
```

From a vertical perspective, we require that

```
y1 < Y < y2
```
Otherwise, the polygon edge would be above or below the rectangle and could not intersect.

From a horizontal perspective, if the edge does not intersect the rectangle, then this means it's either entirely to the left or entirely to the right of the rectangle. In other words, the condition for an intersection is
```
not ((X2 < x1) or (x2 < X1))
```

This can be simplified to
```
max(x1, X1) < min(x2, X2)
```

The same parallel logic can be applied to vertical edges.

Notice that I have been using `<` instead of `<=`. Honestly, this came from trial and error.
