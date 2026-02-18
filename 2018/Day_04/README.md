# Day 4: Repose Record

[Problem Link](https://adventofcode.com/2018/day/4)

## Unified Data Structure

There are probably many different solutions, but I was looking for a unified data structure that could solve both parts. I believe the following was the intended solution.

Using the example given in the problem
```
Date   ID   Minute
            000000000011111111112222222222333333333344444444445555555555
            012345678901234567890123456789012345678901234567890123456789
11-01  #10  .....####################.....#########################.....
11-02  #99  ........................................##########..........
11-03  #10  ........................#####...............................
11-04  #99  ....................................##########..............
11-05  #99  .............................................##########.....
```

I create a dictionary which has the number of times each guard slept at each minute. For the above example, this would be the following.

```python
total_sleep_time_by_minute_by_guard = {
    10: [
        0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
        1, 1, 1, 1, 2, 1, 1, 1, 1, 0, 
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
        1, 1, 1, 1, 1, 0, 0, 0, 0, 0
    ], 
    99: [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 
        2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 
        1, 1, 1, 1, 1, 0, 0, 0, 0, 0
    ]
}
```

For example, guard `99` slept `3` times at minute `45`.

## Part 1

The `sleepiest_guard` in part 1 is defined as the guard which slept the most total minutes. So we just sum the minute frequency list of each guard, and take the maximum.

```python
sleepiest_guard, _ = max(total_sleep_time_by_minute_by_guard.items(), key=lambda t: sum(t[1]))
```

Now, we want to find the minute interval for which this guard slept the longest. I do this using `enumerate`

```python
max_minute, _ = max(enumerate(total_sleep_time_by_minute_by_guard[sleepiest_guard]), key=lambda t: t[1])
```

Finally, we return their product

```python
return sleepiest_guard * max_minute
```

## Part 2 

Part 2 is very similar, except the `sleepiest_guard` is defined as the guard who most frequently asleep on the same minute. This means instead of summing the minute frequency list, we just take the max. 

```python
sleepiest_guard, _ = max(total_sleep_time_by_minute_by_guard.items(), key=lambda t: max(t[1]))
max_minute, _ = max(enumerate(total_sleep_time_by_minute_by_guard[sleepiest_guard]), key=lambda t: t[1])
return sleepiest_guard * max_minute
```