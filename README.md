# Advent of Code

This is a repository containing my solutions to the annual [Advent of Code](https://adventofcode.com/about). I think these are great problems to exercise the algorithms and data structures skills.

I was a bit late to the party and only heard about this in 2025. So when I'm in the mood I go back and do some of the problems from past years.

## Repository Structure

This repository is organized such that each year is self-contained. In order to run any particular year, you should `cd` into that year, i.e.
```
cd 2025/
```
See the `README.md` instructions in each year's folder for more details.

## My Philosophy

The vibe I get from reddit and reading the solution of others is their priorities are in the following order

1. Find any solution that terminates
2. Find the fastest possible solution
3. Find a solution in the least amount of code

By constrast, my priorities are the following
1. Find any solution that terminates
2. Find a solution that is asympototically efficient and utilizes a well-known algorithm or approach
3. Write the solution such that it is easily understandable

I almost never heard about optimizing for memory, which I mostly agree with. If you have a fast run-time you necessarily are efficient enough in your memory.

The difference between my priority 2. and the former priority 2. is subtle but important. When trying to find the _fastest possible solution_, you will overfit to the specifics of the problem. For example, when sorting a small list of numbers, insertion sort is actually much more efficient than quicksort. But it is much slower theoretically (`O(n^2)` vs `O(n log n)`). In other words, I am not solution-oriented, I am method-oriented. I don't just want to find a fast solution, I want to identify the right method.

I also take issue with priority 3. When you condense your code into the least amount of characters, it makes it utterly unreadable. Most of the time when I read the solutions of others, I have no clue what's going on. I actually want to do the opposite. I will happily write more lines of code if it means that it's more readable.
