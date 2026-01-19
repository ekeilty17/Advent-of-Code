# Day 20: Firewall Rules

[Problem Link](https://adventofcode.com/2016/day/20)

## The Interval Set Data Structure

The key to this problem is what I'm calling the Interval Set data structure. It contains a list of non-overlapping intervals. If you add an internval, it finds all overlapping intervals and merges in order to maintain the invariant that all internvals are non-overlapping. The details of the implementation is found in `interval_set.py`.

This means, in both part 1 and part 2, we can ingest the IP ranges into the Interval Set data structure, which then merges all of the intervals into non-overlapping ranges.

## Part 1

The solution is just the upper-bound of the smallest interval in the Interval Set.

## Part 2 

Summing the lengths of all intervals in the Interval Set gives the total number of **blacklisted IPs**. Therefore, the total number of allowed IPs is the total IP range subtracted by the number of blacklisted IPs.