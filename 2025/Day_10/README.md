# Day 10: Factory

[Problem Link](https://adventofcode.com/2025/day/10)

## Data Loading

This input was a weird one to parse. The easiest way I found was to use [regex](https://en.wikipedia.org/wiki/Regular_expression). I used the following pattern

```
(\[.+\]) (\(.+\))+ (\{.+\})
```

Group 1 gives the light indicators, group 2 gives the button wiring schematics, and group 3 gives the joltage requirements.

## Part 1

I implemented this using a simple [Breadth-First Search](https://en.wikipedia.org/wiki/Breadth-first_search) (BFS). Since this is just a tree search, I didn't have to bother with queues and while loops. I could just do a level traversal. It looks something like
1. Let `L` be the list of all nodes at depth `d`
2. **Initialize** `L' = []`
3. **For each** node at the current depth
    1. Get all possible next states based on the button wiring schematics
    2. Add each new state to `L'` 
5. `L'` is now the list of all nodes at depth `d+1`
6. **Recurse** on `L'` until a solution a found
7. **Return** the depth of the solution state

Essentially I'm searching all possible combinations of button presses until I reach the solution state. Since I am using BFS, I know that the first solution I find will be an optimal solution. The **depth** of my BFS represents the number of button presses.

## Part 2 

### State Space Search

I tried implementing using the same method as part 1, however it's too slow. I tried adding intelligent pruning, but it was still too slow. From others I heard that even implementing a [bidirection BFS](https://www.geeksforgeeks.org/dsa/bidirectional-search/) is too slow. So it seems like this is not the correct approach.

### Integer Programming

We can reframe the problem as follows. Each list of button indices can be converted as follows

```
(3)                [[0, 0, 0, 1],
(1,3)               [0, 1, 0, 1],
(2)                 [0, 0, 1, 0],
(2,3)       -->     [0, 0, 1, 1],
(0,2)               [1, 0, 1, 0],
(0,1)               [1, 1, 0, 0]]
```

Now, the problem boils down to the optimization problem 
```
min sum(x) subject to Ax = b
```

`A` is a matrix of indexes, representing which joltages are incremented when the button is clicked. `x` is the vector of how many times each button was clicked (what we are trying to optimize). `b` is the vector of required joltages.

I didn't really feel like writing my own linear programming solver. So I just used `milp` from `scipy.optimize`. One nuance is that the constraint `Ax = b` has to be specified as two constraints: `Ax >= b` and `Ax <= b`. This is actually a pretty standard trick in optimization.
