import heapq

class Solution:
    def minimumEffortPath(self, heights):
        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < cols

        def dijkstra():
            queue = [(0, 0, 0)]
            efforts = [[float('inf')] * cols for _ in range(rows)]
            efforts[0][0] = 0

            while queue:
                curr_effort, x, y = heapq.heappop(queue)

                if x == rows - 1 and y == cols - 1:
                    return curr_effort

                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy

                    if is_valid(new_x, new_y):
                        new_effort = max(curr_effort, abs(heights[x][y] - heights[new_x][new_y]))

                        if new_effort < efforts[new_x][new_y]:
                            efforts[new_x][new_y] = new_effort
                            heapq.heappush(queue, (new_effort, new_x, new_y))

        return dijkstra()