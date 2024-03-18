def dfs(visited, graph, node,n):  #Depth First Search
    if node not in visited:
        visited.add(node)
        for i in range(n):
            if graph[node][i] == 1:
                dfs(visited, graph, i, n)


while True:
    n,m=map(int,input().split(' '))
    
    if n == m == 0:
        break
    
    points = [0]*n
    for i in range(n):
        points[i] = [0]*n
        
    for i in range(m):
        v,w,d = map(int,input().split(' '))
        points[v-1][w-1] = 1
        if d == 2:
            points[w-1][v-1] = 1
            
    possible = True
    for i in range(n):
        visited = set()
        dfs(visited,points,i,n)
        for j in range(n):
            if j not in visited:                
                possible = False
                break            
        if possible == False:
            break
        
    if possible:
        print('S')
    else:
        print('N')
