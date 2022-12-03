# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-23 22:42:41
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-23 23:10:00
# @url: https://leetcode.com/problems/reshape-the-matrix/
from itertools import chain
from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c == len(mat)*len(mat[0]):
            s = list(chain(*mat))
            return [s[i:i+c] for i in range(0, len(s), c)]
        return mat
Solution().matrixReshape([[1,2,3,4]]
,2,2)