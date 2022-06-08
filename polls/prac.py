def getTotalX(a, b):
    # Write your code here
    mi = max(a)
    ma = min(b)
    cont = 0
    for i in range(mi,  ma + 1):
        esdivisor = True
        for n in b:
            if n % i != 0:
                esdivisor=False
        if esdivisor == True:
            for x in a:
                if i % x != 0:
                    esdivisor= False
            if esdivisor == True:
                print(i)
                cont+=1
    return cont
b=[16,32,96]
a= [2,4]

print(getTotalX(a, b))