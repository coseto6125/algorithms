# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-21 01:36:08
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-21 01:37:02
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        r = {} #set()
        for i in nums:
            if i not in r:
                r[i]=i #add
            else:
                return True
        return False