class Solution:
    # def minGroups(self, intervals: list[list[int]]) -> int:
    #     # Time O(n^2), Space O(1)
    #     result = 0

    #     for point, _ in intervals:
    #         count = 0
    #         for start, end in intervals:
    #             if start <= point <= end:
    #                 count += 1
    #         result = max(result, count)
    #     return result

    def minGroups(self, intervals: list[list[int]]) -> int:
        # Time O(n), Space O(n)
        from collections import defaultdict
        start_end_map = defaultdict(int)

        for start, end in intervals:
            start_end_map[start] += 1
            start_end_map[end+1] -= 1

        result = 0
        count = 0
        sorted_map = dict(sorted(start_end_map.items()))
        for value in sorted_map.values():
            count += value
            result = max(result, count)
        return result


#  0 1 2 3 4 5 6 7 8 9
#    ---------     ---
#  ----   -----  -
#    --- ---  --------
#  --------------
#  -----   ---
#  0 1 2 3 4 5 6 7 8 9


# [1, 3], [5, 8]
# [0, 1]
# [4, 7]

#  0 1 2 3 4 5 6 7 8 9
#    -----   ---
#              -----
#          -----

#  0 1 2 3 4 5 6 7 8 9


#  0 1 2 3 4 5 6 7 8 9
#    -----   -------
#          ---     ---
#      -----
#  0 1 2 3 4 5 6 7 8 9


#  0 1 2 3 4 5 6          7 8 9
#    ----- ---              ---
#      ----- ----------------
#  0 1 2 3 4 5 6          7 8 9

# 56.5 × 365.25 × 24 × 60 × 60

# 365.25 × 24 × 60 × 60 ≈ 30 000 000


# 3 встречи

#      0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
#      ↓        ↓            ↓       ↓       ↓          ↓
#      ----------------------        -------------------
#               -----------------------------
#      1        2                     2



#  0 1 2 3 4 5 6          7 8 9
#    ----- ---              ---
#      ----- ----------------
#   1      -1
#          1   -1           1   -1

# {
#     1: 1,
#     2: 1,
#     4: 0,
#     5: 0,
#     6: -1,
#     8: 1,
#     9: -1,
#     10: -1,
# }


s = Solution()

intervals = [[1,3], [4,5], [8,9], [2,4], [5,8]]
print(s.minGroups(intervals), " == ", 2)