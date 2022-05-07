from typing import List
import heapq

# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/


class Solution:
    # TC = O(nums1 * k)
    # def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    #     nums1_pairs = [0] * len(nums1)
    #
    #     output = []
    #     for _ in range(k):
    #         min_pair = None
    #         for i in range(len(nums1)):
    #             if nums1_pairs[i] < len(nums2):
    #                 if min_pair is None:
    #                     min_pair = i
    #                 elif (nums1[i] + nums2[nums1_pairs[i]]) < (nums1[min_pair] + nums2[nums1_pairs[min_pair]]):
    #                     min_pair = i
    #
    #         if min_pair is None:
    #             break
    #
    #         output.append([nums1[min_pair], nums2[nums1_pairs[min_pair]]])
    #         nums1_pairs[min_pair] += 1
    #
    #     return output


    # TC = O(log(nums1) * k)
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        nums1_heap = []
        for i in range(len(nums1)):
            heapq.heappush(nums1_heap, [nums1[i] + nums2[0], i, 0])

        output = []
        while nums1_heap and k > 0:
            _, nums1_idx, nums2_idx = heapq.heappop(nums1_heap)
            if nums2_idx + 1 < len(nums2):
                pair_sum = nums1[nums1_idx] + nums2[nums2_idx + 1]
                heapq.heappush(nums1_heap, [pair_sum, nums1_idx, nums2_idx + 1])
            output.append([nums1[nums1_idx], nums2[nums2_idx]])
            k -= 1
        return output
