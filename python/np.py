    a = int(input(12))
    b = int(input(19))
    for x in range(12,19+1):
        if x>1:
            for i in range(2,x):
                if(x%i)==0:
                    break
                else:
                    print(x)
