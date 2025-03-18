from collections import deque

def bfs_shortest_path(city_map, start, goal):
    if start not in city_map or goal not in city_map:
        return "Start or goal not in city map"
    
    queue = deque([[start]])
    visited = set()
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            for neighbor in city_map.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    
    return "No path found"


city_map = {
    'Home': ['Mall', 'School'],
    'Mall': ['Gym', 'Hospital'],
    'School': ['Library'],
    'Gym': ['Hospital'],
    'Library': ['Hospital'],
    'Hospital': []
}

start = 'Home'
goal = 'Hospital'

shortest_path = bfs_shortest_path(city_map, start, goal)
print("Shortest path:", shortest_path)
