# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-19 00:35:28
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-20 00:24:06
# @url: https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/submissions/
from typing import List
from math import lcm

class Solution:

    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n, res = len(nums), 0
        for i in range(n):
            s = nums[i]
            for j in range(i, n):
                if 0 != k % nums[j]:
                    break
                if (s := lcm(nums[j], s)) == k:
                    res += 1
        return res