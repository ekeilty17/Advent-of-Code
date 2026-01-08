# Day 17: No Such Thing as Too Much

[Problem Link](https://adventofcode.com/2015/day/17)

## Part 1

This is a variant of the classic [coin change](https://www.geeksforgeeks.org/dsa/understanding-the-coin-change-problem-with-dynamic-programming/) dynamic programming problem, except in this case we have a finite number of coins we can use.

Let $N$ be the target number. Let $\texttt{Containers}$ be the list of containers of length $M$. Let $\texttt{Combinations}[i, n]$ be the number of ways of creating $n$ using containers $1, \ldots, i$.
The Bellman equation is as follows. 
$$
\texttt{Combinations}[i, n] = \begin{cases}
    0 &\quad\text{if } n < 0 \\[5pt]
    1 &\quad\text{if } n = 0 \\[5pt]
    \sum_{n=0}^N \texttt{Combinations}[i-1, n-\texttt{Containers}[i]] &\quad\text{otherwise}
\end{cases}
$$

Essentially, we are solving the coin change problem for each subset of coins, building up to the final solution one by one. This way, we know that we never use a container more than once, preventing any double-counting.

Note that setting $\texttt{Combinations}[i, 0] = 1$ is a nice trick to act as our base-case. Otherwise, you would have needed another condition like if $\texttt{Containers}[i] == n$, then increment the total by 1. Still works but is less elegant. Setting $\texttt{Combinations}[i, 0] = 1$ is a bit like how $0! = 1$. It's asking "how many ways can I create a total of $0$ with $0$ containers? And the answer is $1$ by doing nothing.

## Part 2 

I don't know if there's a better way of doing this other than computing every possible unique way of creating liters of eggnog. Especially because we need to return the number of ways to create the minimum length, and not just the minimum length.

So all I've done is modified my part 1 code to maintain all of the sequences of containers, rather than just the counts.

In my implementation, I set `C[0][0] = [0]` in place of setting `C[0][0] = 1`. This just lets me differentiate it from an empty list and makes the implementation cleaner. So the result of my algorithm will give `[0, 5, 5, 15]` and I can remove the leading `0` afterwards.