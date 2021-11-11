def wiggleMaxLength(nums):
    dp = []
    for x in nums:
        if not dp:
            print(dp, x)
            dp += x,
            continue
        if x == dp[-1]:
            continue
        if len(dp) == 1:
            print(dp, x)
            dp += x,
            continue
        if dp[-1] > dp[-2]:
            if x > dp[-1]: dp[-1] = x
            else: dp += x,
        else:
            if x < dp[-1]: dp[-1] = x
            else: dp += x,
    return len(dp)
                
print(wiggleMaxLength([1,7,4,9,2,5]))
                
        