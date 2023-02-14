from graph import Graph
from math import inf
from heapq import heappop, heappush

nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens"]

init_graph = {}
for node in nodes:
    init_graph[node] = {}

init_graph["Reykjavik"]["Oslo"] = 5
init_graph["Reykjavik"]["London"] = 4
init_graph["Oslo"]["Berlin"] = 1
init_graph["Oslo"]["Moscow"] = 3
init_graph["Moscow"]["Belgrade"] = 5
init_graph["Moscow"]["Athens"] = 4
init_graph["Athens"]["Belgrade"] = 1
init_graph["Rome"]["Berlin"] = 2
init_graph["Rome"]["Athens"] = 2


def dijkstra(graph, starting_node):
    shortest_path = dict()
    visited = set()

    for node in graph.nodes:
        shortest_path[node] = inf if node != starting_node else 0

    to_process = [(0, starting_node)]
    while to_process:
        node_dist, node_val = heappop(to_process)
        visited.add(node_val)

        for outgoing_node in graph.get_outgoing_edges(node_val):
            shortest_path[outgoing_node] = min(shortest_path[outgoing_node], node_dist + graph.value(node_val, outgoing_node))

            if outgoing_node not in visited:
                heappush(to_process, (shortest_path[outgoing_node], outgoing_node))

    return shortest_path


cities_graph = Graph(nodes, init_graph)

print(dijkstra(cities_graph, 'Reykjavik'))
