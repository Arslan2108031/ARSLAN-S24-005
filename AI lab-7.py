class Node:
    def __init__(self, name, g=float("inf"), h=0):
        self.name = name    
        self.g = g           
        self.h = h            
        self.f = g + h        
        self.parent = None   
    def __lt__(self, other):
        return self.f < other.f  
class AStarGraph:
    def __init__(self):
        self.nodes = {}      
        self.edges = {}      
    def add_node(self, name, heuristic=0):
        self.nodes[name] = Node(name, h=heuristic)
    def add_edge(self, from_node, to_node, cost):
        if from_node in self.nodes and to_node in self.nodes:
            self.edges.setdefault(from_node, []).append((to_node, cost))
            self.edges.setdefault(to_node, []).append((from_node, cost))  
    def a_star_search(self, start, goal):
        if start not in self.nodes or goal not in self.nodes:
            print("Start or goal node not found!")
            return None
        open_list = [self.nodes[start]]  
        closed_set = set()             
        self.nodes[start].g = 0  
        self.nodes[start].f = self.nodes[start].h  
        while open_list:
            open_list.sort()  
            current = open_list.pop(0) 
            if current.name == goal: 
                return self.reconstruct_path(current)
            closed_set.add(current.name)
            for neighbor_name, cost in self.edges.get(current.name, []):
                neighbor = self.nodes[neighbor_name]
                if neighbor.name in closed_set:
                    continue  
                tentative_g = current.g + cost  
                if tentative_g < neighbor.g:  
                    neighbor.g = tentative_g
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.parent = current 
                    if neighbor not in open_list:
                        open_list.append(neighbor)
        return None  
    def reconstruct_path(self, node):
        path = []
        while node:
            path.append(node.name)
            node = node.parent
        return path[::-1]
graph = AStarGraph()
heuristics = {
    "A": 10, "B": 8, "C": 5, "D": 7, "E": 3, "F": 6, "G": 0
}
for node, h_value in heuristics.items():
    graph.add_node(node, heuristic=h_value)
graph.add_edge("A", "B", 2)
graph.add_edge("A", "C", 4)
graph.add_edge("B", "D", 3)
graph.add_edge("B", "E", 1)
graph.add_edge("C", "F", 5)
graph.add_edge("D", "G", 6)
graph.add_edge("E", "G", 2)
graph.add_edge("F", "G", 3)
shortest_path = graph.a_star_search("A", "G")
if shortest_path:
    print("Shortest Path:", " → ".join(shortest_path))
else:
    print("No path found.")
