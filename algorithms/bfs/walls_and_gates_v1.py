from typing import List
import collections

# BFS with stack
# https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1373/


class Solution:
    def __init__(self):
        self.WALL = -1
        self.UNCHECKED_PATH = 2147483647
        self.GATE = 0

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == self.UNCHECKED_PATH:
                    rooms[i][j] = self.bfsShortestPath(rooms, i, j)

    def bfsShortestPath(self, rooms, room_row, room_col):
        def addNeighbors(y, x, distance, options, visited):
            neighbors = []
            if y + 1 < len(rooms):
                neighbors.append([y+1, x])
            if x + 1 < len(rooms[y]):
                neighbors.append([y, x+1])
            if y - 1 >= 0:
                neighbors.append([y-1, x])
            if x - 1 >= 0:
                neighbors.append([y, x-1])
            for n_y, n_x in neighbors:
                if f'{n_y}_{n_x}' not in visited and rooms[y][x] != self.WALL:
                    options.append([n_y, n_x, distance+1])

        potential_paths = collections.deque()
        visited = {f'{room_row}_{room_col}'}
        addNeighbors(room_row, room_col, 0, potential_paths, visited)
        while potential_paths:
            r_y, r_x, distance = potential_paths.popleft()
            visited.add(f'{r_y}_{r_x}')
            if rooms[r_y][r_x] == self.GATE:
                return distance
            else:
                addNeighbors(r_y, r_x, distance, potential_paths, visited)
        return rooms[room_row][room_col]
