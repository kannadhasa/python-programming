a=int(input('Enter the N value:'))
b=int(input("enter the k value:"))
l=[int(input()) for i in range(0,a)]
if b<a:
    l=l[:b]
    s=sum(l)
    print(s)
else:
    print("wrong input:")
