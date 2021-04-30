n=int(input("enter the number to get the fibanancy series"))
n1,n2=0,1
for i in range(n):
    print(n1)
    sum= n1+n2
    n1=n2
    n2=sum
    
