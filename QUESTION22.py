def findDisappearedNumbers(nums):
    nums.sort()    
    missing = []
    expect = 1
    i = 0
    n = len(nums)

    while expect <= n and i < n:
         
        if nums[i] < expect:
            i += 1
         
        elif nums[i] > expect:
            missing.append(expect)
            expect += 1
         
        else:
            expect += 1
            i += 1

     
    while expect <= n:
        missing.append(expect)
        expect += 1

    return missing

