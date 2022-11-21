# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-22 00:01:33
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-22 00:06:01
# @url: https://leetcode.com/problems/minimum-size-subarray-sum/
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target in nums: return 1
        cms,ls = sum(nums),len(nums)
        if cms == target: return ls
        if cms < target: return 0
        
        res = float('inf')
        curSum = left = 0
        for right in range(ls):
            curSum += nums[right]
            while left <= right and curSum >= target:
                res = min(res, right-left+1)
                curSum -= nums[left]
                left += 1
        return 0 if res == float('inf') else res
Solution().minSubArrayLen(6,[10,2,3]
)