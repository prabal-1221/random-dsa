import ast
import heapq
from collections import defaultdict


class Solution:
    def minCost(self, n: int, edges: list[list[int]]) -> int:
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, 2 * w))

        dist = [float("inf")] * n
        dist[0] = 0
        pq = [(0, 0)]

        while pq:
            cost, node = heapq.heappop(pq)

            if node == n - 1:
                return cost

            if cost > dist[node]:
                continue

            for nei, wt in graph[node]:
                new_cost = cost + wt
                if new_cost < dist[nei]:
                    dist[nei] = new_cost
                    heapq.heappush(pq, (new_cost, nei))

        return -1


if __name__ == "__main__":
    n = int(input().strip())
    edges = ast.literal_eval(input().strip())

    sol = Solution()
    print(sol.minCost(n, edges))
