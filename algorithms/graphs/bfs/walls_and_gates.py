from typing import List
import collections

# BFS with stack -> Time optimized version, bfs and mark all rooms from gates
# https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1373/


class Solution:
    def __init__(self):
        self.WALL = -1
        self.UNCHECKED_PATH = 2147483647
        self.PROCESSING = -2
        self.GATE = 0

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        unchecked_rooms = collections.deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == self.GATE:
                    rooms[i][j] = self.PROCESSING
                    unchecked_rooms.append([i, j, 0])

        while unchecked_rooms:
            room_y, room_x, distance = unchecked_rooms.popleft()
            rooms[room_y][room_x] = distance
            self.addNeighbors(unchecked_rooms, room_y, room_x, distance+1, rooms)

    def addNeighbors(self, queue, y, x, distance, rooms):
        neighbors = []
        if y + 1 < len(rooms):
            neighbors.append([y+1, x])
        if x + 1 < len(rooms[y]):
            neighbors.append([y, x+1])
        if y - 1 >= 0:
            neighbors.append([y-1, x])
        if x - 1 >= 0:
            neighbors.append([y, x-1])
        for neighbor_y, neighbor_x in neighbors:
            if rooms[neighbor_y][neighbor_x] == self.UNCHECKED_PATH:
                queue.append([neighbor_y, neighbor_x, distance])
                rooms[neighbor_y][neighbor_x] = self.PROCESSING
