# Day 23: LAN Party

[Problem Link](https://adventofcode.com/2024/day/23)

## Background

We are back in the world of graph algorithms. Both part 1 and part 2 are asking us to find a set of computers such that all of them are connected to each other. The graph theory term for this is a [clique](https://en.wikipedia.org/wiki/Clique_(graph_theory)).

Cliques are a pretty ubiquitous data structure with many applications. It's also a famous NP-Complete problem taught in university courses. As such there is a lot of theory and research in algorithms for finding cliques in graphs. I think I once knew more on this topic, but frankly, I don't really remember much anymore. I did not do any research prior to solving part 1 and 2. 

## Part 1

This question asks us to find all cliques of size `3` in the network. The general algorithm is [finding all cliques of size k](https://www.geeksforgeeks.org/dsa/find-all-cliques-of-size-k-in-an-undirected-graph/). However, I did not use google to answer this question, so I took a brute force approach.

The first step is to process the list of edges into an adjacency list, taking care to encode each edge as undirected. See `get_adjacency_list()` for the details.

My main loop is essentially just iterating through every triplet of nodes and checking that they are all in each others adjacency list. However, we can be a bit more efficient by iterating over just the adjacent nodes instead of the full set of nodes. See the main loop in `solution()` for more details.

The last trick (also used in part 2) is we can prevent duplication by using the sorted node list as a hash, i.e.
```python
triples.add(tuple(sorted((u, v, w))))
```

Finally, just filter all `3`-cliques with only the ones containing a node starting with `t`.

## Part 2 

This is called the [Maximum Clique Problem](https://www.geeksforgeeks.org/dsa/maximal-clique-problem-recursive-solution/) which is a well-known problem. I probably once knew the theoretical solution, but again I did not use google when I initially solved this.

My solution was to build up the cliques using an induction-style approach. The induction algorithm is as follows (`clique_induction()` in the code).
1. Let `cliques_n` be the complete list of cliques with `n` nodes
2. **For each** `clique` in `cliques_n`
    1. **For each** `node` in the graph
        1. **If** `node` connects to every node in `clique`, **then** `clique U {node}` is a clique of size `n+1`

Starting with `cliques_1` which are all cliques of size 1, i.e. just the list of nodes, we can iteratively apply the above routine to compute any clique of size `k`. We terminate the algorithm once `cliques_n` is an empty list. Then the previous iteration is the set of maximum cliques.

My only complaint with this algorithm is that it takes about 1 minute to run. I may do some research and write a `part_2_alt.py` with a more efficient algorithm. However, this problem is NP-Complete, so it can only be so efficient.