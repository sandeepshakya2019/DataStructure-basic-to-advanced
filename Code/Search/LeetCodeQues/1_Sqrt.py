def SQRTBs(num):
    if num == 1: return 1
    start = 0
    end = num - 1
    main = 0
    while start <= end:
        mid = start + int((end - start)/2)
        ans = mid * mid
        if ans > num: end = mid - 1
        else:
            main = mid
            start = mid + 1
    return main

print(SQRTBs(16))