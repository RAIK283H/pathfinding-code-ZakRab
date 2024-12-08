import graph_data
# desc: this function will transform a graph from an adjacency list to an adjancey matrix with weights 
def transform_graph_to_matrix(curr_graph):
    n = len(curr_graph)
    matrix = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 0

    for i, curr_node in enumerate(curr_graph):
        (x2, y2), edges = curr_node
        for edge in edges:
            x, y = curr_graph[edge][0]
            weight = ((x2 - x)**2 + (y2 - y)**2)**0.5
            matrix[i][edge] = weight
    return matrix

def floyd_warshall(matrix):
    n = len(matrix)
    dist = [row[:] for row in matrix]  
    pred = [[-1] * n for _ in range(n)] 

    for i in range(n):
        for j in range(n):
            if dist[i][j] != float('inf') and i != j:
                pred[i][j] = i  

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]  

    return dist, pred

def reconstruct_path(pred, start, end):
    path = []
    if pred[start][end] == -1:
        return path 
    
    while end != start:
        path.insert(0, end)
        end = pred[start][end]
    path.insert(0, start)
    
    return path

def shortest_pathfw(graph, start, end):
    matrix = transform_graph_to_matrix(graph)
    dist_matrix, pred_matrix = floyd_warshall(matrix)
    path = reconstruct_path(pred_matrix, start, end)
    if not path:
        return None  # No path exists
    return path, dist_matrix[start][end]


def main():
    # test the function
    curr_graph = graph_data.graph_data[0]

    start_node = 0
    end_node = 2
    result = shortest_pathfw(curr_graph, start_node, end_node)
    
    if result is None:
        print(f"No path exists between node {start_node} and node {end_node}.")
    else:
        path, distance = result
        print(f"The shortest path from node {start_node} to node {end_node} is {path} with a distance of {distance}.")

main()