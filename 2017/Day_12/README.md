# Day 12: Digital Plumber

[Problem Link](https://adventofcode.com/2017/day/12)

## Part 1

The puzzle input is an [Undirected Graph](https://www.geeksforgeeks.org/dsa/what-is-unidrected-graph-undirected-graph-meaning/). The question is asking to the [Connected Component](https://en.wikipedia.org/wiki/Component_(graph_theory)) containing the program ID `0`.

To do this, we implement a simple [Depth-First Search](https://en.wikipedia.org/wiki/Depth-first_search) (DFS) starting at program ID `0`. The puzzle input tells us which nodes are connected to which other nodes in the graph. All the nodes that were visited in the DFS is the **component containing program `0`**.

## Part 2 

Part 2 asks us to find **all connected components** in the input graph. This is done by iterating over every node in the graph. If that node is already part of a connected component, then skip. Otherwise, do a DFS starting at that node.