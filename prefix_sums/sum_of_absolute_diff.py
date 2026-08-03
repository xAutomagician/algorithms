class Solution:
    def getSumAbsoluteDifferences(self, nums):
        result = []
        for i, num1 in enumerate(nums):
            tmp = 0
            for j, num2 in enumerate(nums):
                if i == j:
                    continue
                tmp += abs(num1 - num2)
            result.append(tmp)
        return result

    def getSumAbsoluteDifferences1(self, nums):
        result = []

        total = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            right_sum = total - left_sum - num

            abs_diff = (num * i - left_sum) + right_sum - num * (len(nums) - (i + 1))
            result.append(abs_diff)
            left_sum += num

        return result


s1 = Solution()
print(s1.getSumAbsoluteDifferences1([2, 3, 5]))
print([4,3,5])
print()
print(s1.getSumAbsoluteDifferences1([1, 4, 6, 8, 10]))
print([24,15,13,15,21])



# nums = [1,    4,    5,    7,    9,    13,    21]
#       ×
#      1-0   4-1   5-1    7-1   9-1   13-1   21-1
#      [            ×                          ]

#                  i=2

#     5-1    5-4   5-5   5-7   5-9   5-13   5-21
#     ----------------   7-5   9-5   13-5   21-5
#                        -----------------------
#     5×3 - (1 + 4 + 5)  (7 + 9 + 13 + 21) - 5×4

#     nums[i] * (i+1) - sum(nums[0:i+1])    sum(nums[i+1:]) -  nums[i] * (len(nums) - (i + 1))
#     nums[i] * (i+1) - sum(nums[0:i+1])    sum(nums) - sum(nums[0:i+1]) -  nums[i] * (len(nums) - (i + 1))


# print(r1, "==", [4,3,5])
# print(r2, "==", [24,15,13,15,21])

# [2,  3,  5]
#  2   5   8

# 2   1   2