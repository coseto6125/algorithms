# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-21 01:15:43
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-21 01:16:22
from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        v = [-1]*n
        for i in range(n):
            cur = i
            next = -1
            for j in range(m):
                next = cur+grid[j][cur]
                if(next<0 or next >=n or grid[j][cur]!=grid[j][next]):
                    cur = -1
                    break
                cur = next
            v[i]=cur
        return v