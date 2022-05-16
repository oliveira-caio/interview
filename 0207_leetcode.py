"""207. Course Schedule

link: https://leetcode.com/problems/course-schedule/

problem: There are a total of numCourses courses you have to take, labeled from
0 to numCourses - 1. You are given an array prerequisites where prerequisites[i]
= [ai, bi] indicates that you must take course bi first if you want to take
course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first
take course 1.

Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you
should also have finished course 1. So it is impossible.

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""


from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def bfs(courses, source, output):
            visited = {source}
            queue = deque([source])

            while queue:
                curr = queue.popleft()
                output.append(curr)
                for neighbor in courses[curr][1]:
                    if neighbor not in visited:
                        courses[neighbor][0] -= 1
                        if courses[neighbor][0] == 0:
                            visited.add(neighbor)
                            queue.append(neighbor)

        courses = {i: [0, []] for i in range(numCourses)}
        start, output = [], []

        for first, second in prerequisites:
            courses[second][1].append(first)
            courses[first][0] += 1

        for course in courses:
            if courses[course][0] == 0:
                start.append(course)

        for course in start:
            bfs(courses, course, output)

        return len(output) == numCourses
