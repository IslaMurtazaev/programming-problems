# https://leetcode.com/problems/course-schedule-ii/
import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        use topological sorting
        0 -> 1

        0 => 2 => 3
        0 => 1
        """
        indegree = [0] * numCourses
        adj_list = collections.defaultdict(set)
        for dest, src in prerequisites:
            indegree[dest] += 1
            adj_list[src].add(dest)

        zero_in_degrees = collections.deque()
        for course, in_degree in enumerate(indegree):
            if in_degree == 0:
                zero_in_degrees.append(course)

        output = []
        while zero_in_degrees:
            course = zero_in_degrees.pop()
            output.append(course)
            for dest in adj_list[course]:
                indegree[dest] -= 1
                if indegree[dest] == 0:
                    zero_in_degrees.append(dest)

        return output if len(output) == numCourses else []


print(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
