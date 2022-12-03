# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-19 00:06:41
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-12-04 03:47:22
# @url: https://leetcode.com/problems/first-missing-positive/description/
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        k = {i for i in nums if i>0}
        m = set(range(1,len(k)+2))
        return min(k^m)