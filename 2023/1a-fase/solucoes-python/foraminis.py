from math import sqrt

def energy(signal):
    e = 0
    for i in range(len(signal)):
        e+=signal[i]*signal[i]
    return e

H = [1/sqrt(2),1/sqrt(2)]
#G = [1/sqrt(2),-1/sqrt(2)]


n = int(input())
for i in range(n):
    S = list(map(int,input().split(' ')))
    R = []
    for j in range(0,8,2):
        R.append(H[0]*S[j]+H[1]*S[j+1]) #BAIXA FREQUÊNCIA
        #R.append(G[0]*S[j]+G[1]*S[j+1]) #ALTA FREQUÊNCIA
    
    if energy(R)/energy(S) > 0.5:
        print('INIMIGO')
    else:
        print('-')
    
        
