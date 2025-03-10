# Title: 'Two Sum'
# Author: Rishin Rahim <rishin07@gmail.com>
# Created: 2021-03-22
# Difficulty : Easy
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 10^3
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.

'''

class Solution:
    
    def twoSum(self, nums: list, target: int) -> list:
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in nums[i+1:]:
                k = nums[i+1:].index(dif) + i+1
                return [i,k]
        return "No two sum solution"
    
    


                
                
        
                
        
            
        

