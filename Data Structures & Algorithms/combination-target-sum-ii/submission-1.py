class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []

        def dfs(start_index, current_sum, combination):

            if current_sum >= target:
                if current_sum == target:
                    results.append(combination.copy())
                    return
                return

            for current_index in range(start_index, len(candidates)):

                if (current_index != start_index and
                    candidates[current_index - 1] == candidates[current_index]):
                    continue

                candidate = candidates[current_index]

                if current_sum + candidate > target:
                    return

                combination.append(candidate)
                dfs(current_index + 1, current_sum + candidate, combination)
                combination.pop()

        dfs(0,0,[])
        return results