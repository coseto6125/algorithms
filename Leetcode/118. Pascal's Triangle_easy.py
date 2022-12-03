# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-23 23:12:09
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-23 23:13:05
# @url: https://leetcode.com/problems/pascals-triangle/
from math import factorial as f

class Solution:
    def generate(self, n: int) -> List[List[int]]:
        return [[(f(i)//(f(j)*f(i-j)))for j in range(i+1)] for i in range(n)]