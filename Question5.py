# WAP to find the greatest of three numbers entered by the user.

a= int(input("enter the first number:"))
b= int(input("enter the second number:"))
c= int(input("enter the third number:"))

if(a>b):
    if(a>c):
        print(a,"is largest")
    else:
        print(c,"is largest") 

if(b>a):
    if(b>c):
      print(b,"is largest")
    else:
      print(c,"is largest") 


