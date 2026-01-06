# Day 16: Aunt Sue

[Problem Link](https://adventofcode.com/2015/day/16)

## Part 1

A bit of a silly one. Essentially, each `Sue` represents an incomplete set of correct criteria. The `ticker_tape` gives the full set of criteria.

So we need to find a Sue such that
$$
\texttt{gift} \in \texttt{Sue} \implies \texttt{gift} \in \texttt{TickerTape}
$$

This is exactly the definition of a subset $\texttt{Sue} \subseteq \texttt{TickerTape}$. Therefore, we can check

$$
\texttt{Sue} - \texttt{TickerTape} = \empty
$$

The Sue for which the above is true, is the Sue who gave us the gift.

## Part 2 

This is essentially the same thing, except some gifts have different matching criteria. It's just a direct implementation of the problem description. You can see `is_match()` in `part_2.py` for those details.