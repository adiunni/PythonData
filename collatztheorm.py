c0=int(input("Enter any number: "))
count=0
while c0!=1:
    if c0%2==0:
        c0=c0/2
    else:
        c0=3*c0+1
    print(c0)
    count+=1
print("steps: ",count)    
