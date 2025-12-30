# Day 6: Guard Gallivant

[Problem Link](https://adventofcode.com/2024/day/6)

## Part 1

This is a puzzle where I think you just have to simulate it. I don't think there is any better algorithm than just simulating the guard's patrolling path. But I'm happy to be proven wrong.

In my solution, there were 2 complicated parts of this code. First, is writing the `update_guard_position()` function. Just a bit tedious to get all of the indices correct. Second are the break conditions of the while loop inside `compute_patrolled()`. There are two things you have to check for
1. If the guard's current position is on the edge of the map. This means they have left the mapped area.
2. If the guard has started looping. The easiest way to check for this is the combination of the guard's orientation (i.e. `^`, `>`, `v`, or `<`) and the guard's position. This combination I call the guard's _state_. If the state ever repeats, then the gaurd is looping and we need to break.

The solution to part 1 is to call this `compute_patrolled()` which returns a boolean array of all of the positions that guard patrolled. Then just return the count.

## Part 2 

Again, I don't think there is anything much more clever than just brute-force simulating how the gaurd's path changes with each new obstruction.

One key insight is to first compute the natural patrolling path, i.e. what we computed in part 1. Then we only have to check obstruction positions at the positions the guard would naturally patrol. If we were to put a new obstruction at a position the guard does not natrually patrol, then their path would not be altered.

So my solution to part 2 is to iterate through all patrolled positions, compute the new patrolled path, and check if the guard leaves or loops. Then just return the number of new obstructions which cause the guard to loop.
