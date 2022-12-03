# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-23 22:01:15
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-23 22:01:51
# @url: https://leetcode.com/problems/reverse-string/
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        s.reverse()
        '''
        s[:] = s[::-1]'''