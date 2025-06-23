# Time Complexity: O(k), where k is the number of valid permutations (typically much less than n!)
# - We prune invalid paths early based on the divisibility rule.
#
# Space Complexity: O(n)
# - O(n) for the visited array
# - O(n) recursion depth in the call stack
#
# Did this code successfully run on Leetcode : YES
# Any problem you faced while coding this : No

from typing import List

class Solution:
    def countArrangement(self, n: int) -> int:
        self.count = 0
        visited = [False] * (n + 1)  # 1-based indexing

        def backtrack(pos: int):
            # base case: all positions filled
            if pos > n:
                self.count += 1
                return

            # try placing each number at current position
            for i in range(1, n + 1):
                if not visited[i] and (i % pos == 0 or pos % i == 0):
                    visited[i] = True
                    backtrack(pos + 1)
                    visited[i] = False  # backtrack

        backtrack(1)
        return self.count

        # ---------------------------------------------------------------
        # Brute-force Permutation-Based Backtracking
        #
        # Time Complexity: O(n!) worst-case (all permutations tried)
        # Space Complexity: O(n) for recursion stack + nums array
        #
        # self.count = 0
        # nums = list(range(1, n + 1))
        #
        # def is_valid(perm):
        #     for i, val in enumerate(perm, 1):
        #         if val % i != 0 and i % val != 0:
        #             return False
        #     return True
        #
        # def permute(start):
        #     if start == n:
        #         if is_valid(nums):
        #             self.count += 1
        #         return
        #     for i in range(start, n):
        #         nums[start], nums[i] = nums[i], nums[start]
        #         permute(start + 1)
        #         nums[start], nums[i] = nums[i], nums[start]
        #
        # permute(0)
        # return self.count


# -------------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.countArrangement(1))  # Output: 1
    print(sol.countArrangement(2))  # Output: 2
    print(sol.countArrangement(3))  # Output: 3
    print(sol.countArrangement(4))  # Output: 8
    print(sol.countArrangement(5))  # Output: 10
