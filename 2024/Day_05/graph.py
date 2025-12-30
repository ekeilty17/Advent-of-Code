from collections import deque
from typing import Set, Tuple, Hashable, Dict, List, Optional

class Graph:

    def __init__(self):
        self._nodes: Set[Hashable] = set([])
        self._adj: Dict[Hashable, List[Hashable]] = {}

    @classmethod
    def from_adjacency_list(cls, adj: Dict[Hashable, List[Hashable]]):
        G = cls()
        for u, neighbors in adj.items():
            for v in neighbors:
                G.add_edge((u, v))
        return G

    # ---------- Getters and Setters ----------
    def get_nodes(self) -> Set[Hashable]:
        return self._nodes
    
    def get_edges(self):
        for u, neighbors in self._adj.items():
            for v in neighbors:
                yield (u, v)

    def add_node(self, u: Hashable):
        self._nodes.add(u)

    def add_edge(self, edge: Tuple[Hashable, Hashable]):
        u, v = edge
        self.add_node(u)
        self.add_node(v)

        if u in self._adj:
            self._adj[u].add(v)
        else:
            self._adj[u] = set([v])

    def get_neighbors(self, u: Hashable) -> List[Hashable]:
        return self._adj.get(u, [])

    # ---------- Subgraph ----------
    def get_subgraph(self, sub_nodes: List[Hashable]):
        subG = Graph()
        for u in sub_nodes:
            subG.add(u)
        
        for u, v in self.get_edges():
            if not (u in sub_nodes and v in sub_nodes):
                continue
            subG.add_edge((u, v))
        
        return subG

    # ---------- Subgraph ----------
    def get_subgraph(self, sub_nodes: List[Hashable]):
        subG = Graph()
        
        for u, v in self.get_edges():
            if not (u in sub_nodes and v in sub_nodes):
                continue
            subG.add_edge((u, v))
        
        return subG

    # ---------- Properties of the Graph ----------
    def get_in_degrees(self) -> Dict[Hashable, int]:
        in_degree = {node: 0 for node in self.get_nodes()}
        for u, v in self.get_edges():
            in_degree[v] += 1
        return in_degree
    
    def get_out_degrees(self) -> Dict[Hashable, int]:
        out_degree = {node: 0 for node in self.get_nodes()}
        for u, v in self.get_edges():
            out_degree[u] += 1
        return out_degree

    # ---------- Graph Algorithms ----------
    def topological_sort(self) -> List[Hashable]:

        in_degree = self.get_in_degrees()

        # Initialize queue with nodes of in-degree 0
        queue = deque([node for node in in_degree if in_degree[node] == 0])
        topological_order = []

        # Modified BFS
        while queue:
            node = queue.popleft()
            topological_order.append(node)

            for neighbor in self.get_neighbors(node):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Check for cycle
        if len(topological_order) != len(in_degree):
            raise RuntimeError("Graph contains a cycle. Topological sort not possible.")

        return topological_order