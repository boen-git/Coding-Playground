执行上述操作任意次, 返回nums中做多可以标记的下标数.

一个直观的想法是:
```python
class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if 2 * nums[i] <= nums[j]:
                    count += 1
        return count
```