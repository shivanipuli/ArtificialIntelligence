#Outstanding Work
#ProjectEuler key: 1731402_kDtCDDQcYQ9Q5kRiveLslyn3Di2cOUR6
#Problem 11:
#greatest product of 4 adj numbers in same direction (up, down, left, right, or diagonally) in the 20×20 grid?
grid=[[8,2,22,97,38,15,0,40,0,75,4,5,7,78,52,12,50,77,91,8],[49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,0]]
grid.append([81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65])
grid.append([52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91])
grid.append([22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80])
grid.append([24,47,32,60,99,3,45,2,44,75,33,53,78,36,84,20,35,17,12,50])
grid.append([32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70])
grid.append([67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21])
grid.append([24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72])
grid.append([21,36,23,9,75,0,76,44,20,45,35,14,0,61,33,97,34,31,33,95])
grid.append([78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92])
grid.append([16,39,5,42,96,35,31,47,55,58,88,24,0,17,54,24,36,29,85,57])
grid.append([86,56,0,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58])
grid.append([19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40])
grid.append([4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66])
grid.append([88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69])
grid.append([4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36])
grid.append([20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16])
grid.append([20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54])
grid.append([1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48])
maxValue=0
for x in range(16):
    for y in range(20):
        across = grid[x][y] * grid[x + 1][y] * grid[x + 2][y] * grid[x + 3][y]
        maxValue = max(maxValue, across)
for x in range(20):
    for y in range(16):
        down = grid[x][y] * grid[x][y + 1] * grid[x][y + 2] * grid[x][y + 3]
        maxValue = max(maxValue, down)
for x in range(16):
    for y in range(16):
        diag = grid[x][y] * grid[x + 1][y + 1] * grid[x + 2][y + 2] * grid[x + 3][y + 3]
        maxValue = max(maxValue, diag)
for x in range(0,16):
    for y in range(4,20):
        diag = grid[x][y] * grid[x + 1][y - 1] * grid[x + 2][y - 2] * grid[x + 3][y - 3]
        maxValue = max(maxValue, diag)
print("Problem 11: " + str(maxValue))
#Problem 12: triangular number w/ over 500 divisors
def numDivisors(x):
    count=0
    for i in range(1,int(x**.5)):
        if x%i==0:
            count+=1
    count*=2
    #if (x**.5)%1==0:
    #    count+=1
    return count
num=0
add=1
answer=None
while answer is None:
    num+=add
    add+=1
    if numDivisors(num)>500:
        answer=num
print("Problem 12: " + str(answer))
# Problem 14: longest iterative chain n → n/2 (n is even) n → 3n + 1 (n is odd)
values={1:1}
def seqCount(number):
    count=0
    x=number
    while x not in values:
        if x%2==0:
            x=x/2
        else:
            x=3*x+1
        count+=1
    values[number]=count+values[x]

maxValue=1
for i in range(2,1000000):
    if i not in values.keys():
        seqCount(i)
    if values[maxValue]<values[i]:
        maxValue=i
print("Problem 14: " + str(maxValue))
# Problem 17
ones={0:"",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen"}
tens={2:"Twenty",3:"Thirty",4:"Forty",5:"Fifty",6:"Sixty",7:"Seventy",8:"Eighty",9:"Ninety"}
def letters(x):
    count=0
    if x>=100:
        count+=len(ones[int(x/100)])
        if x%100==0:
            count+=len("Hundred")
        else:
            count += len("HundredAnd")
        x=x%100
    if x>=20:
        count+=len(tens[int(x/10)])
        x=x%10
    count+=len(ones[x])
    return count
total=len("OneThousand")
for i in range(1,1000):
    total+=letters(i)
print("Problem 17: " + str(total))
# 18 using the brute force solution; the clever solution is probably too hard for week 1
triangle = [[75],[95, 64]]
triangle.append([17, 47, 82])
triangle.append([18, 35, 87, 10])
triangle.append([20, 4, 82, 47, 65])
triangle.append([19, 1, 23, 75, 3, 34])
triangle.append([88, 2, 77, 73, 7, 63, 67])
triangle.append([99, 65, 4, 28, 6, 16, 70, 92])
triangle.append([41, 41, 26, 56, 83, 40, 80, 70, 33])
triangle.append([41, 48, 72, 33, 47, 32, 37, 16, 94, 29])
triangle.append([53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14])
triangle.append([70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57])
triangle.append([91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48])
triangle.append([63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31])
triangle.append([4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23])
maximums = []
def maxes(matrix, posx, posy, sum):
    sum += matrix[posx][posy]
    if posx == 14:
        maximums.append(sum)
    else:
        maxes(matrix, posx + 1, posy + 1,sum)
        maxes(matrix, posx + 1, posy,sum)
maxes(triangle, 0, 0, 0)
print("Problem 18: %s " % max(maximums))
#problem 30
specials=[]
for num in range(2,1000000):
    digits=[int(char) for char in str(num)]
    total=sum([i**5 for i in digits])
    if num==total:
        specials.append(num)
print("Problem 30: " + str(sum(specials)))