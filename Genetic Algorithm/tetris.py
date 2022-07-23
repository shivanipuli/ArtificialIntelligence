import sys, time
import random,statistics


POPULATION_SIZE=100#or 300?
NUM_ClONES=POPULATION_SIZE//6
TOURNAMENT_SIZE=20
TOURNAMENT_WIN_PROBABILITY=.75
#CROSSOVER_LOCATIONS=11 #optimal
MUTATION_RATE=.2#optimal
NUM_STRATS=3

board="".join(sys.argv[1:])#200 char string
board = "          #         #         #      #  #      #  #      #  #     ##  #     ##  #     ## ##     ## #####  ########  ######### ######### ######### ######### ########## #### # # # # ##### ###   ########"
outcomes=[]
pieces={"I":["####5","#5#5#5#5"],"O":["##5##5"],"T":["###5 # 5","# 5##5# 5"," # 5###5"," #5##5 #5"],"S":["## 5 ##5"," #5##5# 5"],"Z":[" ##5## 5","# 5##5 #5"],"J":["###5#  5","# 5# 5##5","  #5###5","##5 #5 #5"],"L":["###5  #5","##5# 5# 5","#  5###5"," #5 #5##5"]}

def print_board(board):
    if board=="GAME OVER":
        print("GAME OVER")
    else:
        print("=======================")
        for count in range(20):
            print(' '.join(list(("|" + board[count * 10: (count + 1) * 10] + "|"))), count)
        print("=======================")
        #print()
        print("  0 1 2 3 4 5 6 7 8 9  ")
        print()

def find_last_row(board,block,col):
    last_row=None
    for row in range(20):
        if last_row is None:
            for c in range(block.index("5")):
                if board[row*10+col+c]=="#" and block[c]=="#":
                    last_row=row-1
    return 19

def eliminate_rows(board):
    num=0
    for i in range(20):
        if board[i*10:i*10+10]=="#"*10:
            board=(" "*10)+board[:i*10]+board[i*10+10:]
            num+=1
    return board,num
    # if num==0:
    #     return board,0
    # elif num==1:
    #     return board,40
    # elif num==2:
    #     return board,100
    # elif num==3:
    #     return board,300
    # elif num==4:
    #     return board,1200
    # else:
    #     return board,num*300

def place_block_on_row(board,block,col,last_row):
    if col+block.index("5")>10: #if it goes over the edge
        return "GAME OVER"
    #last_row=find_last_row(board,block,col)
    ind=last_row*10+col
    for l in block:
        if last_row<0:
            return "GAME OVER"
        if l=="5": #next row
            last_row-=1
            ind=last_row*10+col
        elif board[ind]=="#" and l=="#": #only case with clashing
            return "GAME OVER"
        else:
            if l=="#":
                board=board[:ind]+"#"+board[ind+1:] #or "R"
            #print_board(board)
            ind+=1
    return board#eliminate_rows(board)

def place_block(board,block,col):
    possible=True
    best_board="GAME OVER"
    for row in range(block.count("5")-1,20):
        b=place_block_on_row(board,block,col,row)
        if b=="GAME OVER":
            return best_board
        else:
            best_board=b
    return best_board


#<-------TETRIS MODELLING---------------->

# mytime=time.perf_counter()
# #print_board(board)
# #print_board(place_block(board,pieces["T"][1],5))
# f=open("tetrisout.txt","x")
# for piece in pieces:
#     for orientation in pieces[piece]:
#         for col in range(11-orientation.index("5")):
#             outcome = place_block(board, orientation, col)
#             outcome = eliminate_rows(outcome)[0]
#             print_board(outcome)
#             outcomes.append(outcome)
#             f.write(outcome)
#             f.write("\n")
# f.close()
# print_board(board)
# print(time.perf_counter()-mytime)


#Countermeasures in tetris board: how high up the tetris # gets on board
# for scoring a tetris board, I think height, number of blocks,
# and number of closed off holes, or overhangs would be useful
def heuristic(board,strategy):
    #ROUGHNESS,HOLES=strategy
    ROUGHNESS,ROW,HOLES = strategy
    #ROUGHNESS,HOLES,ROW,TOTBLOCKS=strategy
    if board=="GAME OVER":
        return -10000
    value=0
    # #highest column level
    # high_col=19
    # if "#" in board:
    #     high_col=board.index("#")//10
    # value+=HIGHCOL*high_col #higher up = lower row # = less points

    # max height in each column
    # heights=0
    # for col in range(10):
    #     vars=[board[i] for i in range(col,200,10)]
    #     if "#" in vars:
    #         heights+=(vars.index("#"))
    # value+=MAXH*heights

    # number of holes
    #holes = ([board[i] == " " and board[i - 10] == "#" for i in range(10, 200)]).count(True)
    #value += (HOLES ** 2)* holes  # more holes=less points
    holes=0
    heights = []
    for col in range(10):
        vars=[board[i] for i in range(col,200,10)]
        if "#" in vars:
            heights.append(vars.index("#"))
            below=vars[heights[-1]:]
            if " " in below:
                holes+=below.count(" ")
        else:
            heights.append(0)
        # value+=MAXH*heights
    roughness=0
    for i in range(9):
        roughness+=abs(heights[i]-heights[i+1])

    value += (HOLES ** 3) * holes
    value+=(ROUGHNESS**3)*roughness
    lastrow=19
    if "#" in board:
        lastrow=board.index("#")//10
    value+=(ROW**3)*lastrow
    # #completed rows
    # board, rows = eliminate_rows(board)
    # value+=COMPROWS*rows #more comp rows=more points

    #total number of blocks
    #value+=(TOTBLOCKS**3)*board.count("#") #more filled = less points

    return value


def play_game(strategy):
    board=" "*200
    points=0
    while board!="GAME OVER":
        #print_board(board)
        poss_scores={}
        piece=random.choice(list(pieces.keys()))
        for orientation in pieces[piece]:
            for col in range(11 - orientation.index("5")):
                poss_board=place_block(board,orientation,col)
                poss_score=heuristic(poss_board,strategy)
                poss_scores[poss_score]=poss_board
        board=poss_scores[max(poss_scores.keys())]

        #eliminated rows
        board,num=eliminate_rows(board)
        new_points=num*300
        if num == 1:
            new_points= 40
        elif num == 2:
            new_points=100
        elif num == 3:
            new_points=300
        elif num == 4:
            new_points= 1200
        points+=new_points
    #print_board(board)
    return points

def play_game_print(strategy):
    board=" "*200
    points=0
    while board!="GAME OVER":
        print_board(board)
        print("Current Score: " + str(points))
        poss_scores={}
        piece=random.choice(list(pieces.keys()))
        for orientation in pieces[piece]:
            for col in range(11 - orientation.index("5")):
                poss_board=place_block(board,orientation,col)
                poss_score=heuristic(poss_board,strategy)
                poss_scores[poss_score]=poss_board
        board=poss_scores[max(poss_scores.keys())]

        #eliminated rows
        board,num=eliminate_rows(board)
        if num == 1:
            points+= 40
        elif num == 2:
            points+=100
        elif num == 3:
            points+=300
        elif num == 4:
            points+= 1200
    #print_board(board)
    return points

def test_fitness(strategy):
    scores=0
    for i in range(5):
        scores+=play_game(strategy)
    return scores/5



def breed(parent1,parent2):
    child=[]
    for i in range(NUM_STRATS):
        if random.random() < .5:
            child.append(parent1[i])
        else:
            child.append(parent2[i])
    # MUTATE
    if random.random() < MUTATION_RATE:
        index = random.randint(0, NUM_STRATS - 1)
        val=child[index]+random.uniform(-.1,.1)
        while val>1 or val<-1:
            val = child[index] + random.uniform(-.05, .05)
        child[index] = val
    return child

def find_max_inds(fitnesses,count):
    ordered=sorted(fitnesses)
    ordered=ordered[:-count-1:-1]
    inds=[]
    add_to_ind=0
    for fitness in ordered:
        for i in range(len(fitnesses)):
            if fitnesses[i]==fitness:
                inds.append(i)
            if len(inds)==count:
                return inds

def tournament(strats,fits):
    contestants=random.sample(strats,TOURNAMENT_SIZE*2)
    tourney1,tourney2=contestants[:TOURNAMENT_SIZE], contestants[TOURNAMENT_SIZE+1:]
    #newstrats=contestants
    newfits=[]
    for strat in contestants:
        newfits.append(fits[strats.index(strat)])
    max_inds=find_max_inds(newfits,40)
    max1=max_inds.copy()
    winner1, winner2 = None, None  # keeps track of winning indexes
    while winner1 is None:
        ind = max1.pop(0)
        if contestants[ind] in tourney1:
            winner1 = contestants[ind]
            if random.random() > TOURNAMENT_WIN_PROBABILITY and len(max1)>0:
                winner1 = None
    while winner2 is None:
        ind = max_inds.pop(0)
        if contestants[ind] in tourney2:
            winner2 = contestants[ind]
            if random.random() > TOURNAMENT_WIN_PROBABILITY and len(max_inds)>0:
                winner2 = None
    # if random.random()>.65:
    #    return parents[winner1]
    return breed(winner1, winner2)

def tournamentold(strats,fits): #parent fitnesses
    contestants = random.sample(range(POPULATION_SIZE), TOURNAMENT_SIZE * 2)
    tourney1, tourney2 = contestants[:TOURNAMENT_SIZE], contestants[TOURNAMENT_SIZE:]#two lists of strategies
    max_inds=find_max_inds(fits,18)
    max1=max_inds.copy()
    winner1, winner2 = None, None#keeps track of winning indexes
    while winner1 is None:
        ind=fits.index(max(fits))
        if ind in tourney1:
            winner1=ind
            if random.random() > TOURNAMENT_WIN_PROBABILITY:
                winner1 = None
    while winner2 is None:
        ind = max_inds.pop(0)
        if ind in tourney2:
            winner2 = ind
            if random.random() > TOURNAMENT_WIN_PROBABILITY:
                winner2 = None
    # if random.random()>.65:
    #    return parents[winner1]
    return breed(strats[winner1], strats[winner2])

def find_max(fitnesses,count):
    indices={}
    for ind,fitness in enumerate(fitnesses):
        indices[fitness]=1
    max_vals=sorted(fitnesses)
    max_vals=max_vals[:-count-1:-1]
    inds=[]
    for fitness in max_vals:
        inds.append(indices[fitness])
    return inds

def new_generation(parentstrats,parentfits,gen):
    childstrats=[]  # contains only strats
    childfits=[]

    # if gen < 5:
    #     maxfit = max(parentfits)
    #     maxstrat = parentstrats[parentfits.index(maxfit)]
    #     print("Best Strategy: " + str(maxstrat))
    #     print(" Best fitness: " + str(maxfit))  # prints best strategy
    #     print("Average fitness: " + str(sum(parentfits) / POPULATION_SIZE))
    #     print((time.perf_counter() - mytime) / 60)
    if gen==5:
        maxfit = max(parentfits)
        maxstrat = parentstrats[parentfits.index(maxfit)]
        print("Best Strategy: " + str(maxstrat))
        print("Best fitness: " + str(maxfit))  # prints best strategy
        print("Average fitness: " + str(sum(parentfits) / POPULATION_SIZE))
        print((time.perf_counter() - mytime) / 60)
        return parentstrats,parentfits


    # CLONING TOP PARENTS
    for ind in find_max_inds(parentfits,NUM_ClONES):
        childstrats.append(parentstrats[ind])
        childfits.append(parentfits[ind])

    #BREEDING PROCESS
    while len(childstrats)<POPULATION_SIZE:
        strat=tournament(parentstrats,parentfits)
        childstrats.append(strat)
        childfits.append(test_fitness(strat))

    return new_generation(childstrats,childfits,gen+1)

def random_gen_0():
    #f = open("strategies.txt", "x")
    strategies = []
    fitnesses = []
    for i in range(POPULATION_SIZE):
        strategy = [random.uniform(-1, 1) for y in range(NUM_STRATS)]
        strategies.append(strategy)
        fitnesses.append(test_fitness(strategy))
        #strategy=[str(i) for i in strategy]
        #f.write(" ".join(strategy))
        #f.write("\n")
    #f.close()
    return strategies,fitnesses

def load_gen_0(filename):
    strategies=[]
    fitnesses=[]
    with open(filename) as f:
        for line in f:
            strat=line.strip()
            strat=strat.split(" ")
            strat=[float(i) for i in strat]
            if len(strat)==NUM_STRATS+1:
                strategies.append(strat[:-1])
                fitnesses.append(strat[-1])
            else:
                strategies.append(strat)
                fitnesses.append(test_fitness(strat))
    return strategies,fitnesses

mytime=time.perf_counter()

answer=input("Load strategies (Type L) or create new strategies(Type N)? ")
strategies,fitnesses=[],[]
if answer=="L":
    filename=input("Enter full filename: ")
    strategies,fitnesses=load_gen_0(filename)
    new_generation(strategies,fitnesses,5)
else:
    strategies,fitnesses=random_gen_0()
    new_generation(strategies, fitnesses, 5)
POPULATION_SIZE=len(strategies)

while answer!="E":
    answer=input("Save strategies (S) or watch best game (B) or evolve new generation(G) or end(E)? ")
    if answer=="S":
        filename=input("Enter new filename: ")
        f=open(filename,"x")
        for ind in range(len(strategies)):
            strat=[str(i) for i in strategies[ind]]+[str(fitnesses[ind])]
            f.write(" ".join(strat))
            f.write("\n")
        f.close()
    elif answer=="B":
        beststrat=strategies[fitnesses.index(max(fitnesses))]
        play_game_print(beststrat)
    elif answer=="G":
        strategies,fitnesses=new_generation(strategies,fitnesses,4)

print(time.perf_counter()-mytime)
#print("HOLES ROUGHNESS TOTBLOCKS")
#print("ROUGHNESS HOLES")
print("ROUGHNESS,ROW,HOLES")
#print("ROUGHNESS,HOLES,ROW,TOTBLOCKS")
