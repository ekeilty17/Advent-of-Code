# Day 21: Scrambled Letters and Hash

[Problem Link](https://adventofcode.com/2016/day/21)

## Part 1

The solution is just to read the problem the problem carefully and implement each of the operations as described. In `load_input.py`, I parse the operation strings into dictionaries with the operation type and parameters. Then in `operations.py` I write the logic of each operation, with a map of operation type to operation function in the variable `OPERATIONS`.

## Part 2 

In this part we have to inverse each of the operations. All but one are trivial to invert. The `rotate by letter` operation is a bit complicated due to two factors. 1) modular arthimetic means we've lost some information, 2) indices `>= 4` add an additional step.

The trick is to think about where the input index gets mapped to in the normal `rotate by letter` operation.

$$
i' = \begin{cases}
    i + (i + 1) &\quad\text{if } i < 4 \\
    i + (i + 2) &\quad\text{if } i \geq 4
\end{cases}
$$

Notice that $i'$ is even if and only if $i \geq 4$. So this let's us identify the two cases. What my code does to invert the operation is I just iterately decrement $i'$ until I find an $i$ that satifies all conditions.