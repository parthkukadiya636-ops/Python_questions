# print the maximum occuring character in the word 
string  = input("Enter a string:")
chars=[]
count = []

for char in string:
    if char not in chars:
        chars.append(char)
        count.append(string.count(char))

count.sort()
x= len(count)
print(count[x-1])  