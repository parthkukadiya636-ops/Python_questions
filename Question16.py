class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if(nums[i]==target):
                print(i)
                return 0
        
         
        nums.append(target)
        nums.sort()
        for i in range((len(nums))):
               
            if(nums[i]==target):
                print(i) 
Solution().searchInsert([1,3,5,6],2)                
                