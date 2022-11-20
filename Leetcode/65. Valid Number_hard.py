# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-18 23:48:35
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-18 23:48:48
# @url: https://leetcode.com/problems/valid-number/description/
class Solution:
    def isNumber(self, s: str) -> bool:
        try: 
            float(s)
            return s if 'nf' not in s else False
        except:
            return False