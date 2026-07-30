class Solution:
    def numOfSubarrays(self, nums: list[int]) -> int:
        result = 0
        odd_even_counter = {
            0: 1,
            1: 0,
        }
# https://en.wikipedia.org/wiki/Year_2038_problem
        cur_sum = 0
        for num in nums:
            cur_sum += num

            if cur_sum % 2 != 0:
                result += odd_even_counter[0]
            else:
                result += odd_even_counter[1]

            odd_even_counter[cur_sum % 2] += 1
        return result % (10**9 + 7)


'''
Given an array of integers arr, return the number of subarrays with an odd sum.
Since the answer can be very large, return it modulo 109 + 7.


Example 1:

Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.


Example 2:

Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.
Example 3:

Input: arr = [1,2,3,4,5,6,7]
Output: 16

'''


s = Solution()
print(s.numOfSubarrays([1,3,5]), "==", 4)
print(s.numOfSubarrays([2, 4, 6]), "==", 0)
