def MazeProblemCount(start, end):
    # print(start, end)
    if start[0] > end[0]:
        return 0
    if start[1] > end[1]:
        return 0
    
    if start[0] == end[0] and start[1] == end[1]:
        return 1
    
    
    # going down
    cor = [start[0] + 1, start[1]]
    down = MazeProblemCount(cor, end)
    #  going right
    cor = [start[0], start[1] + 1]
    right = MazeProblemCount(cor, end)

    # combine
    return down + right 

def MazeProblemPath(start, end, p, ans):
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
    MazeProblemPath(cor, end, p + "D", ans)
    #  going right
    cor = [start[0], start[1] + 1]
    MazeProblemPath(cor, end, p + "R", ans)

    # combine
    return ans

def MazeProblemDiagCount(start, end):
    # print(start, end)
    if start[0] > end[0]:
        return 0
    if start[1] > end[1]:
        return 0
    
    if start[0] == end[0] and start[1] == end[1]:
        return 1
    
    
    # going down
    cor = [start[0] + 1, start[1]]
    down = MazeProblemDiagCount(cor, end)
    #  going right
    cor = [start[0], start[1] + 1]
    right = MazeProblemDiagCount(cor, end)
    # going diagonal
    cor = [start[0] + 1, start[1] + 1]
    diag = MazeProblemDiagCount(cor, end)

    # combine
    return down + right  + diag

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
    MazeProblemDiagPath(cor, end, p + "D", ans)
    #  going right
    cor = [start[0], start[1] + 1]
    MazeProblemDiagPath(cor, end, p + "R", ans)
    #going diag
    cor = [start[0] + 1, start[1] + 1]
    MazeProblemDiagPath(cor, end, p + "K", ans)

    # combine
    return ans

# print(MazeProblemDiagCount([0,0], [2,2]))

print(len(MazeProblemDiagPath([0,0], [2,2], "", [])))