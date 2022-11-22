# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-22 00:25:53
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-23 00:41:48
# @url: https://leetcode.com/problems/find-k-closest-elements/
from typing import List
class Solution:
    def findClosestElements(self, A: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(A) - k
        while left < right:
            mid = int((left + right) / 2)
            if x - A[mid] > A[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return A[left:left + k] 
Solution().findClosestElements([1,1,1,10,10,10],1,9
)