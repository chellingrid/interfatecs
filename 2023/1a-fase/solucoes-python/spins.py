while True:
    n=int(input())
    if n == 0:
        break
    result = []
##    q = [-1]*n #quantum gates todos fechados
##    #-1 fechado, 1 aberto
##    print(q)
##    for i in range(1,n+1):
##        for j in range(i, n+1, i):
##            print(i,j)
##            q[j-1]*=-1
##            print(q)
##    
##    for i in range(n):
##        if q[i] == 1:
##            result.append(str(i+1))
    i = 1
    while i*i < n+1:
        result.append(str(i*i))
        i+=1

    print(" ".join(result))
