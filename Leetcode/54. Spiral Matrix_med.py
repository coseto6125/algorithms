# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-21 00:33:20
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-21 01:07:50
from typing import List

# Recursive algorithm
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

# smart for loop 
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        while matrix:
            res+=matrix.pop(0)
            matrix=list(zip(*matrix))[::-1]
        return res    
    
# brute force
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix[0]), len(matrix)
        q,k = 0,0
        res = []
        x = y = 0
        ko = m*n
        rt = 0
        while True:
            while x<m:
                res.append(matrix[y][x])
                rt+=1
                if rt == ko:
                    return res
                x+=1
            x-=1
            m-=1
            y+=1
            while y<n:
                res.append(matrix[y][x])
                rt+=1
                if rt == ko:
                    return res
                y+=1
            y-=1
            n-=1
            x-=1
            while x>q:
                res.append(matrix[y][x])
                rt+=1
                if rt == ko:
                    return res
                x-=1
            q+=1
            while y>k:
                res.append(matrix[y][x])
                rt+=1
                if rt == ko:
                    return res
                y-=1
            y+=1
            x+=1
            k+=1
print(Solution().spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))