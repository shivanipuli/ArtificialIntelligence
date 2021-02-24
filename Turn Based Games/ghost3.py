import sys

filename=sys.argv[1]
min_length=int(sys.argv[2])
word=""
if len(sys.argv)==4:
    word=sys.argv[3]

dictionary=[]
with open(filename) as f:
    for line in f:
        line=line.strip()
        line=line.upper()
        if line.isalpha():
            if line[0:len(word)]==word and len(line)>=min_length:
                dictionary.append(line)
        #    word_length_dict[len(line)]=word_length_dict.get(len(line),[])+[line]

def next_letter(word, possibilities):
    letters={}
    ind=len(word)
    for w in possibilities:
        letters[w[ind]]=letters.get(w[ind],[])+[w]
    return letters

def max_step(word,possibilities,turn):
    if word in possibilities:
        if turn==1:
            return -1
        return 1
    outcomes=[]
    next_move = next_letter(word, possibilities)
    for letter in next_move.keys():
        new_word=word+letter
        result=max_step(new_word,next_move[letter], (turn+1)%3)
        outcomes.append(result)
    return min(outcomes)

def min_step(word,possibilities,turn):
    if word in possibilities:
        return (turn-1)%3
    outcomes=[]
    next_move=next_letter(word,possibilities)
    for letter in next_move.keys():
        new_word=word+letter
        outcome=max_step(new_word,next_move[letter], (turn+1)%3)
        outcomes.append(outcome)
    return min(outcomes)

def compTurn(word,possible):
    #turn=number from 0 to 2
    #print(word)
    guarantee_success=[]
    next_move=next_letter(word,possible)
    for letter in next_move.keys():
        new_word=word+letter
        outcome=max_step(new_word,next_move[letter], 1)
        if outcome==1:
            guarantee_success.append(letter)
    if len(guarantee_success)>0:
        print("Next player can win by with any of these letters: " + str(guarantee_success))
        #letter = input("Your choice?")
        letter=guarantee_success[0]
        new_word = word + letter
        new_possible = next_move[letter]
        #compTurn(new_word, new_possible)
    else:
        print("Next player will lose!")


compTurn(word,dictionary)