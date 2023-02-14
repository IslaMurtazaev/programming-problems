from typing import List
import collections
from math import inf
import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        treat every cell as the vertex
        and abs differences between neighbors are weighted edges

        use djikstra from 0,0 to m-1,n-1


        eg:
        node = (0, 0)
        edges = {
            nodeA: [(nodeB, difficulty)]
        }
        """
        graph = collections.defaultdict(dict)
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                node = (i, j)
                if i > 0:
                    self.assign_edges(node, (i-1, j), graph, heights)
                if i + 1 < len(heights):
                    self.assign_edges(node, (i+1, j), graph, heights)
                if j > 0:
                    self.assign_edges(node, (i, j-1), graph, heights)
                if j + 1 < len(heights[i]):
                    self.assign_edges(node, (i, j+1), graph, heights)

        for key, value in graph.items():
            print(key,value)

        # use djikstra
        starting_pos = (0,0)
        dist = dict()
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                dist[(i,j)] = inf
        dist[starting_pos] = 0

        to_process = [(0, starting_pos)]
        visited = set()
        while to_process:
            node_dist, position = heapq.heappop(to_process)
            visited.add(position)
            i, j = position

            neighbors = []
            if i > 0:
                neighbors.append((i-1, j))
            if i + 1 < len(heights):
                neighbors.append((i+1, j))
            if j > 0:
                neighbors.append((i, j-1))
            if j + 1 < len(heights[0]):
                neighbors.append((i, j+1))

            for neighbor in neighbors:
                dist[neighbor] = min(dist[neighbor], max(dist[position], graph[position][neighbor]))
                if neighbor not in visited:
                    heapq.heappush(to_process, (dist[neighbor], neighbor))

        return dist[(len(heights)-1, len(heights[0])-1)]

    def assign_edges(self, src_node, dest_node, graph, heights):
        weight = abs(heights[src_node[0]][src_node[1]] - heights[dest_node[0]][dest_node[1]])
        graph[src_node][dest_node] = min(graph[src_node].get(dest_node, inf), weight)
        graph[dest_node][src_node] = min(graph[dest_node].get(src_node, inf), weight)


print(Solution().minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]))
