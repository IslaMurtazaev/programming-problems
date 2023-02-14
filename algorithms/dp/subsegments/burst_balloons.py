from functools import lru_cache
from typing import List


class Solution:
    def maxCoins(self, nums: List[int], product=0) -> int:
        """
        burst all balloons with maximum coins gain

        bursting an i-th balloon removes it from array and uses product of (i-1,i,i+1)

        better burst balloons with smaller coins first?

        Brute force
        nums = [3,1,5,8]
                              0
                        /   /   \    \
                    1-3-1 3-1-5 1-5-8 5-8-1
                   / | \
             3-1-5 1-5-8 5-8-1

        base case:
            * the list of balloons gets empty

        [3,1,5,8]

                     1,2,3|0   12
                      / | \
               2,3|2  1,3|6  1,2|6
             / |       /\       | \
         3|6  2|6    3|3 1|3   2|2  1|2
        (9)   (8)   (6) (4)   (4)   (3)

        [1 * 2 * 3] = 6
        [1 * 1 * 3] = 3
        [1 * 3 * 1] = 3
        3 + 3 + 6 = 12 (max)

        use dfs
        number of children = n (decreases on each level by 1)
        depth = n
        TC = n^n

        dynamic programming
        123 = 12
        [0] = 2 || 11
        [1] = 6 || 12
        [2] = 6 || 10
        """
        # handle edge case
        nums = [1] + nums + [1]

        @lru_cache(None)  # memoization
        def dp(left, right):
            # maximum if we burst all nums[left]...nums[right], inclusive
            if right - left < 0:
                return 0
            result = 0
            # find the last burst one in nums[left]...nums[right]
            for i in range(left, right + 1):
                # nums[i] is the last burst one
                gain = nums[left - 1] * nums[i] * nums[right + 1]
                # nums[i] is fixed, recursively call left side and right side
                remaining = dp(left, i - 1) + dp(i + 1, right)
                # update the result
                result = max(result, remaining + gain)
            print('left', left, 'right', right, 'result', result)
            return result

        # we can not burst the first one and the last one
        # since they are both fake balloons added by ourselves
        return dp(1, len(nums) - 2)


print(Solution().maxCoins([3, 1, 5, 8]))
