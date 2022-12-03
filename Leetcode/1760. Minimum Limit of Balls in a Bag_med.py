# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-23 21:57:10
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-23 21:57:52
# @url: https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/
from typing import List
import numpy as np

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        nums = np.array(nums, np.int)
        lo, hi = 1, nums.max()
        nums -= 1
        while lo < hi:
            mid = (lo + hi) // 2
            ops = np.sum(nums // mid)
            lo, hi = (lo, mid) if ops <= maxOperations else (mid + 1, hi)
        return lo