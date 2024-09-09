## 单向链表也叫单链表, 是链表中最简单的一种形式.
## 信息域 + 链接域

## Node

class Node(object):
    def __init__(self, elem):
        # _elem存放元素
        self.elem = elem
        # _next存放下一个节点的标识
        self.next = None

## 测试
## 实现单向链表

class SingleLinkList(object):
    ## 构造函数
    def __init__(self):
        self._head = None
    ## 判断链表是否为空
    def is_empty(self):
        return self._head == None
    ## 链表长度
    def length(self):
        cur = self._head
        count = 0
        while cur!= None:
            count += 1
            cur = cur.next
        return count
    ## 输出链表
    def print(self):
        cur = self._head
        while cur != None:
            print(cur.elem, end=' ')
            cur = cur.next
        print('\n')
        return None
    ## 头部添加元素
    def add(self, elem):
        node = Node(elem)
        node.next = self._head
        self._head = node

    ## 尾部添加元素
    def append(self, elem):
        node = Node(elem)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    ## 插入元素
    def insert(self, pos, elem):
        if pos <= 0:
            self.add(elem)
        elif pos > (self.length()-1):
            self.append(elem)
        else:
            node = Node(elem)
            cur = self._head
            count = 0
            while count < (pos-1):
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    ## 删除元素
    def remove(self, elem):
        cur = self._head
        pre = None
        while cur != None:
            if cur.elem == elem:
                if not pre:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
    ## 查找元素是否存在
    def search(self, elem):
        cur = self._head
        while cur != None:
            if cur.elem == elem:
                return True
            cur = cur.next
        return False
    

## 测试
if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.print()
    ll.add(6)
    ll.print()
    ll.insert(3, 7)
    ll.print()
    ll.remove(7)
    ll.print()
    
    