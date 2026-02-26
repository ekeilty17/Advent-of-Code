from utils.solve import test, solve
from typing import Any

class DoubleLinkedListNode:
    def __init__(self, value: Any, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __repr__(self):
        return self.value.__repr__()

class DoubleLinkedListRoot:

    def __init__(self) -> None:
        self.root = None

    def __repr__(self) -> str:
        if self.root is None:
            return "[]"
        
        nodes = [self.root.value]
        curr = self.root.next
        while curr != self.root:
            nodes.append(curr.value)
            curr = curr.next
        return "[" + ", ".join([str(node) for node in nodes]) + "]"

    def append(self, value: Any) -> None:
        if self.root is None:
            self.root = DoubleLinkedListNode(value=value)
            self.root.next = self.root
            self.root.prev = self.root
            return
        
        node = DoubleLinkedListNode(value=value, prev=self.root.prev, next=self.root)
        node.prev.next = node
        self.root.prev = node

    def pop(self) -> Any:
        if self.root is None:
            return None
        
        last = self.root.prev
        if last == self.root:
            self.root = None
            return last.value
        
        last.prev.next = self.root
        self.root.prev = last.prev

        last.prev = None
        last.next = None
        return last.value

    def rotate(self, n: int=1):
        if n == 0:
            return
        if self.root is None:
            return
        

        last = self.root.prev
        if last == self.root:
            return

        new_root = self.root
        for _ in range(abs(n)):
            new_root = new_root.prev if n > 0 else new_root.next

        self.root = new_root


def solution(num_players: int, num_marbels: int) -> int:
    player_scores = [0] * num_players
    played_marbles = DoubleLinkedListRoot()
    played_marbles.append(0)

    for turn in range(num_marbels):
        player = turn % num_players
        marble = turn + 1

        if marble % 23 == 0:
            played_marbles.rotate(7)
            player_scores[player] += marble + played_marbles.pop()
            played_marbles.rotate(-1)

        else:
            played_marbles.rotate(-1)
            played_marbles.append(marble)

    return max(player_scores)

if __name__ == "__main__":
    examples = [
        (9, 25, 32),
        (10, 1618, 8317),
        (13, 7999, 146373),
        (17, 1104, 2764),
        (21, 6111, 54718),
        (30, 5807, 37305),
    ]
    for example_num_players, example_num_marbels, expected_answer in examples:
        test(expected_answer, solution, example_num_players, example_num_marbels)
    
    num_players = 427
    num_marbels = 70723 * 100
    solve(solution, num_players, num_marbels)