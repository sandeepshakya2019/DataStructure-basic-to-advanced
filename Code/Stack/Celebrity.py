class Solution:
    def celebrity(self, mat):
        # code here
        n = len(mat)
        arr = [i for i in range(n)]
        # print(arr)
        while len(arr) > 1:
            firstElem = arr.pop()
            secondElem = arr.pop()
            if mat[firstElem][secondElem] == 1:
                # discard first Elemnent 
                arr.append(secondElem)
            
            elif mat[secondElem][firstElem] == 1:
                # discard the second elembt
                arr.append(firstElem)
            
        if len(arr) == 0:
            return -1
        # print(mat[arr[0]], arr[0])
        check = False
        for k in range(len(mat[arr[0]])):
            # check is this real celebrity
            if k != arr[0]:
                if mat[arr[0]][k] == 1 or mat[k][arr[0]] == 0:
                    return -1
        return arr[0]
                
                