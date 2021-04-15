from math import log
import random, time, sys

message=" ".join(sys.argv[1:])
times=time.perf_counter()
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n_grams={}
N=3
POPULATION_SIZE=500#or 300?
NUM_ClONES=3
TOURNAMENT_SIZE=20
TOURNAMENT_WIN_PROBABILITY=.75
CROSSOVER_LOCATIONS=11 #optimal
MUTATION_RATE=.5#optimal
answer=""
STABLE=70
if len(message)<350:
    POPULATION_SIZE = 700
    #STABLE=100

#populate n_grams
with open("ngrams.txt") as f:
    for line in f:
        line=line.strip()
        segment,number=line.split(" ")
        n_grams[segment]=int(number)


def encode(cipherbet,m):
    encrypted=""
    for letter in m:
        if letter not in alphabet:
            encrypted+=letter
        else:
            ind=alphabet.index(letter)
            encrypted+=cipherbet[ind]
    return encrypted

def decodes(cipherbet, encrypted):
    for i in range(26):
        encrypted=encrypted.replace(cipherbet[i],"%"+str(cipherbet.index(cipherbet[i]))+"*")
    for i in range(26):
        encrypted=encrypted.replace("%"+str(i)+"*",alphabet[i])
    return encrypted


def decode(cipherbet, encrypted):
    m=""
    for letter in encrypted:
        if letter not in alphabet:
            m+=letter
        else:
            ind=cipherbet.index(letter)
            m+=alphabet[ind]
    return m

def random_cipher():
    cipherbet = list(alphabet)
    random.shuffle(cipherbet)
    return "".join(cipherbet)

# def test_fitness(n, code):
#     sum=0
#     for i in range(0,len(code)-n):
#         fragment=code[i:i+n]
#         if fragment.isalpha():
#             freq=n_grams.get(fragment,0)
#             if freq>0:
#                 sum+=log(freq,4)
#     return sum

def test_fitness(n, cipher):
    sum=0
    code=decode(cipher,message)
    for i in range(0,len(code)-n):
        fragment=code[i:i+n]
        if fragment.isalpha():
            freq=n_grams.get(fragment,0)
            if freq>0:
                sum+=log(freq,2)
    return sum

def mutate(cipherbet):
    ind1,ind2=random.sample(range(26),2)
    # ind1=random.randint(0,25)
    # ind2=ind1
    # while ind2==ind1:
    #     ind2=random.randint(0,25)
    #print("Swap "+ cipherbet[ind1] + cipherbet[ind2])
    if ind1>ind2:
        temp=ind1
        ind1=ind2
        ind2=temp
    return cipherbet[:ind1]+cipherbet[ind2]+cipherbet[ind1+1:ind2]+cipherbet[ind1]+cipherbet[ind2+1:]

def hill_climbing(cipherbet):
    fitness=test_fitness(N,cipherbet)
    for i in range(100): #arbitrary, goes infinitely
        new_cipher=mutate(cipherbet)
        new_fitness=test_fitness(N,new_cipher)
        if new_fitness>fitness:
            fitness=new_fitness
            cipherbet=new_cipher
            print(decode(cipherbet,message))
            print()
    return cipherbet

def crossover(cipher1,cipher2,stable):
    child_cipher=[]
    for i in range(26):
        if random.random()<.5:
            child_cipher.append(cipher1[i])
        else:
            child_cipher.append(cipher2[i])
    missing=[letter for letter in alphabet if letter not in child_cipher]
    random.shuffle(missing)
    for i in range(26):
        if child_cipher.count(child_cipher[i])>1:
            child_cipher[i]=missing.pop()
    child="".join(child_cipher)
    #MUTATE
    if random.random()<(1-MUTATION_RATE**(stable/10)):
        return mutate(child)
    return child

def crossoverold(cipher1,cipher2):
    child_cipher=[""]*26
    indices=random.sample(range(0,26),CROSSOVER_LOCATIONS)
    for ind in indices:
        child_cipher[ind]=cipher1[ind]
    ind=0
    child_ind=0
    while child_ind<26:
        if child_cipher[child_ind]!="":
            child_ind+=1
        elif cipher2[ind] in child_cipher:
            ind+=1
        else:
            child_cipher[child_ind]=cipher2[ind]
    child= "".join(child_cipher)
    #MUTATE
    if random.random()<MUTATION_RATE:
        child=mutate(child)
    #fitness=test_fitness(N,child)
    return child

def tournament(parents,stable):
    contestants = random.sample(parents.keys(), TOURNAMENT_SIZE * 2)
    tourney1, tourney2 = contestants[:TOURNAMENT_SIZE], contestants[TOURNAMENT_SIZE:]
    winner1, winner2 = None, None
    while winner1 is None:
        winner1 = max(tourney1)
        if random.random() > TOURNAMENT_WIN_PROBABILITY:
            tourney1.remove(winner1)
            winner1 = None
    while winner2 is None:
        winner2 = max(tourney2)
        if random.random() > TOURNAMENT_WIN_PROBABILITY:
            tourney2.remove(winner2)
            winner2 = None
    #if random.random()>.65:
    #    return parents[winner1]
    return crossover(parents[winner1],parents[winner2],stable)

def new_generation(parents,gen,stable):
    print(str(stable)+" " + str(N))
    # Just checking best cipher
    code = decode(parents[max(parents.keys())], message)
    print(code)
    print()
    #if gen==0:
    #    return parents
    if stable==0:
        return parents
    children=set()#contains only ciphers
    #CLONING TOP PARENTS
    fitnesses=sorted(parents.keys())
    for fitness in fitnesses[:-NUM_ClONES-1:-1]:
        children.add(parents[fitness])
    #ADD SOME RANDOM
    for i in range(10):
        children.add(random_cipher())
    #TOURNAMENT USING FITNESSES INSTEAD OF CIPHERS
    while len(children)<POPULATION_SIZE:
        child=tournament(parents,stable)
        children.add(child)
    child_fitnesses={}
    for cipher in children:
        child_fitnesses[test_fitness(N, cipher)] = cipher  # key=fitness,value=cipher
    if max(child_fitnesses.keys())==fitnesses[-1]:
        stable-=1
    else:
        stable=STABLE
    return new_generation(child_fitnesses,gen-1,stable)


# cipherbet="XRPHIWGSONFQDZEYVJKMATUCLB"
# print("hello".upper())
# code=encode(cipherbet,"HELLO, students!")
# print(code)
# message=decode(cipherbet,code)
# print(message)

#hill_climbing()
#POPULATION_SIZE=200
parents=set()
while len(parents)<POPULATION_SIZE:
    temp=random_cipher()#temp=alphabet string
    parents.add(temp)

population={}
for cipher in parents:
    population[test_fitness(N,cipher)]=cipher #key=fitness,value=cipher

N=3
population=new_generation(population,700,STABLE)

N=4
#STABLE*=2
population=new_generation(population,500,STABLE)

N=5
NUM_ClONES=5
#STABLE//=2
population=new_generation(population,500,STABLE)

N=3
STABLE=20
#population=new_generation(population,500,STABLE)

#print(decode(population[max(population.keys())],message))

max_sum=0
max_cipher=""
for cipher in range(population.values()):
    sum=test_fitness(3,cipher)+test_fitness(4,cipher)+test_fitness(5,cipher)
    if sum>max_sum:
        max_sum=sum
        max_cipher=cipher

print(decode(max_cipher,message))

print()
print(str(time.perf_counter()-times) + "s")


