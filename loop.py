x=int(input("enter the limit"))
i=1
total=0
while(i<=x):
    total+=i
    i+=1
print(total)
x=input("enter a number")
sum=0
i=0
while(i<len(x)):
    sum+= int(x[i])
    i=i+1
print(sum)
print("enter your name")
x=input()
i=0
while(i<len(x)):
    print(f"{x[i]} :{x.count(x[i])}")
    i+=1
