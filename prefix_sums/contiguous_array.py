"""
Contiguous Array

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.


Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Example 3:

Input: nums = [0,1,1,1,1,1,0,0,0]
Output: 6
Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.
 """

class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        result = 0
        ones = 0
        zeroes = 0
        diff_index = {0: -1}

        for i in range(len(nums)):
            if nums[i] == 1:
                ones += 1
            else:
                zeroes += 1

            if ones - zeroes not in diff_index:
                diff_index[ones - zeroes] = i

            idx = diff_index[ones - zeroes]
            result = max(result, i - idx)

        return result



s = Solution()
print(s.findMaxLength([0,1]), "==", 2)
print(s.findMaxLength([0,1,0]), "==", 2)
print(s.findMaxLength([0,1,1,1,1,1,0,0,0]), "==", 6)

#
# nums  = [0, 1, 1, 1, 1, 1, 0, 0, 0]
#             ---------------------------
# Основная идея - считаем разницу между кол-вом единиц и нулей, и если на индексах   i  и  j  эта разница равна,
# значит внутри отрезка nums[i:j+1] сумма разниц кол-ва 0 и 1 равна 0, то есть кол-во 0 и 1 равно.
#                  dif  index
#                  {0: -1}
#
# i   1s  0s
# 0   0 - 1  → -1  {-1: 0}
# 1   1 - 1  →  0  in map → res = current index - map[dif]  → 1 -(-1) == 2
# 2   2 - 1  →  1  {1: 2}
# 3   3 - 1  →  2  {2: 3}
# 4   4 - 1  →  3  {3: 4}
# 5   5 - 1  →  4  {4: 5}
# 6   5 - 2  →  3  in map → 6 - 4 = 2
# 7   5 - 3  →  2  in map → 7 - 3 = 4
# 8   5 - 4  →  1  in map → 8 - 2 = 6
