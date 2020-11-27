import sys,queue,time

def isConnected(word1,word2):
    return [word1[i]==word2[i] for i in range(6)].count(False)==1

myTime=time.perf_counter()
wordList=[]
with open(sys.argv[1]) as f:
    wordList = [line.strip() for line in f]

neighbors={}
#Makes dictionary of neighbors for each
for i in range(len(wordList)-1):
    for y in range(i+1,len(wordList)):
        if isConnected(wordList[i],wordList[y]):
            neighbors[wordList[i]]=neighbors.get(wordList[i],[])+[wordList[y]]
            neighbors[wordList[y]] = neighbors.get(wordList[y], []) + [wordList[i]]
myTime=time.perf_counter()-myTime
print("Time to generate data structures %s " %str(myTime))
clumps=[]
copyList=wordList.copy()
singletons=0
maxClump=[]
while len(copyList)>0:
    tempClump=[]
    fringe=queue.Queue()
    fringe.put(copyList[0])
    while not fringe.empty():
        word=fringe.get()
        if word in copyList:
            copyList.remove(word)
            tempClump+=[word]
            for item in neighbors.get(word,[]):
                fringe.put(item)
    if len(tempClump)==1:
        singletons+=1
    if len(maxClump)<len(tempClump):
        maxClump=tempClump
    clumps.append(tempClump)
print("Number of singles: %s" %singletons)
print("Largest Clump Length: %s" %str(len(maxClump)))
print("Number of clumps: %s " %str(len(clumps)-singletons))

def findPath(word1,word2):
    checked=set()
    checked.add(word1)
    previous={word1:""}
    fringe=queue.Queue()
    fringe.put(word1)
    while not fringe.empty():
        word = fringe.get()
        if word==word2:
            path=[word2]
            while word1 not in path:
                path+=[previous[path[-1]]]
            path.reverse()
            return path
        for item in neighbors.get(word, []):
            if item not in checked:
                checked.add(item)
                fringe.put(item)
                previous[item]=word
    return ["No path found"]
myTime=time.perf_counter()
with open(sys.argv[2]) as f:
    count=0
    for line in f:
        words=line.strip().split(" ")
        path=findPath(words[0],words[1])
        if "No path found" in path:
            print("Line %s: No path found from %s to %s" % (str(count),words[0], words[1]))
        else:
            print("Line %s: Length of Path from %s to %s: %s" %(str(count),words[0],words[1],len(path)))
            print(path)
        count+=1
myTime=time.perf_counter()-myTime
print("Total Time to Solve Puzzles: %s " %str(myTime))


# maxPath=[]
# for i in range(len(maxClump)-1):
#     for y in range(i+1,len(maxClump)):
#         path=findPath(maxClump[i],maxClump[y])
#         if len(path)>len(maxPath):
#             maxPath=path
# print("Max Path: " + str(maxPath))
