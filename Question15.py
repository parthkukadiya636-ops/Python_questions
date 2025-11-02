class Solution(object):
    def romanToInt(self, s):
        sum=0
        roman_Dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        i=0
        while i<len(s):
            if(i<len(s)-1 and roman_Dict[s[i]]<roman_Dict[s[i+1]]):
                sum = sum + (roman_Dict[s[i+1]] - roman_Dict[s[i]])
                i +=2
                
            else:
                sum = sum + roman_Dict[s[i]]
                i +=1


        return sum
Solution().romanToInt("III")    