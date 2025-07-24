class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        # print(intervals)
        arr = []
        n = len(intervals)
        i = 0
        pos = [0,0]
        while i < n:
            if i == 0:
                pos = intervals[i]
            else:
                if pos[0] <= intervals[i][0] and pos[1] >= intervals[i][0]:
                    e = max(intervals[i][1], pos[1])
                    pos = [pos[0], e]
                else:
                    arr.append(pos)
                    pos = intervals[i]
            i += 1
        # print(pos)
        arr.append(pos)
        return arr





    
intervals = [[1,3],[2,6],[8,10],[15,18],[9,11], [2,4], [8,9],[16,17]]
print(Solution().merge(intervals))