# Day 3: Lobby

[Problem Link](https://adventofcode.com/2025/day/3)

## Part 1

There are essentially 2 cases.

#### Case 1: Max-Valued Digit is the Last Digit

If the max-valued digit appears last in the bank, then we preprend the second max digit, and that will be our _maximum joltage_.

```
115111111119 --> 59
```

#### Case 2: Otherwise

Since the max-valued digita is not the last in the bank, then it will necessarily be our first digit. Therefore, to maximize our joltage, we don't want to pick any digits to the left of the max digit. Thus, we pick the maximum digit to the right, and append to get our _maximum joltage_.

```
88888911115111 --> XXXXX911115111 --> 95
```

## Part 2

I implemented a dynamic programming solution which I am reasonably happy with.

At a high level, the idea is the following.
1. Iterate from high-valued batteries to lowest, i.e. iterate from `9, 8, ..., 1, 0`. Let's suppose we are using the digit `9`
2. There will be some number of `9`'s in the string. Consider the **left-most** `9`. This digit is guaranteed to be included in the maximized joltage.
3. Now we can partition the bank at this digit. Everything to the left we no longer care about (similar to part 1). Everything to the right we recurse.

Let's do an example where we want to take the maximum `4` digits in sequence from the number: `1819188119`

```
1819188119
181(9)188119              <-- left most 9, will be in the final solution
181(9)[188119]            <-- recurse on all digits after, will select 3 more digits
181(9)[18811(9)]          <-- only 9, will be in the final solution
181(9)[1(8)811(9)]        <-- move onto 8s, left-most 8 will be in the final solution
181(9)[1(8)[811(9)]]      <-- recurse on all digits after, will select 1 more digit
181(9)[1(8)[811(9)]]      <-- no 9s left
181(9)[1(8)[(8)11(9)]]    <-- move onto 8s, only 8 will be in the final solution
181(9)1(8)(8)11(9)        <-- return from all recursion
9889                      <-- final answer
```

Essentially, we are guaranteed to reduce the problem by `1` in each recursion. For this problem, this algorithm is very efficient because the size of the banks are long, but the number of digits we need to extract is small (only `12`). And in each iteration, we are reducing the number of digits we need to extract by `1`, so it will in the worst case it will take `12` steps to complete.
