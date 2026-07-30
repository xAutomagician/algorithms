class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        # Space O(n), how can be O(1) with extra space for dynamic?
        # Time O(n)?
        MAX_LOCATION_KM = 1000

        dynamic = [0] * (MAX_LOCATION_KM + 1) # 1000 from task constraint, wrong solution?

        for seats, _from, _to in trips:
            dynamic[_from] += seats
            dynamic[_to] -= seats



        cur_sum = 0
        for d in dynamic:
            cur_sum += d
            if cur_sum > capacity:
                return False

        return True

        # answer = [0]

        # for d in dynamic:
        #     if answer[-1] + d > capacity:
        #         return False
        #     answer.append(answer[-1] + d)

        # return True

"""

trips = [[2,1,5],[3,3,7]], capacity = 4

0   1  2   3  4   5  6   7  8    9
   +2     +3        -2     -3
    2  2   5  5   5  3   3  0  0


0   1  2   3  4   5  6  7  8  9
   -2     -3     +2       +3
    0  2   2  5   5   3    3

"""


trips = [[2,1,5],[3,3,7]]
capacity = 4
s1 = Solution()

print(s1.carPooling(trips, capacity), "==", False)
