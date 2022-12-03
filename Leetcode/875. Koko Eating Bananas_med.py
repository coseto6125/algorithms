# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-24 20:48:21
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-24 21:34:02
from bisect import bisect_left
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ls = len(piles)
        if ls == h:
            return 
        if ls == 1:
            return 2
        r,l = 1,max(piles)
        while r<=l:
            m =sum(map(lambda x:x//s+1,piles))
            if m == h:
                return s-1
            if m > h:
                s+=1
            if m < h:
                s-=1
        return 
Solution().minEatingSpeed([312884470]
,312884469
)