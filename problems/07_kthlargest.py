# 215. Kth Largest Element in an Array

# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?

# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

# Constraints:
# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # max heap of size N
        # Time: O(N + klogN)
        # Space: O(1)


        # heapify the list
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            print(heapq.heappop(nums))

        return heapq.heappop(nums)
    

if __name__ == "__main__":
    # nums = [3,2,1,5,6,4]
    # k = 2
    # print(Solution().findKthLargest(nums, k)) # 5

    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    print(Solution().findKthLargest(nums, k)) # 4