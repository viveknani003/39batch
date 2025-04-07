a=int(input("enter a number:"))
for value in range(1,a+1):
           for line in range(a-value+1,0,-1):
            print(line,end="")
           print()
a=int(input("enter a number:"))
for i in range(1,a+1):
    for j in range(i,a+1):
        print(j*2,end="")
    print()

for i in range(1,10):
    for j in range(i,10):
        print(j,end="")
    print()

for i in range(1,a+1):
    for j in range(a-i+1,0,-1):
        print(j,end="")
    print()

b=int(input("enter a number:"))
for i in range(1,b+1):
    rev=""
    for j in range(1,b-i+2):
        rev=rev+str(j)
    print(rev)
    print(rev[::-1])
