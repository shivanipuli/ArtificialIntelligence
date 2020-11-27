from math import pi , acos , sin , cos
from heapq import heappop, heappush, heapify
import time, sys
import tkinter as tk

def makeCoord(node):
    lat,long=node
    x=(lat-14)*15
    y=(131+long)*15
    x=750-x
    return y,x

lines={}



def makeLine(c,name1,name2,node1,node2):
    x1,y1=makeCoord(node1)
    x2,y2=makeCoord(node2)
    line=c.create_line([(x1,y1),(x2,y2)], tag='grid_line')
    lines[name1+name2]=line
    lines[name2+name1]=line
    #c.update()

def changeColor(r,c,line,color):
    c.itemconfig(line, fill=color)
    #r.update()

def calcd(node1, node2):
   if node1==node2:
        return 0
   y1, x1 = node1
   y2, x2 = node2
   R   = 3958.76 # miles = 6371 km
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R

def create_grid(r,c):
    for line in lines.values():
        c.itemconfig(line, fill="black")  # changes color of one line to red
        r.update()

root = tk.Tk() #creates the frame

button = tk.Button(root,text = 'NEXT', height=2,width=10, command=root.quit)
button.pack()
canvas = tk.Canvas(root, height=750, width=1100, bg='white') #creates a canvas widget, which can be used for drawing lines and shapes
canvas.pack(expand=True) #packing widgets places them on the board


myTime=time.perf_counter()

names={}
#with open("Train Routes/rrNodeCity.txt") as f:
with open("rrNodeCity.txt") as f:
    for line in f:
        line=line.strip()
        node=line[:line.index(" ")]
        name=line[line.index(" ")+1:]
        names[name]=node

latLong={}
# minLat=40
# maxLat=50
# minLong=-70
# maxLong=-100
#with open("Train Routes/rrNodes.txt") as f:
with open("rrNodes.txt") as f:
    for line in f:
        line=line.strip()
        lis=line.split(" ")
        # minLong=min(minLong,float(lis[2]))
        # minLat = min(minLat, float(lis[1]))
        # maxLong = max(maxLong, float(lis[2]))
        # maxLat = max(maxLat, float(lis[1]))
        latLong[lis[0]]=(float(lis[1]),float(lis[2]))

edges={}
#with open("Train Routes/rrEdges.txt") as f:
with open("rrEdges.txt") as f:
    for line in f:
        line=line.strip()
        edge1,edge2=line.split(" ")
        dist=calcd(latLong[edge1],latLong[edge2])
        edgeList=edges.pop(edge1,[])
        edgeList.append((edge2,dist))
        edges[edge1]=edgeList
        edgeList = edges.pop(edge2, [])
        edgeList.append((edge1, dist))
        edges[edge2]= edgeList
        makeLine(canvas,edge1,edge2,latLong[edge1],latLong[edge2])
canvas.update()

myTime=time.perf_counter()-myTime
print("Time to create data structure: " + str(myTime))


def dijkstra(start,end):
    distTo={start:0}
    checked=set()
    checked.add(start)
    fringe=[(0,start,[start])]
    heapify(fringe)
    count=0
    pathTo={}
    while len(fringe)>0:
        dist,node,path=heappop(fringe)
        if node==end:
            for i in range(len(path) - 1):
                changeColor(root, canvas, lines[path[i] + path[i + 1]], "red")
            root.update()
            return dist
        for edge,dist2 in edges[node]:
            if edge in checked and distTo[edge]>dist+dist2:
                distTo[edge] = dist + dist2
                pathTo[edge]=path+[edge]
                heappush(fringe, (dist + dist2, edge,path+[edge]))
            if edge not in checked:
                changeColor(root,canvas,lines[edge+node],"green")
                distTo[edge]=dist+dist2
                pathTo[edge] = path + [edge]
                heappush(fringe,(dist+dist2,edge,path+[edge]))
                checked.add(edge)
        count+=1
        if count%1000==0:
            root.update()
    root.update()
    path=pathTo[end]
    for i in range(len(path)-1):
        changeColor(root, canvas, lines[path[i] + path[i+1]], "red")
    root.update()
    return distTo[end]

def ASearch(start,end):
    distTo = {start: 0}
    checked = set()
    checked.add(start)
    heuristic=calcd(latLong[start],latLong[end])
    fringe = [(heuristic, start, 0,[start])]
    heapify(fringe)
    count=0
    while len(fringe) > 0:
        heur, node, dist,path = heappop(fringe)
        if node==end:
            for i in range(len(path) - 1):
                changeColor(root, canvas, lines[path[i] + path[i + 1]], "red")
            root.update()
            return heur
        for edge, dist2 in edges[node]:
            heur=calcd(latLong[edge],latLong[end])
            if edge in checked and distTo[edge] > dist + dist2:
                distTo[edge] = dist + dist2
                heappush(fringe, (heur+dist + dist2, edge,dist+dist2,path+[edge]))
            if edge not in checked:
                distTo[edge] = dist + dist2
                changeColor(root, canvas, lines[edge + node], "blue")
                heappush(fringe, (heur+dist + dist2, edge,dist+dist2,path+[edge]))
                checked.add(edge)
        count+=1
        if count%10==0:
            root.update()
    return distTo[end]

name1,name2 = sys.argv[1:3]


def setTargets(r,c,name1,name2):
    x,y=makeCoord(latLong[name1])
    x1, y1 = x-5, y- 5
    x2, y2 = x+5, y + 5
    c.create_oval(x1, y1, x2, y2, fill="red")
    x, y = makeCoord(latLong[name2])
    x1, y1 = x - 5, y - 5
    x2, y2 = x + 5, y + 5
    c.create_oval(x1, y1, x2, y2, fill="red")
    r.update()


setTargets(root,canvas,names[name1],names[name2])

myTime=time.perf_counter()
dist=dijkstra(names[name1],names[name2])
myTime=time.perf_counter()-myTime
print("%s to %s with Dijkstra: %s in %s seconds." %(name1,name2,dist,myTime))
myTime=time.perf_counter()
root.mainloop()


dist=ASearch(names[name1],names[name2])
myTime=time.perf_counter()-myTime
print("%s to %s with A*: %s in %s seconds." %(name1,name2,dist,myTime))
root.mainloop()