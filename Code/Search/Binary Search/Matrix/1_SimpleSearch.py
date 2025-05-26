matrix = [[18,9,12],[36,-4,91],[44,33,16]]

def SimpleSearch(matrix, target):
    for arr in matrix:
        for el in arr:
            if el == target:
                return True
            
    return False

print(SimpleSearch(matrix, 16))