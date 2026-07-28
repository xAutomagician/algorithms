from itertools import islice
# https://leetcode.com/problems/range-sum-query-immutable/description/


class NumArray:
    # N == len(nums)
    # time O(1)   space O(1)
    # def __init__(self, nums):
    #     self.nums = nums

    # time O(n)   space O(n)
    def __init__(self, nums):
        self.prefix_sums = [0]
        for num in nums:
            self.prefix_sums.append(self.prefix_sums[-1] + num)

        # print(self.prefix_sums)

    # slice  → space O(N)  time(N)
    # islice → space O(1)  time(N)
    # K calls
    def sumRange(self, left, right):
        # return sum(self.nums[left:right+1])
        # s = 0
        # for i in range(left, right + 1):
        #     s += self.nums[i]
        # return s
        return self.prefix_sums[right + 1] - self.prefix_sums[left]


# na1 = NumArray([-2,3,-5,2,-1,8])  # space O(1)  time O(1)


# prefix_sums[i] == sum(nums[0:i]) == nums[0] + nums[1] + ...  nums[i-1]
# сумма элементов с индексами до i (не включительно)

#    0   -2    1    -4   -2    -3    5    ← prefix_sums
#        -2    3    -5    2    -1    8    ← nums
#         0    1     2    3     4    5    ← index
#                   [-----------]
#                   L           R

# sum(nums[0:R+1])  ==  prefix_sums[R+1]  ==  nums[0] + nums[1] + ...  nums[R]
# sum(nums[0:L])    ==  prefix_sums[L]    ==  nums[0] + nums[1] + ...  nums[L-1]

# print(na1.sumRange(0,2), "==", "-4")  # space O(1)  time O(N)
# print(na1.sumRange(2,4), "==", "-4")
# print(na1.sumRange(3,3), "==", "2")
# print(na1.sumRange(3,5), "==", "9")

from time import perf_counter

N = 100_000_000
K = 5_000

ones = [1] * N
# # 60 × 60 × 24
# # space O(1) time O(N×K)


na2 = NumArray(ones)

start = perf_counter()

for k in range(K):
    na2.sumRange(0, N - 1)

print(perf_counter() - start)


# 10_000      0.0005221670144237578
# 10_000      0.0005381660303100944
# 100_000_000 0.000557416002266109
# 10          0.0006867920164950192


# 100_000 - .784716083027888
# 100_000   - 0.00057
# 1_000_000 - 0.000541166984476149
