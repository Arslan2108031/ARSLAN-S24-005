def bfs_recursive(graph, level_nodes, visited):
    if not level_nodes:
        return  
        
    next_level = []  
    for node in level_nodes:
        if node not in visited:
            print(node, end=" ")  
            visited.add(node) 
            next_level.extend(graph.get(node, []))  
    bfs_recursive(graph, next_level, visited)  
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": []
}
print("BFS Traversal")
bfs_recursive(graph, ["A"], set())
