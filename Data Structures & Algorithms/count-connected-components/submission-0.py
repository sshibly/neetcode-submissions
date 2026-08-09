class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        
        seen = set()
        count = 0

        for i in range(n):
            if i not in seen:
                seen.add(i)
                count += 1
                dfs(i)
        
        return count

        # time complexity: O(v+e)
        # space complexity: O(v+e)
        