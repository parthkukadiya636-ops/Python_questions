class Solution(object):
    def plusOne(self, digits):
       x  = int("".join(map(str,digits)))
       y=x+1
       list = []
       while(y>0):
        r = y%10
        list.append(r)
        y = y//10
       list.reverse()
       print(list)
Solution().plusOne([1,2,3])
        