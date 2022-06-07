sal=int(input())
hra=int(input())
ded=int(input())
n=sal-hra-ded
if(n<=300000):
    print("no tax")
a=n-300000
if(a>300000 and a<=600000):
    print(a/10,"10% interest")
elif(a>600000 and a<=1000000):
    print(a*3/20,"15% interest")
else:
    print(a/5,"20% interest")
