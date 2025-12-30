class InternvalSet:
    
    def __init__(self):
        self.intervals = set([])

    def __repr__(self):
        out = ""
        for interval in sorted(self.intervals):
            out += str(interval) + "\n"
        return out

    def __contains__(self, item):
        for a, b in self.intervals:
            if a <= item <= b:
                return True
        return False
    
    def __iter__(self):
        return self.intervals.__iter__()

    def add(self, lower, upper):
        lower, upper = min(lower, upper), max(lower, upper)

        overlapping_intervals = set([(lower, upper)])

        for a, b in self.intervals:
            if (upper < a) or (b < lower):
                # None overlapping intervals
                continue
            overlapping_intervals.add((a, b))
        
        self.intervals = self.intervals - overlapping_intervals

        new_a = min(a for a, _ in overlapping_intervals)
        new_b = max(b for _, b in overlapping_intervals)
        self.intervals.add((new_a, new_b))