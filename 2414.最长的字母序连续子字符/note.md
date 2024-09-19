要找到字符串中的最长子串, 一个直观的想法是去模拟从前到后找到最长子串的过程.
```python
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        longest = []
        ans = 0
        for i in s:
            if len(longest) == 0:
                longest.append(i)
            elif ord(longest[-1]) + 1 == ord(i):
                longest.append(i)
            else:
                ans = max(len(longest), ans)
                longest = []
                longest.append(i)
        ans = max(len(longest), ans)
        return ans
```

但是这样写无论是时间上还是内存上, 开销都比较大, 因此一个更优雅的改进是:
```python
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        res = 1 # 最长的串
        cur = 1 # 当前串的长度
        for i in range(1, len(s)): # 简化考虑, 从第2个元素开始
            if ord(s[i]) == ord(s[i - 1]) + 1:
                cur += 1 # 当前串变长
            else:
                cur = 1 # 切换到下一个串
            res = max(res, cur) # 最长
        return res
```