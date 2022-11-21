# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-21 22:17:17
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-21 22:17:58
# @url: https://leetcode.com/problems/two-sum/
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        c = 0
        for i in nums:
            m = target-i
            if numMap.__contains__(m):
                return [numMap[m],c]
            numMap[i] = c
            c +=1