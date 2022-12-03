# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-18 23:38:45
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-12-04 03:47:15
# @url: https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1+nums2)
        n = len(nums)
        i = n // 2
        return nums[i] if n & 1 else (nums[i - 1] + nums[i]) / 2
    
Solution().findMedianSortedArrays([1,3],[2])
Solution().findMedianSortedArrays([1,3],[3,4])
