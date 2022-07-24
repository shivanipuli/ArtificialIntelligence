n=10
m=20
max_t=50
#beauty=[3,7,5,6,8]
beauty=[96498533,27054154,92830679,23152772,347212,84213970,68645321,49486803,35560380,95724838]
u=[1,0,1,3,1,6,6,4,7,0,5,1,9,7,8,2,4,6,3,2]
v=[0,2,3,4,5,3,7,8,9,5,7,4,8,8,6,5,0,2,9,9]
t=[11,11,11,10,11,10,11,11,11,10,11,11,10,11,11,11,11,10,10,11]

def findBestPath(n, m, max_t, beauty, u, v, t):
    edges=makeEdgeList(m,u,v)
    fringe=[(beauty[0],0,[0])]#beauty,time,path
    maxBeauty=beauty[0]
    bestPath=[0]
    while len(fringe)>0:
        beaut,time,path=fringe.pop()
        if time<=max_t:
            if beaut>maxBeauty and path[-1]==0:
                maxBeauty=beaut
                bestPath=path
            for child,t in edges[path[-1]]:
                if child in path:
                    fringe.append((beaut,time + t, path + [child]))
                if child not in path:
                    fringe.append((beaut+beauty[child],time+t,path+[child]))
    return maxBeauty

def makeEdgeList(m,u,v):
    edges={}
    for i in range(m):
        node1=u[i]
        node2=v[i]
        time=t[i]
        tempEdge=edges.get(node1,[])
        tempEdge.append([node2,time])
        edges[node1]=tempEdge
        tempEdge=edges.get(node2,[])
        tempEdge.append([node1,time])
        edges[node2]=tempEdge
    return edges

print(findBestPath(n,m,max_t,beauty,u,v,t))