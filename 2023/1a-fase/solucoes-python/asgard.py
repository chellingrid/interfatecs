n,q=map(int,input().split(" "))
days=int(input())
registers = n*n-n
trades = [0]*n
for i in range(n):
    trades[i] = [0]*n
for i in range(days):
    for j in range(registers+1): #+1 do cabeçalho
        if j > 0:
            x,y,quantity=map(int,input().split(" "))
            trades[x-1][y-1]+=quantity
        else:
            input()
    
    print(f'Final do dia {i+1}')
    notTraded = True
    for j in range(n): #empresa1
        for k in range(j+1, n): #empresa2
            if trades[j][k] >= q and trades[k][j] >= q:
                notTraded = False
                v1=trades[j][k]//q
                trades[j][k]-=v1*q
                v2=trades[k][j]//q
                trades[k][j]-=v2*q
                print(f'  Trocas entre {j+1}({v1}v) e {k+1}({v2}v)')
    if notTraded:            
        print('  Sem Trocas')
