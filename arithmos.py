def my(x,y):
 while y!=0:
   x=x+y%10
   y=y//10  
 return x,y   

print("give me a positive integer")
x=int(input())

x=x*3+1
y=x
x=0
a=my(x,y)
x=a[0]
y=a[1]
while x>=10:
  x=x*3+1
  y=x
  x=0
  a=my(x,y)
  x=a[0]
  y=a[1]
print(x)
