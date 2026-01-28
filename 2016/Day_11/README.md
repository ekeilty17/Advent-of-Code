# Day 11: Radioisotope Thermoelectric Generators

[Problem Link](https://adventofcode.com/2016/day/11)

## Important Constraints

The description of this problem is long, but the following are two relevant passages.

> if a chip is ever left in the same area as another RTG, and it's not connected to its own RTG, the chip will be fried

> there is an elevator that can move between the four floors. Its capacity rating means it can carry at most yourself and two RTGs or microchips in any combination

In summary
- Microchips cannot be left alone with other generators. It must either be only with other microchips or accompanied by its corresponding generators.
- The elevator can take either 1 or 2 of any device at a time

## Part 1 and Part 2

Both part 1 and part 2 are essentially the same problem, except part 2 has a larger search space. Both require a state-space search which can be accomplished either using a standard [Breadth-First Search](https://en.wikipedia.org/wiki/Breadth-first_search) (BFS) or with [A*](https://en.wikipedia.org/wiki/A*_search_algorithm). The key to the problem; however, is the reduction of the state-space.

### State Space Search

In `part_1.py` I implement BFS. In `part_2.py` I implement A*. However, both give similar run-times with A* being only slightly more efficient.

In both implementations, given a particular configuration we iterate over every device and every pair of devices. Then we try moving them both up one floor and down one floor. The logic for moving devices is implemented in `move_devices()` in `part_1.py`. Then we need to make sure the move didn't fry a microchip anywhere. This logic is implemented in `is_floor_safe()` in `part_1.py`.

### Reducing the State Space

The key to solving both problems in under 2 seconds is to reduce the state-space. To do this, we have to think about what defines a **unique state**. 

In this section, I will use `M` to indicate microchips and `G` to indicate generators. Numbers will be used to indicate the different _types_. For example, `(M1, G1)` are one `(microchip, generator)` pair, and `(M2, G2)` are another `(microchip, generator)` pair.

The first observation is that the order of devices on each floor does not matter. For example, the following configurations are equivalent.

```
|F4      M2 G2 |        |F4      G2 M2 |
|F3 E    M1 G1 |        |F3 E    G1 M1 |
|F2            |        |F2            |
|F1            |        |F1            |
```

The second and more important observation is that each `(microchip, generator)` are indistinguishable from each other. For example, the following configurations are equivalent.

```
|F4      M2 G2 |        |F4      M1 G1 |
|F3 E    M1 G1 |        |F3 E    M2 G2 |
|F2            |        |F2            |
|F1            |        |F1            |
```

So how do we encode the problem such that all of these configurations map to the same **state**? The key is to consider the floors of each `(microchip, generator)` pair. In this case, this would be

```python
left_positions = {
    1: (3, 3),
    2: (4, 4)
}

right_positions = {
    1: (4, 4),
    2: (3, 3)
}
```

Now, we just sort the floor number tuples. So in each case, this would become

```python
pairs = [(3, 3), (4, 4)]
```

Now, the full state is 
```python
state = (elevator_position, pairs)
```

This implementation is found in the function `get_state()` in `part_1.py`.


### The Heuristic Function in A*

As a quick recap of A*. It is a heuristic search prioritized by the function 

$$
f(n) = g(n) + h(n)
$$

where $g(n)$ is the cost of getting to the current state and $h(n)$ is a heuristic function which estimates the cost of getting to the target state. It's important that $h(n)$ is **admissible** which means 

$$
h(x) \leq d(x, y) + h(y)
$$

In plain English, this means $h(n)$ is an **under-estimate** of the actual cost of getting to the target state. This guarantees that the first solution the algorithm finds is an optimal solution.

In this problem $g(n)$ is just the current depth of the search. $h(n)$ is a little more complicated. It is a lower-bound on the number of elevator moves required to get all of the items to the target floor. 

Here is one possible function.

$$
h(n) = \left \lfloor \frac{1}{2} \sum_{\text{floor}} (\text{distance to target floor}) \cdot (\text{number of devices on floor}) \right \rfloor
$$

This function is counting the number of steps required if we moved 2 devices towards the target floor in each iteration. While this is admissible, it greatly under-estimates the number of steps required.

What we failed to consider is if there are more than 2 items on a floor, then the elevator has to go up to the target floor and then come back to the original floor to retrieve the other items. Thus, we get a much better lower-bound of

$$
h(n) = \left \lfloor \frac{1}{2} \sum_{\text{floor}} (\text{distance to target floor}) \cdot [ (\text{number of devices on floor}) + (\text{number of devices on floor} - 1)]\right \rfloor
$$