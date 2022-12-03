# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-23 22:21:09
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-23 22:21:42
# @url: https://leetcode.com/problems/sort-list/

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        if not head:
            return head
        while(head):
            a.append(head.val)
            head=head.next
        a.sort()
        head = ListNode(','.join(map(str,a)))
        return head