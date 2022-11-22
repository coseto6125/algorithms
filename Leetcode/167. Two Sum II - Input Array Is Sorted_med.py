# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-22 23:01:13
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-22 23:33:29
# @url: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from bisect import bisect_left
from typing import List


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ls = len(numbers)
        for i in range(ls):
            tk = target - numbers[i]
            m = bisect_left(numbers, tk)
            if m < ls and (numbers[m] == tk):
                return [i + 1, m + 1 if i != m else m + 2]


print(Solution().twoSum([0, 0, 3, 4], 0))
