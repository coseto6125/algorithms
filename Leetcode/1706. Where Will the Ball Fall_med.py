# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-21 01:15:43
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-12-04 03:48:46
from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        v = [-1]*n
        for i in range(n):
            cur = i
            next_n = -1
            for j in range(m):
                next_n = cur+grid[j][cur]
                if(next_n<0 or next_n >=n or grid[j][cur]!=grid[j][next_n]):
                    cur = -1
                    break
                cur = next_n
            v[i]=cur
        return v