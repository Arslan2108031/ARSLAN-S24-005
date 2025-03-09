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
    def bfs_with_queue(self, start_value):
        if start_value not in self.nodes:
            print("node not found")
            return       
        start_node = self.nodes[start_value]
        queue = [start_node]  
        visited = set()  

        print("BFS Traversal:", end=" ")
        while queue:
            node = queue.pop(0)  
            if node not in visited:
                print(node.value, end=" ") 
                visited.add(node)  
                for neighbor in node.neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)
graph = Graph()
for value in ["A", "B", "C", "D", "E", "F", "G"]:
    graph.add_node(value)
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("B", "E")
graph.add_edge("C", "F")
graph.add_edge("C", "G")
graph.bfs_with_queue("A")
