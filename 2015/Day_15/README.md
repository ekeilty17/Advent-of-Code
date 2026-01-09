# Day 15: Science for Hungry People

[Problem Link](https://adventofcode.com/2015/day/15)

## Part 1

I took a brute force approach. Since we know that the total number of teaspoons is exactly `100`, I just get all possible combinations of numbers which sum to `100`. Let $\boldsymbol{x}$ be the teaspoon amounts per ingredient. Let $P$ be the matrix of properties. Then the total score is

$$\boldsymbol{b} := P \boldsymbol{x}$$
$$\texttt{score}(\boldsymbol{x}; P) = \prod_i \max(0, b_i)$$

And we just find the maximum score.

## Part 2 

Again, I took a brute force approach, which means I did exactly the same thing as part 1, which the additional contraint that the calories sum to `500`. It's just an additional `if`-statement when iterating over all valid values of $\boldsymbol{x}$. 

I definitely want to come back to this problem. I feel there is some elegant math learking that would make the solution very fast to compute. Especially in part 2.
