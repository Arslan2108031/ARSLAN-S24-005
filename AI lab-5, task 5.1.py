class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []  
    def add_neighbor(self, node):
        self.neighbors.append(node)
class Graph:
    def __init__(self):
        self.nodes = {} 
    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = Node(value)
    def add_edge(self, from_value, to_value):
        if from_value in self.nodes and to_value in self.nodes:
            self.nodes[from_value].add_neighbor(self.nodes[to_value])
            self.nodes[to_value].add_neighbor(self.nodes[from_value])
    def dfs_stack(self, start_value):
        if start_value not in self.nodes:
            print("node not found")
            return        
        start_node = self.nodes[start_value]
        stack = [start_node]  
        visited = set()  
        print("DFS Traversal:")
        while stack:
            node = stack.pop()  
            if node not in visited:
                print(node.value)  
                visited.add(node)  
                for neighbor in reversed(node.neighbors):  
                    if neighbor not in visited:
                        stack.append(neighbor)
graph = Graph()
for value in ["A", "B", "C", "D", "E"]:
    graph.add_node(value)
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("B", "E")
graph.dfs_stack("A")
