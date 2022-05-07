from graph import Graph
from math import inf

nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens"]

edges = {}
for node in nodes:
    edges[node] = {}

edges["Reykjavik"]["Oslo"] = 5
edges["Reykjavik"]["London"] = 4
edges["Oslo"]["Berlin"] = 1
edges["Oslo"]["Moscow"] = 3
edges["Moscow"]["Belgrade"] = 5
edges["Moscow"]["Athens"] = 4
edges["Athens"]["Belgrade"] = 1
edges["Rome"]["Berlin"] = 2
edges["Rome"]["Athens"] = 2


def prims_mst(graph):
    selected = dict()
    for node in nodes:
        selected[node] = False
    selected[nodes[0]] = True

    unprocessed_nodes = len(nodes)
    while unprocessed_nodes > 1:
        minimum = inf

        min_edge_nodes = [None, None]
        for node1 in nodes:
            if selected[node1]:
                for node2 in nodes:
                    if not selected[node2] and minimum > graph.value(node1, node2):
                        minimum = graph.value(node1, node2)
                        min_edge_nodes = [node1, node2]

        unprocessed_nodes -= 1
        node1, node2 = min_edge_nodes
        selected[node2] = True
        print('shortest path', node1, 'to', node2, 'is taking', minimum, 'cost')


cities_graph = Graph(nodes, edges)

print(prims_mst(cities_graph))

