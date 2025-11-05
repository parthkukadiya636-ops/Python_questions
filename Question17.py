# index of the target element 
class Solution(object):
    def search(self, nums, target):
        for i in range(0,len(nums)):
            if(nums[i]==target):
                return i

        return -1
Solution().search([4,5,6,7,0,1,2],0)                