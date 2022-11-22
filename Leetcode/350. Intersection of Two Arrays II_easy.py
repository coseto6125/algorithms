# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-22 23:39:41
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-23 00:04:55
# @url: https://leetcode.com/problems/intersection-of-two-arrays-ii/
from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) <len(nums2):
            base = nums1
            flag = Counter(nums2)
        else:
            base = nums2
            flag = Counter(nums1)
        res = []
        for i in base:
            if flag[i] >0:
                flag[i]-=1
                res.append(i)
        return res
