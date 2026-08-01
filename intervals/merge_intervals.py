class Solution:
    # Sort O(n log n) + O(n)
    # Space O(n) - на ответ merged_intervals
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:      # [[1,3],[2,6]]
        intervals.sort()
        # [[1,3],[2,6]]
        merged_intervals = [intervals[0]]  # [[1,3]]

        for i in range(1, len(intervals)):
            interval_1 = merged_intervals[-1]  # [1,3]
            interval_2 = intervals[i]  # [2,6]

            if interval_2[0] <= interval_1[1]:   # 2 <= 3 == True
                start = interval_1[0] # 1
                end = max(interval_1[1], interval_2[1])  # (3, 6) → 6
                merged_intervals[-1] = [start, end]  # [1, 6]
            else:
                merged_intervals.append(interval_2)

        return merged_intervals





"""

[[1,3],[2,6],[8,10],[15,18]]
[[1,3],[2,6],[5,10],[15,18]]

1. Конец интервала < Начало следующего интервала   -> оставляем предыдущий как есть
[2,6],[8,10]

2. Начало следующего интервала <= конца предыдущего
[1,3],[2,6]

    2.1 Конец предыдущего интервала  >= конец следующего
        [4,7], [1,4] > [1, 7]
    2.2 Конец предыдущего интервала  < конец следующего
        [1,4], [4,7]

"""



s = Solution()

intervals_1 = [[1,3],[2,6]]
intervals_2 = [[4,7], [1,4]]
intervals_3 = [[1,3],[2,6],[8,10],[15,18]]


print(s.merge(intervals_1))
print([[1, 6]])
print()

print(s.merge(intervals_2))
print([[1, 7]])
print()


print(s.merge(intervals_3))
print([[1, 6], [8, 10], [15, 18]])
