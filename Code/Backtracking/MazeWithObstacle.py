def MazeProblemDiagPath(start, end, p, ans):
    # print(start, end)
    if start[0] > end[0]:
        return 0
    if start[1] > end[1]:
        return 0
    
    if start[0] == end[0] and start[1] == end[1]:
        ans.append(p)
        return 1
    
    
    # going down
    cor = [start[0] + 1, start[1]]
    # if cor !== False for obstacle return 0
    MazeProblemDiagPath(cor, end, p + "D", ans)
    #  going right
    cor = [start[0], start[1] + 1]
    # if cor !== False for obstacle return 0
    MazeProblemDiagPath(cor, end, p + "R", ans)
    #going diag
    cor = [start[0] + 1, start[1] + 1]
    # if cor !== False for obstacle reutrn 0
    MazeProblemDiagPath(cor, end, p + "K", ans)

    # combine
    return ans

# print(MazeProblemDiagCount([0,0], [2,2]))

print(len(MazeProblemDiagPath([0,0], [2,2], "", [])))