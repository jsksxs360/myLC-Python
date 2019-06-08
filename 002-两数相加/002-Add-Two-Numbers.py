from typing import List
import json
import sys
import io

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        p = head
        temp = 0
        while l1 or l2:
            if l1 and l2:
                num = l1.val + l2.val + temp
                p.next = ListNode(num % 10)
                p = p.next
                temp = num // 10
                l1 = l1.next
                l2 = l2.next
            elif l1:
                num = l1.val + temp
                p.next = ListNode(num % 10)
                p = p.next
                temp = num // 10
                l1 = l1.next
            else:
                num = l2.val + temp
                p.next = ListNode(num % 10)
                p = p.next
                temp = num // 10
                l2 = l2.next
        if temp != 0:
            p.next = ListNode(temp)
        return head.next

def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    return dummyRoot.next

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            l1 = stringToListNode(line)
            line = next(lines)
            l2 = stringToListNode(line)
            
            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()