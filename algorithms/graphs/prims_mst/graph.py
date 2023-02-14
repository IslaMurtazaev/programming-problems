from math import inf

class Graph(object):
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self._keys_to_indices = dict()
        self.graph = self.construct_graph(nodes, edges)

    def construct_graph(self, nodes, edges):
        '''
        Create an adjacency matrix of graph
        '''
        N = len(nodes)
        adjacency_matrix = [[inf] * N for _ in range(N)]

        for i, node in enumerate(nodes):
            self._keys_to_indices[node] = i

        for node1 in edges.keys():
            for node2, cost in edges[node1].items():
                node1_idx, node2_idx = self._keys_to_indices[node1], self._keys_to_indices[node2]
                adjacency_matrix[node1_idx][node2_idx] = cost
                adjacency_matrix[node2_idx][node1_idx] = cost

        return adjacency_matrix

    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes

    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node) is not None:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        node1_idx, node2_idx = self._keys_to_indices[node1], self._keys_to_indices[node2]
        return self.graph[node1_idx][node2_idx]
