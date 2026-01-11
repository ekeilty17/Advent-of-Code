# Day 24: It Hangs in the Balance

[Problem Link](https://adventofcode.com/2015/day/24)

## Part 1

Thinking about this problem for a bit, I convinced myself that there was no dynamic programming type of solution here as there problem does not exhibit [optimal substructure](https://en.wikipedia.org/wiki/Optimal_substructure). Furthermore, this problem is a special case of the famous [bin packing problem](https://en.wikipedia.org/wiki/Bin_packing_problem) which is [strongly NP-complete](https://en.wikipedia.org/wiki/Strong_NP-completeness). So this lead me to believe that the solution is just an efficient state-space search.

First, we can calculate the weight each group must be, which is just `sum(weights) // num_groups`. Then, I implemented a [Best-First Search](https://en.wikipedia.org/wiki/Best-first_search) implemented using a [priority queue](https://www.geeksforgeeks.org/dsa/priority-queue-set-1-introduction/) which minimized on the tuple `(group_length, entanglement)`. Due to the prioirity queue, the first solution that we find will be the optimial solution.

In this search, we are essentially trying all possible combinations of weights until we find a set which sums to `target_weight`. The result will partition our `weights` list into `group_1` and `remaining_weights`. Now, we can recurse on `remaining_weights` and do another search in order to find the optimal set of weights which sum to `target_weight`.

Since this problem is NP-complete, this solution requires a cooperative input. The first group which summed to the target weight had subsequent groups that were also able to be partitioned into the target weight. Had this problem had stricter constraints, my code probably wouldn't halt.

## Part 2

Exactly the same as part 1, exception `num_groups` is `4` instead of `3`.