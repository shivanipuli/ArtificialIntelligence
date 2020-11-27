import math
def is_prime(x):
    for i in range(2,1+int(x**.5)):
        if x%i==0:
            return False
    return True
#problem 1: sum of all multiples of 3 and 5
print("Problem 1: %s" % sum(i for i in range(1000) if i%3==0 or i%5==0))
#problem 2: sum of even fibonacci less than 4 million
nums=[1,2]
evens=[2]
while nums[0]<4000000 and nums[1]<4000000:
    nums.append(sum(nums))
    if nums[2]%2==0:
        evens.append(nums[2])
    nums.pop(0)
print("Problem 2: %s" %sum(evens))
#problem 3: largest prime factor of 600851475143
maxPrime=1
num=600851475143
for i in range(2,int(num**.5)):
    while num%i==0:
        maxPrime=i
        num=num/i
print("Problem 3: %s" %maxPrime)
#problem 4: largest palindrome made from the product of two 3-digit numbers
maxProd=1
for x in range(100,1000):
    for y in range(100,1000):
        product=x*y
        if str(product)==str(product)[::-1]:
            maxProd=product
print("Problem 4: %s" %maxProd)
#problem 7: 1001st prime number
primes=[2]
currNum=3
while(len(primes)<1001):
    if is_prime(currNum):
        primes.append(currNum)
    currNum+=1
print("Problem 7: %s" %primes[-1])
#problem 8: largest greatest product of 13 adjacent numbers
num=7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
nums=[int(i) for i in str(num)]
maxNum=0
for i in range(1000-13):
    sublist=nums[i:i+13]
    product=1
    for x in sublist:
        product*=x
    if product>maxNum:
        maxNum=product
print("Problem 8:" + str(maxNum))

#problem 9: a + b + c = 1000  a2 + b2 = c2
triangle=()
for x in range(1,1000):
    for y in range(1,1000):
        z=(x**2+y**2)**.5
        if x+y+z==1000:
            triangle=(x,y,z//1)
print("Problem 9:" + str(triangle))


