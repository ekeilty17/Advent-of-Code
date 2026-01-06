# Day 7: Some Assembly Required

[Problem Link](https://adventofcode.com/2015/day/7)

## Part 1

This was definitely more complicated than I was expecting it to be. 

### Parsing Executing Gates

First things first is we needed to translate things like `p LSHIFT 2` and `NOT e` into python code. First, I used regex patterns to identify each cases
- `r"[A-Za-z0-9]+"` is assignment
- `r"NOT ([A-Za-z0-9]+)"` is negation
- `r"([A-Za-z0-9]+) ([A-Z]+) ([A-Za-z0-9]+)"` is all other boolean operations such as `AND`, `OR`, `LSHIFT`, and `RSHIFT`

These get encoded into a dictionary, for example `p LSHIFT 2 -> q` becomes
```python 
gate = {
    "operation": "LSHIFT",
    "operands": ["p", 2]
}
```

Now, I can define a function to execute each operation
```python
OPS = {
        "assign": lambda a: a,
        "NOT": lambda a: ~a,
        "AND": lambda a, b: a & b,
        "OR": lambda a, b: a | b,
        "LSHIFT": lambda a, b: a << b,
        "RSHIFT": lambda a, b: a >> b,
    }
```

and each gate can be execute using
```python
output = u16( OPS[gate["operation"]](*gate["operands"]) )
```

Note that `u16()` is a custom function which is just the following
```python
def u16(x: int) -> int:
    MASK16 = 0xFFFF
    return x & MASK16
```

There are a few details I have left out, but that is the high-level idea. See the function `parse_gate()` and `execute_gate()` for the full details.

### Determining Execution Order

The list of instructions provided in `input.txt` are not in the correct order. We need to determine the order of execution by tracing the dependencies of each gate. 

Each gate in the circuit has `N` input wires connecting to `1` output wire. Therefore, let the circuit be a [graph](https://en.wikipedia.org/wiki/Graph_(abstract_data_type)) where each wire is a node. A directed edge is placed between two nodes `u -> v` if there is a gate such that `u` is an input and `v` is the output. Since the problem says that 

> Each wire can only get a signal from one source

this will be a [Directed Acyclic Graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph) (DAG). Therefore, there exists a [topologically sort](https://en.wikipedia.org/wiki/Topological_sorting) this DAG. This gives us exactly the order in which we need to execute the instructions.

Finally, iterate through the wires in topological order, execute each instruction, and return the desired wire signal value.

## Part 2 

In part 2, we execute part 1 to obtain the signal of wire `a`, stored in `wire_signals_part_1`. Then, I edit the gates using the following.

```python
gate_by_output_wire["b"] = {
        "operation": "assign",
        "operands": [wire_signals_part_1["a"]]
    }
```

Now, I have replaced the gate on wire `b` with a gate that assigns `b` the value of `a`. Then, I just re-run the whole circuit.