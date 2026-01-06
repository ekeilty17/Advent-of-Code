# Day 13: Knights of the Dinner Table

[Problem Link](https://adventofcode.com/2015/day/13)

## Part 1

This is very similar to Day 9, except we are looking for the optimal [Hamiltonian cycle](https://www.geeksforgeeks.org/dsa/hamiltonian-cycle/). The tricky part of the problem is how to quickly iterate over every possible Hamiltonian cycle.

Using the small example, we have people `people = {"Alice", "Bob", "Carol", "David"}`. If we do the naive thing and call `itertools.permutations(people)`, then we will have a lot of repeats. For example,

```python
("Alice", "Bob", "Carol", "David")
("Bob", "Carol", "David", "Alice")
("Carol", "David", "Alice", "Bob")
("David", "Alice", "Bob", "Carol")
("David", "Carol", "Bob", "Alice")
("Carol", "Bob", "Alice", "David")
("Bob", "Alice", "David", "Carol")
("Alice", "David", "Carol", "Bob")
```

are all the exact same cycle. Since we have `4` people, we have `2 x 4 = 8` duplicates per unique cycle. In the challenge input where we have `8` people, we would have `2 x 8 = 16` duplicates per unique cycle.

In order to reduce the number of redundant cycle, I do the following. First, remove one person from the set of people. Suppose this is `Alice`. Then, compute all permutations of the remaining people. 

```python
("Bob", "Carol", "David")
("Carol", "David", "Bob")
("David", "Bob", "Carol")
("David", "Carol", "Bob")
("Carol", "Bob", "David")
("Bob", "David", "Carol")
```

Then, append `Alice` to the front of each.

```python
("Alice", "Bob", "Carol", "David")
("Alice", "Carol", "David", "Bob")
("Alice", "David", "Bob", "Carol")
("Alice", "David", "Carol", "Bob")
("Alice", "Carol", "Bob", "David")
("Alice", "Bob", "David", "Carol")
```

Now, for each unique cycle, we have 1 extra duplicate, which is that cycle in reverse order.

Finally, I call `compute_total_happiness()` on each of these cycles, and take the maximum.

## Part 2 

This is exactly the same as part 1, except I just need to add an edge between `"Me"` and every other person with a happiness of `0`.