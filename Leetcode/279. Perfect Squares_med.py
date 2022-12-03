# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-23 01:58:15
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-12-04 03:47:08
# @url: https://leetcode.com/problems/perfect-squares/submissions/

class Solution:
    def numSquares(self , n):
        if (t:=int(n**0.5))**2 == n:
            return 1
        for j in range(t+1):
            if int((ms:=n - j * j)**0.5)**2 == ms:
                return 2
        while not n & 0b11: #n % 4 == 0
            n >>= 2
        return 4 if (n & 0b111) == 0b111 else 3