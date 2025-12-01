def thirdMax(nums):
  
    nums.sort(reverse=True)

    distinct_count = 0
    max_val = nums[0]

    for i in range(1, len(nums)):
        if nums[i] == max_val:
            continue  

        max_val = nums[i]
        distinct_count += 1

        if distinct_count == 2:   
            return max_val

    return nums[0]   
