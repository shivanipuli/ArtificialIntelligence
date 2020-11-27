import sys
inputs=sys.argv[1:]
def swap(minlist,indx,indy):#swaps two vars in list given indices
    temp=minlist[indx]
    minlist[indx]=minlist[indy]
    minlist[indy]=temp

def heappush(minlist, var):
    minlist.append(var) #adds var to end of list
    cInd=len(minlist)-1#sets child index to last index
    pInd=(cInd-1)//2#finds parents index
    while pInd>=0 and minlist[pInd]>minlist[cInd]:#checks if child & parent need to be swapped
        swap(minlist,pInd,cInd)
        cInd=pInd#sets new child index after swap
        pInd=(cInd-1)//2#finds parent index
def heappop(minlist):
    swap(minlist,0,len(minlist)-1) #swaps first and last index
    minVal=minlist.pop()
    pInd=0
    cInd=None
    if pInd*2+1>=len(minlist):  #no nodes exist
        cInd=None
    elif pInd*2==len(minlist):  #only left node exists
        cInd=len(minlist)-1
    else:#both left and right nodes exist
        cList=minlist[pInd * 2 + 1:pInd * 2 + 3]
        cInd=minlist.index(min(cList))#sets cInd to the min index of two children
    while cInd != None and minlist[pInd]>minlist[cInd]:
        swap(minlist,pInd,cInd)
        pInd=cInd
        if pInd * 2 + 1 >= len(minlist):# no nodes exist
            cInd = None
        elif pInd * 2 + 1 == len(minlist) - 1 :# only left node exists
            cInd = len(minlist) - 1
        else:# both left and right nodes exist
            cInd = pInd * 2 + 1
            if minlist[cInd] > minlist[cInd+1]:
                cInd += 1#sets cInd to the min index of two children
    return minVal

def heapify(some_list):
    heap=[]
    for item in some_list:
        heappush(heap,int(item))
    for i in range(len(some_list)):
        some_list[i]=heap[i]


index=min(inputs.index('A'),inputs.index('R'))
heap_list = inputs[:index] #sets list to initial numbers
print("Initial list: %s" %heap_list)

heapify(heap_list)
print("Heapified list: %s" %heap_list)

while len(inputs) > index: #iterates through input list
    if inputs[index]=="A":
        heappush(heap_list,int(inputs[index+1]))  #
        print("Added %s to heap: %s " %(inputs[index+1], heap_list))
        index+=2
    else:
        minVal=heappop(heap_list)
        print("Popped %s from heap: %s " %(minVal, heap_list))
        index+=1
