给你一个包含若干星号 * 的字符串 s 。

在一步操作中，你可以：

选中 s 中的一个星号。
移除星号 左侧 最近的那个 非星号 字符，并移除该星号自身。
返回移除 所有 星号之后的字符串。

注意：

生成的输入保证总是可以执行题面中描述的操作。
可以证明结果字符串是唯一的。


一个直观的想法是:
```python
 def removeStars(self, s: str) -> str:
        n = len(s)
        flag = [1] * n
        ans = ''
        for elem in range(n):
            if s[elem] == '*':
                p = elem - 1
                while flag[p] == 0:
                    p -= 1
                flag[p] = 0
                flag[elem] = 0
        # return flag
        for index, char in enumerate(s):
            if flag[index] == 1:
                ans += char
        return ans

```

但是这样时间开销大, 直接使用栈即可.

```python
def removeStars(self, s: str) -> str:
        res = []
        for c in s:
            if c != '*':
                res.append(c)
            elif res:
                res.pop()
        return ''.join(res)
```