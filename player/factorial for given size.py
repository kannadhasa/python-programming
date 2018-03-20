x=int(input())
fact=1
if x<=20:
    while x>0:
        fact=fact*x
        x=x-1
    print(fact)
else:
    print("enter the valid input")

