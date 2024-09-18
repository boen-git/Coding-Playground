一个想法是遍历passenger, 但是这样在一些特殊的情况下会出现问题:
```python
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses = sorted(buses)
        passengers = sorted(passengers)
        passenger_index = 0
        bus_index = 0
        go = []
        while bus_index < len(buses) and passengers[passenger_index] > buses[bus_index]:
            bus_index += 1
        if bus_index == len(buses): return buses[-1]
        while passenger_index < len     (passengers) and bus_index < len(buses): 
            current_capacity = capacity
            while passenger_index < len(passengers) and bus_index < len(buses) and passengers[passenger_index] <= buses[bus_index] and current_capacity > 0:
                go.append([bus_index, passengers[passenger_index]])
                passenger_index += 1
                current_capacity -= 1
            bus_index += 1
        print(go)
        last_bus_index = max(max(item[0] for item in go), len(buses)-1)
        last_passengers = [item[1] for item in go]
        if max(item[0] for item in go) != len(buses) - 1:
            res = buses[-1]
            while res in last_passengers:
                res -= 1
        elif len(last_passengers) < capacity: 
            res = buses[last_bus_index]
            while res in last_passengers:
                res -= 1
        else: 
            res = max(last_passengers) - 1
            while res in last_passengers:
                res -= 1
        return res
```

模拟的方法如下:

由于最早到达的乘客优先上车, 为了方便模拟, 我们将公交车到达的时间和乘客到达的时间按照先后顺序进行排序. 设第 i 半公交车到达的时间为 buses[i], 此时为上车 且在buses[i] 时刻之前到达的乘客按照时间先后顺序上车, 知道车辆载客人数达到上限capacity为止, 则继续模拟第 i+1 班公交车的乘客上车, 直到所有车辆均模拟完毕,

此时记录最后一班公交车的空位数为 space, 此时有以下的两种情况:
- 如果space > 0, 则表示最后一班公交车发车时车上还有空位, 这意味着我们最晚可以在最后一班公交车发车时候到站即可, 由于不能跟别的乘客同时刻到达, 此时从最后一般发车时刻 buses[n-1] 开始向前找到一个没有乘客到达的时刻即可.

- 如果此时满足 space = 0, 则表示最后一班公交车发车时, 车上没有空位, 这意味着我们最后一个上车的乘客上车以后载客已满, 此时我们从最后一个人上车的乘客到达时间往前找到一个没有乘客到达的时刻即可, 如果到达时间晚于最后一个上车的乘客的到达时间, 则一定无法乘车.

```python
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        pos = 0
        for arrive in buses:
            space = capacity
            while space > 0 and pos < len(passengers) and passengers[pos] <= arrive:
                space -= 1
                pos += 1
        
        pos -= 1
        last_catch_time = buses[-1] idf space > 0 else passengers[pos]
        while pos >= 0 and passengers[pos] == last_catch_time:
            pos -= 1
            last_catch_time -= 1

        return last_catch_time
```

这提醒我们在编程循环的时候, 尽量只循环其中一个, 判断另外一个.