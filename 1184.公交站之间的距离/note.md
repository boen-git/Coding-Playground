计算一个环的长度, 一个想法是算一个长度, 另外的用全长减去. 值得注意的是列表的长度为`n`, 下标从`0`到`n-1`, 因此在取最后一个元素的时候要注意取余数`%`.

```python
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total = sum(distance)
        forward = 0
        n = len(distance)
        current = start
        while current % n != destination:
            forward += distance[current % n]
            current = current % n + 1
        return min(forward, total - forward)
```


更简洁的写法是:
```python
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int):
        if start > destination:
            start, destination = destination, start
        return min(sum(distance[start:destination]), sum(distance[:start]) + sum(distance[destination:]))
```