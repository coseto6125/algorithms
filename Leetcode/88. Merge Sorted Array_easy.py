# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-21 22:21:35
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-21 22:21:57
# @url: https://leetcode.com/problems/merge-sorted-array/
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()