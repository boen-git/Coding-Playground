给出若干公交路线. 求出换乘次数.

## 运算符
（&，|） 和 （and，or）是两组比较相似的运算符。他们的用法如下：
&、| 支持set集合运算

如果a与b是两个set集合，则可以做如下运算：

a与b的交集
In [265]: a = {'a','b','c'}
In [266]: b = {'c','d'}

In [267]: a & b
Out[267]: {'c'}
a与b的并集
In [268]: a|b
Out[268]: {'a', 'b', 'c', 'd'}
除了 &、| 之外，set集合也支持 -、^ 运算

a与b的差集：在集合a存在，不在集合b存在的元素

In [269]: a-b
Out[269]: {'a', 'b'}
a与b的异或

In [270]: a^b
Out[270]: {'a', 'b', 'd'}
a与b的异或,可以理解为先求出只存在于a的元素集合，在求出只存在于b的元素集合，然后取并集

异或是指相同为1，不同为0

但是, 和and, or 有区别
```python
>>> a = set([1,2,3]) 
>>> b = set([2,4,5])
>>> a & b
{2}
>>> a and b
{2, 4, 5}
>>>
```

## 广度优先
```python
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # 记录经过车站 x 的公交车的编号
        stop_to_buses = defaultdict(list)
        for i, route in enumerate(routes):
            for x in route: stop_to_buses[x].append(i)
        # 如果没有公交车经过起点或终点, 直接返回
        if source not in stop_buses or target not in stop_to_buses:
            return -1 if source != target else 0
        # 广度优先搜索
        dis = {source: 0}
        q = deque([source])
        while q:
            x = q.popleft() # 当前在车站 x
            dis_x = dis[x]
            for i in stop_to_buses[x]:
                if routes[i]:
                    for y in routes[i]: # 遍历公交车 i 的路线
                        if y not in dis: # 没有访问过车站 y
                            dis[y] = dis_x + 1
                            q.append(y)
                    routes[i] = None
        return dis.get(target, -1)

```


