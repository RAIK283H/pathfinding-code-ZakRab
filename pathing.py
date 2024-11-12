import heapq
import graph_data
import global_game_data
from numpy import random

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]


def get_random_path():
    path = []
    seen = set()
    curr_graph = graph_data.graph_data[global_game_data.current_graph_index]
    curr_node = 0
    path.append(curr_node)
    seen.add(0)
    # precodition the graph has atleast one node
    assert curr_graph[0] is not None
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    while target_node not in seen:
        curr_neighbors = curr_graph[curr_node][1]
        next_node = random.choice(curr_neighbors)
        path.append(next_node)
        seen.add(next_node)
        curr_node = next_node

    exit_node = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1
    while exit_node not in seen:
        curr_neighbors = curr_graph[curr_node][1]
        next_node = random.choice(curr_neighbors)
        path.append(next_node)
        seen.add(next_node)
        curr_node = next_node
        # postcondition the path has gone through both the target node and the exit node
    assert target_node in seen
    assert exit_node in seen
    return path


def get_dfs_path():
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    exit_node = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1
    curr_graph = graph_data.graph_data[global_game_data.current_graph_index]
    seen = set()
    
    def dfs(curr_node, start_node, end_node):
        if curr_node in seen:
            return None
        seen.add(curr_node)
        if curr_node == end_node:
            return [curr_node]
        for neighbor in sorted(curr_graph[curr_node][1]): 
            assert neighbor in curr_graph[curr_node][1]

            path = dfs(neighbor, start_node, end_node)
            if path is not None:
                return [curr_node] + path
        return None


    target_path = dfs(0, 0, target_node) 
    seen.clear()
    exit_path = dfs(target_node, target_node, exit_node)
    assert target_node in seen
    assert exit_node in seen
    return target_path + exit_path[1:] 



def get_bfs_path():
    curr_graph = graph_data.graph_data[global_game_data.current_graph_index]
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    exit_node = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1

    def bfs(start_node, end_node):
        queue = []
        queue.append([start_node])
        visited = set()  
        visited.add(start_node) 
        
        while queue:
            curr_path = queue.pop(0)  
            curr_node = curr_path[-1]
            
            if curr_node == end_node:
                return curr_path
            
            for neighbor in sorted(curr_graph[curr_node][1]): 
                assert neighbor in curr_graph[curr_node][1]
                if neighbor not in visited: 
                    visited.add(neighbor) 
                    new_path = list(curr_path) 
                    new_path.append(neighbor)
                    queue.append(new_path) 
        
        assert target_node in visited
        assert exit_node in visited

    return bfs(0, target_node) + bfs(target_node, exit_node)[1:]

def get_dijkstra_path():
    curr_graph = graph_data.graph_data[global_game_data.current_graph_index]
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    exit_node = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1
    
    def dijkstra(start_node, end_node):
        heap = []
        heapq.heappush(heap, (0, start_node, [start_node]))
        distances = {node: float('inf') for node in range(len(curr_graph))}
        distances[start_node] = 0
        
        while heap:
            curr_distance, curr_node, path = heapq.heappop(heap)
            
            if curr_node == end_node:
                return path
            
            for neighbor in curr_graph[curr_node][1]:
                x,y = curr_graph[neighbor][0]
                x2,y2 = curr_graph[curr_node][0]
                weight = ((x2-x)**2 + (y2-y)**2)**0.5
                distance = curr_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor, path + [neighbor]))
        
        return None

    target_path = dijkstra(0, target_node)
    exit_path = dijkstra(target_node, exit_node)
    result_path = target_path + exit_path[1:]
    assert target_path is not None
    assert exit_path is not None

    # Postcondition: The result path begins at the start node.
    assert result_path[0] == 0
    # Postcondition: The result path ends at the exit_node.
    assert result_path[-1] == exit_node
    # # Postcondition: Every pair of vertices adjacent in the result path is an edge in the graph.
    # for i in range(len(result_path) - 1):
    #     assert result_path[i + 1] in [neighbor for neighbor, _ in curr_graph[result_path[i]][1]]
    
    return result_path

