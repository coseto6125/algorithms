# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-23 22:16:40
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-23 22:17:38
# @url: https://leetcode.com/problems/odd-even-linked-list/
from typing import Optional

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd, even = head, head.next
        evenHead = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
          
        odd.next = evenHead
        return head