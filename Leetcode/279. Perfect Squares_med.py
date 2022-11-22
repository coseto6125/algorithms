# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-23 01:58:15
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-23 02:48:12
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
        if (n & 0b111) == 0b111: #n % 8 == 7
            return 4
        return 3