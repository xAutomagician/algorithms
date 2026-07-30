
# bookings[i] = [firsti, lasti, seatsi]
# Input: bookings = [[1,2,10],[2,3,20],[2,5,25],[7,9,5]], n = 10
# Output: [10,55,45,25,25,0,5,5,5,0]


# Flight labels:        1   2   3   4   5   6
# Booking 1 reserved:  10  10
# Booking 2 reserved:      20  20
# Booking 3 reserved:      25  25  25  25

#                     +10 +45 -10 -20   0 -25
#                  0   10  55  45  25  25   0

# Total seats:         10  55  45  25  25


class Solution2(object):
    # time O(N×B)  space O(1)
    #                            B         N
    def corpFlightBookings(self, bookings, n):
        dynamic = [0] * (n + 1)

        for first, last, seats in bookings:
            dynamic[first - 1] += seats
            dynamic[last] -= seats

        #   0   1   2   3   4   5    i
        # +10 +45 -10 -20   0 -25    dynamic[i]

        current_sum = 0
        result = []
        for i in range(n):
            current_diff = dynamic[i]
            current_sum += current_diff
            result.append(current_sum)


        # answer = [0]
        # for d in dynamic:
        #     answer.append(answer[-1] + d)

        # result = answer[1:-1]

        return result


s = Solution2()
print(s.corpFlightBookings([[1, 2, 10],[2, 3, 20], [2, 5, 25],[7,9,5]], 10))
print([10, 55, 45, 25, 25, 0, 5, 5, 5, 0])


# [7,9,5]
