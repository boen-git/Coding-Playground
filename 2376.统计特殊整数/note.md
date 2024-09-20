如果一个正整数每一个数位都是 互不相同 的，我们称它是 特殊整数 。

如果一个一个去判断, 非常容易超时.
```python
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        def has_repeat_num(i: int) -> bool:
            digits = []
            while i > 0:
                cur = i % 10
                if cur in digits:
                    return False
                else: 
                    digits.append(cur)
                i //= 10
            return True
        if n < 100:
            count = 0
            for num in range(1,n+1):
                if num % 11 == 0:
                    count += 1
            return n - count
        count = 0
        for i in range(1, n+1):
            if has_repeat_num(i):
                count += 1
        return count
```

一个节省时间的办法是使用组合数学+动态规划.

要返回[1, n]之间的特殊整数的数目, 即小于等于n的没有重复数字的数. 记n的十进制下的位数为k, 可以考虑两种情况:
- 位数小于 k 的整数
- 位数等于 k 的整数

对于位数小于 k 的情况, 分别计算位数为 1 到 k - 1 的情况下特殊整数的数量.
考虑位数为 $k_0 < k$ 的情况, 任意放置数位上的数字, 都能满足 <= n 的条件, 只需保证每一数位都互不相同. 用组合数学的思路求解特殊整数的数量, 最高位有 9 种选择, 次高位有 9 种选择, 以此类推.

接下来考虑位数等于 k 的特殊整数, 相同位数的数字比较大小, 是从最高位开始比较, 若不同, 则最高位大的数字大, 若相同, 则比较次高位.

函数 dp(mask, prefixSmaller) 用来计算以某些数字组合为前缀的特殊整数的数量. 整数mask 即表示了前缀中是用过的数字, 二进制表示下, 从最低位开始, 第 i 为前缀是否小于n的前缀, 如果是, 则接下来的数字可以任意选择, 如果不是, 即当前的前缀等于n的前缀, 则接下来只能小于或者等于 n 同数位的数字. 最后调用 dp(0, false), 则为位数等于 k 的特殊整数的数量.

在 Python 中，@cache通常是指使用functools.lru_cache装饰器对函数进行缓存。

它的主要作用是通过缓存函数的调用结果来提高程序的性能。当使用这个装饰器装饰一个函数时，函数的参数和返回值会被缓存起来。如果后续以相同的参数调用该函数，就可以直接从缓存中获取结果，而不需要再次执行函数体中的代码。

在 Python 的 int 类型中，有一个方法叫做 bit_length()，它返回一个整数的二进制表示形式的位数长度。

在 Python 中，“<<” 是位运算符，表示按位左移。
按位左移运算将一个数的二进制表示向左移动指定的位数。例如，x << n表示将整数x的二进制表示向左移动n位。

```python
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        @cache
        def dp(mask: int, prefixSmaller: bool) -> int:
            if mask.bit_count() == len(nStr):
                return 1
            res = 0
            lowerBound = 1 if mask == 0 else 0
            upperBound = 9 if prefixSmaller else int(nStr[mask.bit_count()])
            for i in range(lowerBound, upperBound + 1):
                if mask >> i & 1 == 0:
                    res += dp(mask | 1 << i, prefixSmaller or i < upperBound)
            return res

        nStr = str(n)
        res = 0
        prod = 9
        for i in range(len(nStr) - 1):
            res += prod
            prod *= 9 - i
        res += dp(0, False)
        dp.cache_clear()
        return res

```

用dfs

```python
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, mask: int, is_limit: bool, is_num: bool) -> int:
            if i == len(s):
                return 1 if is_num else 0  # is_num 为 True 表示得到了一个合法数字
            res = 0
            if not is_num:  # 可以跳过当前数位
                res = dfs(i + 1, mask, False, False)
            # 如果前面没有填数字，则必须从 1 开始（因为不能有前导零）
            low = 0 if is_num else 1
            # 如果前面填的数字都和 n 的一样，那么这一位至多填 s[i]（否则就超过 n 啦）
            up = int(s[i]) if is_limit else 9
            for d in range(low, up + 1):  # 枚举要填入的数字 d
                if mask >> d & 1 == 0:  # d 不在 mask 中，说明之前没有填过 d
                    res += dfs(i + 1, mask | (1 << d), is_limit and d == up, True)
            return res

        return dfs(0, 0, True, False)
```