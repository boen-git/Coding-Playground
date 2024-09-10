## One naive idea is to use 4 loops to iterate all possible combinations of 4 elements in the array.
## However, this solution is not efficient enough. We can improve it by using a hash table to store the number of elements that are less than the current element.

def my_countQuadruplets(nums) -> int:
        flag = 0
        n = len(nums)
        for i in range(0, n-3):
            for j in range(i+1, n-2):
                for k in range(j+1, n-1):
                    for l in range(k+1, n):
                        # print('i: ', i, 'j: ', j, 'k: ', k, 'l: ', l)
                        if nums[i] < nums[k] and nums[k] < nums[j] and nums[j] < nums[l]:
                            flag += 1
        return flag


def countQuadruplets(nums) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        ans = 0
        for j in range(n):
            suf = 0
            for k in range(n - 1, j, -1): 
                if nums[j] > nums[k]:
                    ans += pre[nums[k]] * suf 

                else:
                    suf += 1
            for x in range(nums[j] + 1, n + 1):
                pre[x] += 1
        return ans


if __name__ == '__main__':
    nums = [1,3,2,4,5]
    nums_1 = [1,2,3,4]
    print(countQuadruplets(nums))
    print(countQuadruplets(nums_1))
    
    