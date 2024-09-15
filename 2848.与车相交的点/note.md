回顾: 列表表达式:`[nums[i][1] for i in range(len(nums))]`

一个直观的想法是: 从头到尾走完.
```
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        def check(i:int) -> bool:
            for j in range(len(nums)):
                if nums[j][0] <= i and i <= nums[j][1]: return True
            return False
        count = 0
        max_length = max([nums[i][1] for i in range(len(nums))])
        for i in range(1, max_length + 1): 
            if check(i): count += 1
        return count
```



另一个想法是: 使用一个数组count表示每个坐标被覆盖的次数, 对于数组中的每个元素, 将count中下标从x到y的元素均增加1, 最后数组count中非零的元素即为答案.

```python
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        C = max(y for _, y in nums)
        count = [0] * (C + 1)
        for x, y in nums:
            for i in range(x, y + 1)
            count[i] += 1
        ans = sum(1 for i in range(1, C + 1) if count[i] > 0)
        return ans
```