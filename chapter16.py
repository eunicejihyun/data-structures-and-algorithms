# Modify Dijkstra's algorithm so it only returns the path from a starting vertex to another vertex you pass in.

import heapq


def dijkstra(graph: dict, starting_vertex: str, ending_vertex: str) -> str:
    """Using the starter code for Dijkstra's algorithm from the book, it was modified to return the most efficient path through the graph as opposed to returning a dictionary with distances

    Args:
        graph (dict): a graph represented by a nested python dictionary
        starting_vertex (str): starting point from which to find the most efficient route to the ending vertex
        ending_vertex (str): ending point to which to find the most efficient route from the starting vertex

    Returns:
        str: the most efficient path through the graph
    """
    distances = {
        vertex: {"distance": float("infinity"), "path": ""} for vertex in graph
    }
    distances[starting_vertex] = {"distance": 0, "path": ""}
    pq = [(0, starting_vertex, starting_vertex)]

    while len(pq) > 0:
        current_distance, current_vertex, path = heapq.heappop(pq)
        if current_distance > distances[current_vertex]["distance"]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]["distance"]:
                distances[neighbor]["distance"] = distance
                distances[neighbor]["path"] = f"{path} -> {neighbor}"
                heapq.heappush(pq, (distance, neighbor, f"{path} -> {neighbor}"))
    return distances[ending_vertex]["path"]


graph = {"A": {"B": 2, "C": 6}, "B": {"D": 5}, "C": {"D": 8}, "D": {}}

print(dijkstra(graph, "A", "D"))
