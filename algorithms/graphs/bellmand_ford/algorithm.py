from math import inf

nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens", "Bishkek", "Istanbul", "Antalya"]

edges = [["Reykjavik", "Oslo", 5], ["Reykjavik", "London", 4], ["Oslo", "Berlin", 1],
         ["Oslo", "Moscow", 3], ["Moscow", "Belgrade", 5], ["Moscow", "Athens", 4], ["Athens", "Belgrade", 1],
         ["Rome", "Berlin", 2], ["Rome", "Athens", 2], ["Bishkek", "Istanbul", 1], ["Istanbul", "Bishkek", -1],
         ["Istanbul", "Antalya", -2], ["Antalya", "Bishkek", 5]]


def bellman_ford(edges, source):
    dist = dict()
    for node in nodes:
        dist[node] = inf
    dist[source] = 0

    for _ in range(len(nodes) - 1):
        for src, dst, w in edges:
            dist[dst] = min(dist[src] + w, dist[dst])

    for _ in range(len(nodes) - 1):
        for src, dst, w in edges:
            if dist[dst] > dist[src] + w:
                return "negative cycle detected"

    return dist


print(bellman_ford(edges, "Bishkek"))
