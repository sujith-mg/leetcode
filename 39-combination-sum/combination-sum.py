class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, path, total):
            if total == target:
                result.append(path[:])  # found valid combination
                return
            
            if total > target:
                return  # stop if exceeded
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])  # choose
                backtrack(i, path, total + candidates[i])  # reuse same element
                path.pop()  # backtrack

        backtrack(0, [], 0)
        return result