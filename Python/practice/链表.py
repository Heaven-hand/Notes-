class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def initList(self, data):
        # 创建头结点
        self.head = ListNode(data[0])
        r = self.head
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r

    def printlist(self, head):
        if head == None: return
        node = head
        while node != None:
            print(node.val, end=' ')
            node = node.next


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        first = head
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        if l1 != None:
            head.next = l1
        elif l2 != None:
            head.next = l2
        return first.next


if __name__ == '__main__':
    a = Solution()
    l = LinkList()
    data1 = [-1,0,0,0,0,3,3]
    data2 = [2, 4, 6]
    head = l.initList(data1)
    l2 = l.initList(data2)
    # l.printlist(l1)
    # print("\r")
    # l.printlist(l2)
    # print("\r")
    # m = a.mergeTwoLists(l1, l2)
    # l.printlist(m)
    # re = temp = ListNode(None)
    # add = 0
    # while l1 or l2 or add:
    #     add += (l1.val if l1 else 0) + (l2.val if l2 else 0)
    #     temp.next = ListNode(add % 10)
    #     print('test1: ')
    #     l.printlist(temp)
    #     l.printlist(re)
    #     print('\r')
    #     add //= 10
    #     temp = temp.next
    #     print('test2: ')
    #     l.printlist(temp)
    #     l.printlist(re)
    #     print('\r')
    #     l1 = l1.next if l1 else None
    #     l2 = l2.next if l2 else None
    #
    # l.printlist(re.next)
    Hashmap = set()
    while head:
        Hashmap.add(head.val)
        print(Hashmap)
        head = head.next
    data = list(Hashmap)
    print(data)
