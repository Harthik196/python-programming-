a = int(input())
b = int(input())
for x in range (a, b+1):
    if x >1:
        y=False
        for i in range (2, x):
            if (x%i)== 0:
                y=True
            break
        if y:
            print(x)

            
