class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        seen = set() # all courses along curr DFS path

        def dfs(crs):
            if crs in seen:
                return False

            if preMap[crs] == []:
                return True

            seen.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            seen.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True

        

        