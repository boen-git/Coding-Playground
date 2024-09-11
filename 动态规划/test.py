# def L(nums, i):
#     '''Returns the length of longest increasing subsequence starting from i.'''
#     if i == len(nums) - 1: # Last element
#         return 1
#     max_len = 1
#     for j in range(i + 1, len(nums)):
#         if nums[j] > nums[i]:
#             max_len = max(max_len, 1 + L(nums, j))
#     return max_len 

# def LIS(nums):
#     '''Returns the length of longest increasing subsequence.'''
#     return max(L(nums, i) for i in range(len(nums)))

# nums = [1,5,2,4,3]
# print(LIS(nums)) # 3


# import random
# import time
# random.seed(42)
# def generate_unique_list(length=90):
#     unique_list = []
#     while len(unique_list) < length:
#         new_num = random.randint(1, 1000)  # 可以根据需要调整随机数的范围
#         if new_num not in unique_list:
#             unique_list.append(new_num)
#     return unique_list

# test_list = generate_unique_list()
# print(test_list)

# start_time = time.time()
# print(LIS(test_list))
# print("Took {:.4f} seconds.".format(time.time() - start_time))

memo = {}

def L(nums, i):
    '''Returns the length of longest increasing subsequence starting from i.'''
    if i in memo:
        return memo[i]
    if i == len(nums) - 1: # Last element
        return 1
    max_len = 1
    for j in range(i + 1, len(nums)):
        if nums[j] > nums[i]:
            max_len = max(max_len, 1 + L(nums, j))
    memo[i] = max_len
    return max_len 

def LIS(nums):
    '''Returns the length of longest increasing subsequence.'''
    return max(L(nums, i) for i in range(len(nums)))

nums = [1,5,2,4,3]
print(LIS(nums)) # 3

import random
import time
random.seed(42)
def generate_unique_list(length=90):
    unique_list = []
    while len(unique_list) < length:
        new_num = random.randint(1, 1000)  # 可以根据需要调整随机数的范围
        if new_num not in unique_list:
            unique_list.append(new_num)
    return unique_list

test_list = generate_unique_list()
print(test_list)

start_time = time.time()
print(LIS(nums))
print("Took {:.4f} seconds.".format(time.time() - start_time))

print(list(i for i in range(10, -1, -1)))


def length_of_LIS(nums):
    n = len(nums)
    L = [1] * n # Initialize the list with 1
    for i in range(n, -1, -1):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                L[i] = max(L[i], 1 + L[j])

    return max(L)

start_time = time.time()
print(length_of_LIS(nums))
print("Took {:.4f} seconds.".format(time.time() - start_time))