from math import inf

from helpers.beatify import print_matrix

nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens"]

adj_matrix = [[inf] * len(nodes) for _ in range(len(nodes))]

node_idxs = dict()
for i, city in enumerate(nodes):
    node_idxs[city] = i
adj_matrix[node_idxs["Reykjavik"]][node_idxs["Oslo"]] = 5
adj_matrix[node_idxs["Reykjavik"]][node_idxs["London"]] = 4
adj_matrix[node_idxs["Oslo"]][node_idxs["Berlin"]] = 1
adj_matrix[node_idxs["Oslo"]][node_idxs["Moscow"]] = 3
adj_matrix[node_idxs["Moscow"]][node_idxs["Belgrade"]] = 5
adj_matrix[node_idxs["Moscow"]][node_idxs["Athens"]] = 4
adj_matrix[node_idxs["Athens"]][node_idxs["Belgrade"]] = 1
adj_matrix[node_idxs["Rome"]][node_idxs["Berlin"]] = 2
adj_matrix[node_idxs["Rome"]][node_idxs["Athens"]] = 2


def floyd_warshall(adj_matrix):
    for i in range(len(adj_matrix)):
        adj_matrix[i][i] = 0

    for k in range(len(adj_matrix)):
        for i in range(len(adj_matrix)):
            for j in range(len(adj_matrix)):
                if adj_matrix[i][j] > adj_matrix[i][k] + adj_matrix[k][j]:
                    adj_matrix[i][j] = adj_matrix[i][k] + adj_matrix[k][j]
    return adj_matrix

print_matrix(floyd_warshall(adj_matrix))
