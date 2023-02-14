# https://leetcode.com/problems/pacific-atlantic-water-flow/
import collections
from typing import List


"""
optimization:
store state of cells (states: 1 if can reach pacific, 2 if can reach atlantic, 3 if both)


create a matrix of states = states

results = []
iterate through all cells:
    dfs(cell, states)
    if states[cell] is both PO and AO:
        results.append(cell)

return results

DFS(i, j, states):
    if states[i][j] != None:
        return states[i][j]
    states[i][j] = 0 # to mark this as being processed already and avoid cycles
    if cell is on top or left border:
        states[i][j] += 1
    if cell is on bottom or right border:
        states[i][j] += 2

    for neighbor in neighbors:
        if neighbor is lower than i, j:
            curr_val = dfs(neighbor, states)
            if curr_val != states[i][j]:
                states[i][j] += curr_val
            if states[i][j] == 3:
                break
    return states[i][j]

I didn't think of a case where i,j => i+1,j can also be i+1,j => i,j
when we process i,j we already set value of i+1,j without knowing if i,j would yield a better result
So I have to start DFS from each cell
TC = O((n * m)^2)
SC = O(n * m)
"""


class Approach1:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        PACIFIC = 1
        ATLANTIC = 2
        BOTH = 3

        def get_lower_neighbors(i, j):
            result = []
            if i + 1 < len(heights) and heights[i][j] >= heights[i + 1][j]:
                result.append((i + 1, j))
            if i - 1 >= 0 and heights[i][j] >= heights[i - 1][j]:
                result.append((i - 1, j))
            if j + 1 < len(heights[i]) and heights[i][j] >= heights[i][j + 1]:
                result.append((i, j + 1))
            if j - 1 >= 0 and heights[i][j] >= heights[i][j - 1]:
                result.append((i, j - 1))
            return result

        def dfs(i, j, memo, visited):
            if (i, j) in visited:
                return 0
            if memo[i][j] != None:
                return memo[i][j]
            visited.add((i, j))

            curr_state = 0
            if i == 0 or j == 0:
                curr_state += PACIFIC
            if i + 1 == len(heights) or j + 1 == len(heights[i]):
                curr_state += ATLANTIC
            if curr_state == BOTH:
                return BOTH

            # check neighbors
            neighbors = get_lower_neighbors(i, j)

            for x, y in neighbors:
                neighbor_state = dfs(x, y, memo, visited)
                if neighbor_state == BOTH or (neighbor_state == PACIFIC and curr_state == ATLANTIC) or (
                        neighbor_state == ATLANTIC and curr_state == PACIFIC):
                    return BOTH
                if curr_state == 0:
                    curr_state = neighbor_state
            return curr_state

        states = [[None] * len(heights[0]) for _ in range(len(heights))]

        results = []
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                states[i][j] = dfs(i, j, states, set())
                if states[i][j] == BOTH:
                    results.append((i, j))

        return results


class Approach2:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Approach 2. Traverse from oceans
        TC = O(n * m)
        SC = O(n * m)
        """
        PACIFIC = 1
        ATLANTIC = 2
        BOTH = 3

        N, M = len(heights), len(heights[0])
        oceans = [[0] * M for _ in range(N)]

        def get_uphill_neighbors(x, y):
            neighbors = []
            if x + 1 < N and heights[x + 1][y] >= heights[x][y]:
                neighbors.append((x + 1, y))
            if x - 1 >= 0 and heights[x - 1][y] >= heights[x][y]:
                neighbors.append((x - 1, y))
            if y + 1 < M and heights[x][y + 1] >= heights[x][y]:
                neighbors.append((x, y + 1))
            if y - 1 >= 0 and heights[x][y - 1] >= heights[x][y]:
                neighbors.append((x, y - 1))
            return neighbors

        def bfs(queue, oceans, ocean):
            while queue:
                x, y = queue.popleft()

                neighbors = get_uphill_neighbors(x, y)
                for x_i, y_i in neighbors:
                    if oceans[x_i][y_i] == ocean or oceans[x_i][y_i] == BOTH:
                        continue
                    queue.append((x_i, y_i))
                    oceans[x_i][y_i] += ocean

        # step1 add 1 to all cells that are reachable from pacific ocean
        # bfs?
        queue = collections.deque()
        for i in range(N):
            queue.append((i, 0))
            oceans[i][0] += PACIFIC
        for j in range(1, M):
            queue.append((0, j))
            oceans[0][j] += PACIFIC
        bfs(queue, oceans, PACIFIC)

        # step2 add 2 to all cells that are reachable from atlantic ocean
        queue = collections.deque()
        for i in range(N):
            queue.append((i, M - 1))
            oceans[i][M - 1] += ATLANTIC
        for j in range(M - 1):
            queue.append((N - 1, j))
            oceans[N - 1][j] += ATLANTIC
        bfs(queue, oceans, ATLANTIC)

        # return all cells that have value 3
        result = []
        for i in range(N):
            for j in range(M):
                if oceans[i][j] == BOTH:
                    result.append((i, j))
        return result


