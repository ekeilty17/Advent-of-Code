class BinaryTree:

    def __init__(self, value=0, visited=False):
        self.value = value
        self.visited = visited
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f"'{self.value}'"