# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-21 22:51:39
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-21 23:03:04
# @url: https://leetcode.com/problems/multiply-strings/
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dic = {str(i):i for i in range(9)}
        def func(x):
            m = x[::-1]
            res = dic[m[0]]
            for i,v in enumerate(m[1:],start=1):
                res+=dic[v]*(10**i)
            return res
        return str(func(num1)*func(num2))
        return str(int(num1)*int(num2)) # anti-rule
Solution().multiply('123','456')