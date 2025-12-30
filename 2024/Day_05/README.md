# Day 5: Print Queue

[Problem Link](https://adventofcode.com/2024/day/5)

It took me a bit to understand the interpretation of this problem. Upon reading it, I knew that the author had a specific graph algorithm in mind, and retrofitted a problem for that algorithm, and I believe I found the intended solution.

## Background

### The DAG and Topological Ordering

A [directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph) (DAG) is a graph where every edge has a direction from one vertex to another, and there are no cycles. A key property of DAG's is that they can be [topologically ordered](https://en.wikipedia.org/wiki/Topological_sorting), i.e. you can order the vertices such that edges always flow from left to right.

For example, for the page numnbers `29`, `47`, `53`, `61`, and `75`, the ordering rules give the following directed graph.

```      
         +------------------------+
         |+--------------+        |
         ||       +------+-------+|
         ||       |      V       VV
(75) -> (47) -> (61) -> (53) -> (29)
|||              ^       ^       ^
||+--------------+       |       |
|+-----------------------+       |
+--------------------------------+
```

Thus, as we can see, `[75, 47, 61, 53, 29]` is the **topological ordering** of this subgraph.

To solve this problem, I found it easier to write an abstract graph class, which is found in `graph.py`.

## Part 1

The important sentence in the instructions are

> The notation X|Y means that if both page number X and page number Y are to be produced as part of an update, page number X must be printed at some point before page number Y.

This is essentially describing a topological order of page numbers. Now, the full graph is not a DAG, it contains many cycles. However, if we only consider the subgraph of page numbers, then we get a bunch of subDAGs.

Thus, the algorithm for part 1 is as follows

1. Process the ordering rules into a graph `G`
2. Let `S` be the sequence of page numbers to be printed in order
3. Let `subG` be the subgraph by considering only the nodes and edges from `S`
4. Let `T` be the topological order of `subG`
5. If `S == T`, then `S` is valid

Then we iterate over all page sequences `S` and sum accordingly.

## Part 2 

Part 2 is almost identical to part 1, except the total is different. Instead of taking the median of `S` if `S == T`, we take the median of `T` if `S != T`.