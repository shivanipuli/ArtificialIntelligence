import sys
import math

arg=sys.argv
print(arg)

if arg[1]=="A":
    for i in range(2,5):
        arg[i]=int(arg[i])
    print(sum(arg[2:5]))
elif arg[1]=="B":
    for i in range(2,len(arg)):
        arg[i]=int(arg[i])
    print(sum(arg[2:]))
elif arg[1]=="C":
    for i in range(2,len(arg)):
        arg[i]=int(arg[i])
    print(sum(arg[2:])/3)
elif arg[1] == "D":
    nums = [1, 1]
    for i in range(int(arg[2])):
        nums.append(nums[-2]+nums[-1])
    print(nums)
elif arg[1] == "E":
    nums=[]
    for i in range(int(arg[2]),int(arg[3])+1):
        nums.append(i**2-3*i+2)
    print(nums)
elif arg[1] == "F":
    sides=arg[2:5]
    for i in range(len(sides)):
        sides[i]=float(sides[i])
    sides.sort()
    if sides[2]>=sum(sides[0:2]):
        print("sides not valid")
    else:
        s=sum(sides)/2.0
        area=s*(s-sides[0])*(s-sides[1])*(s-sides[2])
        area=math.sqrt(area)
        print(area)
elif arg[1] == "G":
    vowels={'a':0,'e':0,'i':0,'o':0,'u':0}
    for char in arg[2]:
        if char in vowels.keys():
            vowels[char]=vowels.get(char)+1
    print(vowels)
