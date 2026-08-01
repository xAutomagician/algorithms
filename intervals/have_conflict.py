class Solution:
    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:
        # Space O(1)?
        # Time O(1) in this case
        if event1[0] > event2[0]:
            event1, event2 = event2, event1  # New space or just link changes?

        s1, e1 = event1
        s2, e2 = event2

        # if s2 <= e1:
        #     return True
        # return False

        return s2 <= e1

        # Solution for fun
        # Space O(1) or O(n)?  Мы создаем новый массив, но его размер не зависит от кол-ва  intervals


        # Time O(n)

        # Make array [0000,0001, ... 2359]
        # for time in enevt range increase counter
        # if in some index conter > 1, its mean we have conflict
        # diff = [0] * 2360

        # s1 = int("".join(event1[0].split(":")))
        # e1 = int("".join(event1[1].split(":")))

        # for i in range(s1, e1+1):
        #     diff[i] += 1

        # s2 = int("".join(event2[0].split(":")))
        # e2 = int("".join(event2[1].split(":")))

        # for i in range(s2, e2+1):
        #     diff[i] += 1
        #     if diff[i] > 1:
        #         return True

        # return False



s2 = Solution()
print(s2.haveConflict(["14:13", "22:08"], ["02:40", "08:08"]), "", False)
print(s2.haveConflict(["01:15", "02:00"], ["02:00", "03:00"]), "==", True)
