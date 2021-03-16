from math import log
import random, time, sys

message=" ".join(sys.argv[1:])
times=time.perf_counter()
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n_grams={}
N=4
POPULATION_SIZE=500#or 300?
NUM_ClONES=14
TOURNAMENT_SIZE=20
TOURNAMENT_WIN_PROBABILITY=.9
CROSSOVER_LOCATIONS=11 #optimal
MUTATION_RATE=.5#optimal
answer=""

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

def hill_climbing():
    cipherbet = random_cipher()
    code=decode(cipherbet,message)
    fitness=test_fitness(N,code)
    while fitness>0: #arbitrary, goes infinitely
        if time.perf_counter()-times>30:
            return None
        new_cipher=mutate(cipherbet)
        new_message=decode(new_cipher,code)
        new_fitness=test_fitness(N,new_message)
        if new_fitness>fitness:
            fitness=new_fitness
            cipherbet=new_cipher
            code=new_message
            print(code)
            print()

def create_child(cipher1,cipher2):
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
    fitness=test_fitness(N,child)
    return child

def tournament(parents):
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
    return create_child(parents[winner1],parents[winner2])

def new_generation(parents,gen):
    print(gen)
    code=decode(parents[max(parents.keys())],message)
    if code==answer:
        return code
    if gen==500:
        return decode(parents[max(parents.keys())],message)
    children=set()#contains only ciphers
    # Just checking best cipher
    print(code)
    print()
    #CLONING TOP PARENTS
    fitnesses=sorted(parents.keys())
    for fitness in fitnesses[:-NUM_ClONES-1:-1]:
        children.add(parents[fitness])
    #TOURNAMENT USING FITNESSES INSTEAD OF CIPHERS
    while len(children)<POPULATION_SIZE:
        child=tournament(parents)
        children.add(child)
    child_fitnesses={}
    for cipher in children:
        child_fitnesses[test_fitness(N, cipher)] = cipher  # key=fitness,value=cipher
    new_generation(child_fitnesses,gen+1)


# cipherbet="XRPHIWGSONFQDZEYVJKMATUCLB"
# print("hello".upper())
# code=encode(cipherbet,"HELLO, students!")
# print(code)
# message=decode(cipherbet,code)
# print(message)

#hill_climbing()

parents=set()
while len(parents)<POPULATION_SIZE:
    temp=random_cipher()#temp=alphabet string
    parents.add(temp)

population={}
for cipher in parents:
    population[test_fitness(N,cipher)]=cipher #key=fitness,value=cipher

new_generation(population,0)

# print(message)
# print()
# cipher=random_cipher()
# print(decodes(cipher,message))
# print()
# print(decode(cipher,message))

print(time.perf_counter()-times)

