 ## best example of oop's in that method..
class Solution(object):
    def addTwoNumbers(self, list1, list2):
        x= int("".join(map(str,list1)))
        y= int("".join(map(str,list2)))
        z = x+y
        list = []
        while z>0:
            r = z%10
            list.append(r)
            z = z//10
        print(list)    

P = Solution().addTwoNumbers([2,4,3],[5,6,4])            
    