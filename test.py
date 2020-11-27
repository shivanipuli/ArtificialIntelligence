list=[]
list.append("Alex Blake 5".split(" "))
list.append("Blake Alex 3".split(" "))
list.append("Casey Alex 7".split(" "))
list.append("Casey Alex 4".split(" "))
list.append("Casey Alex 2".split(" "))



def smallestNegativeBalance(debts):
    # Write your code here
    debtsDict={}
    for item in debts:
        borrower=item[0]
        lender=item[1]
        amount=int(item[2])
        mySum=debtsDict.get(borrower,0)
        mySum-=amount
        debtsDict.update({borrower:mySum})
        mySum=debtsDict.get(lender,0)
        mySum+=amount
        debtsDict.update({lender:mySum})
    minValue=-1
    minPerson=[]
    for person in debtsDict.keys():
        debt=debtsDict[person]
        #minPerson.append(person+str(debt))
        if debt<minValue:
            minValue=debt
            minPerson=[person]
        if debt==minValue:
            minPerson.append(person)
    if len(minPerson)==0:
        return "Nobody has a negative balance"
    minPerson.sort()
    return minPerson


print(smallestNegativeBalance(list))