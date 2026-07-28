from itertools import islice


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        result = 0
        for i in range(len(nums)):
            tmp = 0
            for j in range(i, len(nums)):
                tmp += nums[j]
                if tmp == k:
                # if sum(islice(nums, i, j+1)) == k:
                    # print(i,j, nums[i:j + 1])
                    result += 1

        # for ji in range(i, len(nums)):
        #     tmp += nums[j]
        #     if tmp == k:
        #     # if sum(islice(nums, i, j+1)) == k:
        #         # print(i,j, nums[i:j + 1])
        #         result += 1
        return result

    def subarraySum2(self, nums: list[int], target: int) -> int:
        from collections import defaultdict

        total = 0
        prefix_sum = 0
        prefix_sums_counter = defaultdict(int)
        prefix_sums_counter[0] = 1

        for end in range(len(nums)):
            prefix_sum += nums[end]
            complement_sum = prefix_sum - target    # 12 - 7 == 5

            print(nums[end], prefix_sum, prefix_sums_counter)

            # количество отрезков, которые заканчиваются индексом end
            # и их сумма равна k
            end_total = 0
            if complement_sum in prefix_sums_counter:
                end_total = prefix_sums_counter[complement_sum]

            # общее количество всех отрезков с суммой k
            # равно сумме отрезков с суммой k для каждого end
            total += end_total

            prefix_sums_counter[prefix_sum] += 1

        return total

    def subarraySum3(self, nums: list[int], target: int) -> int:
        from collections import defaultdict
        result = []
        prefix_sum = 0

        prefix_sum_indexes = defaultdict(list)
        prefix_sum_indexes[0] = [-1]

        for end in range(len(nums)):
            prefix_sum += nums[end]
            complement_sum = prefix_sum - target    # 12 - 7 == 5

            if complement_sum in prefix_sum_indexes:
                for i in prefix_sum_indexes[complement_sum]:
                    print("i =", i, "end =", end)
                    result.append(nums[i+1:end+1])
            # print(nums[end], prefix_sum, prefix_sums_counter)

            # общее количество всех отрезков с суммой k
            # равно сумме отрезков с суммой k для каждого end

            prefix_sum_indexes[prefix_sum].append(end)
        return result

# https://en.wikipedia.org/wiki/List_of_presidents_of_France#Presidents_of_the_Republic

# days[A:B] + days[B:C] == days[A:C]

# [A, B] → 100 дней
# [B, C] → 150 дней
# [C, D] → 200 дней
# [A, D] → 448 дней

#
#                    ↓     ↓
#  0   2  5   1  7   5  7 12  22  15 23  20
#      2  3  -4  6  -2  2  5  10  -7  8  -3
#  ---------------
#         ------------------
#                   --------

# target = 7

#  2 2         {0: 1}
#  3 5         {0: 1, 2: 1}
# -4 1         {0: 1, 2: 1, 5: 1}
#  6 7         {0: 1, 2: 1, 5: 1, 1: 1}
# -2 5         {0: 1, 2: 1, 5: 1, 1: 1, 7: 1}
#  2 7         {0: 1, 2: 1, 5: 2, 1: 1, 7: 1}
#  5 12        {0: 1, 2: 1, 5: 2, 1: 1, 7: 2}
# 10 22        {0: 1, 2: 1, 5: 2, 1: 1, 7: 2, 12: 1}
# -7 15        {0: 1, 2: 1, 5: 2, 1: 1, 7: 2, 12: 1, 22: 1}
#  8 23        {0: 1, 2: 1, 5: 2, 1: 1, 7: 2, 12: 1, 22: 1, 15: 1}
# -3 20        {0: 1, 2: 1, 5: 2, 1: 1, 7: 2, 12: 1, 22: 1, 15: 1, 23: 1}


#  0   2  5   1  7   5  7 12  22  15 23  20
#      2  3  -4  6  -2  2  5  10  -7  8  -3
#                       ----
#            ---------------

#       ?          7
#  ----------- --------
#  --------------------
#            12

#     target == 7

# N == len(nums) == 5

# i = 0 → num[0:j+1] → N == 5
# i = 1 →              N-1 == 4
# i = 2 →              N-2 == 3
# i = 3 →              N-3 == 2
# i = 4 →              N-4 == 1


# 5 + 4 + 3 + 2 + 1 == 15

# N + N-1 + N-2 + ... + 1 == (N + 1) × N ≈ N²/2

# 1000 + 999 + 998 + ... + 3 + 2 + 1 == 1001 × 500 = 500500

# 00000
# _
# __
# ___
# ____
# _____
#  _


# # 60 × 60 × 24
# N = 100

# zeroes = [0] * N

# import tracemalloc
# from time import perf_counter

# tracemalloc.start()
# start = perf_counter()
# s1 = Solution()
# s1.subarraySum(zeroes, 0)
# print(perf_counter() - start)
# print(tracemalloc.get_traced_memory())
# tracemalloc.stop()

# 500 → 175_695_480 || 4504
# 1000 → 1_369_531_016 || 8504  || islice 696

# 1000 × 1000/2 → 500_000 × 500 × 4 bytes ≈ 1_000_000_000

# 1_000 3.0533911249949597

    # def subarraySum(self, nums: list[int], k: int) -> int:
    #     prefix_sum = [0]
    #     for num in nums:
    #         prefix_sum.append(prefix_sum[-1] + num)

    #     sub_arrays = []
    #     left = 0

    #     for right in range(1, len(prefix_sum)):

    #         while prefix_sum[right] - prefix_sum[left] > k:
    #             left += 1

    #         if prefix_sum[right] - prefix_sum[left] == k and left != right:
    #             sub_arrays.append([left, right])

    #     return sub_arrays




s1 = Solution()
# print(s1.subarraySum2([2, 3,  -4,  6,  -2,  2,  5,  10,  -7,  8,  -3], target=7))
print(s1.subarraySum3([2, 3,  -4,  6,  -2,  2,  5,  10,  -7,  8,  -3], target=7))

# print(s1.subarraySum2([1,1,1], 2), "==", "2")
# print(s1.subarraySum2([1,2,3], 3), "==", "2")
# print(s1.subarraySum2([1], 0), "==", "0")
# print(s1.subarraySum2([-1,-1,1], 0), "==", "1")



# The key insight is that if prefixSum[j] - prefixSum[i] = k, then the subarray from index i+1 to j has sum k
# 1    -2    5    1       → array
# 0    1    -1    4    5  → prefix sum
# 0    1    2    3    4  → index

# k = 4
# prefixSum[3] - prefixSum[1] == k  → array[2] + ... + array[3] = k
