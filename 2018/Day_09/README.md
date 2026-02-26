# Day 9: Marble Mania

[Problem Link](https://adventofcode.com/2018/day/9)

## Part 1

For part 1, I coded the problem exactly as described by the instructions. I used a standard Python list `played_marbles` encoding the order of the marbles, and maintained a `circle` pointer indicating the current position of the circle in the marble list. I used `.insert()` and `.pop()` to add/remove marbles as arbitrary indices inside of the `played_marbles` list.

This approach was fine for part 1, but it is way too slow to solve part 2. The issue is that inserting and removing from arbitrary indices is not something arrays are good at. The part 1 solution is constantly re-sizing and shifting element around, which is very slow once the array size is sufficiently large.

## Part 2 

The trick to solving to use a [Linked List](https://www.geeksforgeeks.org/dsa/linked-list-data-structure/) rather than an [array](https://en.wikipedia.org/wiki/Array_(data_structure)). To insert/remove from a linked list, we just have to update a few pointer references. This is much much faster than the same operation on an array, which requires re-sizing and shifting of elements.

The Python standard library has the [deque](https://www.geeksforgeeks.org/python/deque-in-python/) library which is a [Double-Ended Queue](https://en.wikipedia.org/wiki/Double-ended_queue), which is very efficient for the exact operations we require.

Now, instead of maintaining the `circle` pointer, we can just call `deque.rotate()` and move the circle to the root of the queue. Then we can call `deque.append()` and `deque.pop()` to add/remove from the end of the queue when necessary. See the code in `part_2.py` for the implementation.

## Part 2 Alternative Solution

It felt a bit like cheating to just use an external library to solve the problem. So I also implemented a [Circular Doubly Linked List](https://www.geeksforgeeks.org/dsa/introduction-to-circular-doubly-linked-list/) by hand. So the nodes form a loop with `prev` and `next` pointers. Then I have a `root` pointer which points at the start of the list. This made implementing the `.rotate()` function very easy. See the implementation in `part_2_alt.py`.

Probably because `deque` is using C on the backend, it's about 1 order of magnitude faster than my hand-solution. But asymptotically I think they are equivalent.