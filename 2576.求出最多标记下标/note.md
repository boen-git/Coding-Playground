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

容易发现, 如果我们能找到k对标记, 则一定能找到k-1对标记, 如果我们找不到k对标记, 也一定找不到k+1对标记, 因此答案具有单调性, 可使用二分求解.

首先二分枚举m, 然后尝试将最小的m个数字和最大的m个数尝试匹配, 这样做的原因在于, 我们可以证明, 我们可以证明若能找到m对标记, 那么最小的m个数字和最大的m个数字一定可以匹配.

(也就是说, 原始序列的排序无所谓)

因此, 首先对nums进行排序, 然后将下标[0, m-1]范围内的每个nums[i], 与下标[n-m, n-1]范围内的每个nums[j]尝试进行匹配. 若所有的元素都可成功匹配, 则判定可以找到m组匹配.

