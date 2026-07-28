

class Solution:
    def pivotIndex(self, nums):

        # prefix_sum = [0]
        # for num in nums:
        #     prefix_sum.append(prefix_sum[-1] + num)

        # total_sum = prefix_sum[-1]

        # prefix_sum[i] = sum(nums[0:i])

        # ---------------
        #           =====
        # 0 1 2 3 4 5 6 7  ← i in nums
        #         i
        # ---------

        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            # left_sum = sum(nums[:i])
            right_sum = total_sum - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1


# solution = Solution()
# # print(solution.pivotIndex([1, 7, 3, 6, 5, 6]), "==", 3)


# # # 60 × 60 × 24
# N = 100_000

# # # space O(1) time O(N×K)
# zeroes = [0] * N
# # zeroes = zeroes + [1]
# zeroes.append(1)

# from time import perf_counter

# start = perf_counter()

# answer = solution.pivotIndex(zeroes)
# print(answer)
# print(perf_counter() - start)


# O(N)
# 1_000_000  →   0.048409749986603856  0.04s
# 10_000_000  →  0.4407682500022929    0.4s
# 100_000_000  → 4.11032974999398      4s


# O(N²)
# 10_000      0.1903181660163682
# 50_000      4.533670457982225
# 100_000     17.898149334010668
# 1_000_000   0.5h
# 10_000_000  50h ≈ 2d
# 100_000_000 200d ≈ 7months


#      1     7     3     6     5     6  <- nums
#  0   1     8     11    17    22    28  <- prefix sum
#  0   1     2     3     4     5     6   <- index
#          [--------------------------]
#          L                           R