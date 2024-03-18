l,c,b=map(int,input().split(' ')) #lines, columns, battery
x,y=map(int,input().split(' ')) #position
r=list(input()) #routine
knocked=0

d={'C': [-1,0], 'B': [1,0], 'E': [0,-1], 'D': [0,1]} #directions

for i in range(min(len(r),b)):
    if 0< (x+d[r[i]][0]) < l+1 and 0 < (y+d[r[i]][1]) < c+1:
        x+=d[r[i]][0]
        y+=d[r[i]][1]
    else:
        knocked+=1
print(f'{x} {y} {knocked}')

        
        
