def maximumWealth(self, accounts):
    sums = [sum(row) for row in accounts]
    return max(sums)