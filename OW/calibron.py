import sys

# You are given code to read in a puzzle from the command line.  The puzzle should be a single input argument IN QUOTES.
# A puzzle looks like this: "56 56 28x14 32x11 32x10 21x18 21x18 21x14 21x14 17x14 28x7 28x6 10x7 14x4"
# The code below breaks it down:
puzzle = sys.argv[1].split()
puzzle_height = int(puzzle[0])
puzzle_width = int(puzzle[1])
rectangles = [(int(temp.split("x")[0]), int(temp.split("x")[1])) for temp in puzzle[2:]]
# puzzle_height is the height (number of rows) of the puzzle
# puzzle_width is the width (number of columns) of the puzzle
# rectangles is a list of tuples of rectangle dimensions

def is_possible():
    sum=puzzle_width*puzzle_height
    for x,y in rectangles:
        sum-=x*y
    return sum==0

def print_puzzle(filled):
    filled=filled.replace(" ","-")
    for ind in range(0,puzzle_width*puzzle_height,puzzle_width):
        print(filled[ind:ind+puzzle_width])
    print()

# def get_children(rect,filled):
#     l1=min(rect)
#     l2=max(rect)
#     index=filled.index(" ")
#     if is_valid(filled)
#     if index%puzzle_width+l1>puzzle_width:
#         return None
#     if "x" in filled[index:index+l1]:
#         return None
#     #place long way

def place_piece(filled,height,width):
    index = filled.index(" ")
    if index % puzzle_width + width > puzzle_width: #no space on right
        return None,None
    if index // puzzle_width + height > puzzle_height: #no space on bottom
        return None,None
    for h in range(index,index+puzzle_width*height,puzzle_width): #already filled
        if "x" in filled[h:h+width]:
            return None,None
        filled=filled[:h]+ "x"*width + filled[h+width:]
    tup=(index//puzzle_width,index%puzzle_width,height,width)
    return tup,filled


def solve(used,filled,rects):
    if " " not in filled:
        return used
    next_piece=rects[-1]
    for next_piece in rects:
        tup,new_filled=place_piece(filled,next_piece[0],next_piece[1]) #trying 1st orientation
        new_rects=rects.copy()
        new_rects.remove(next_piece)
        if new_filled is not None:
            new_used=solve(used+[tup],new_filled,new_rects)
            if new_used is not None:
                return new_used
        tup,new_filled=place_piece(filled,next_piece[1],next_piece[0]) #trying 2nd orientation
        if new_filled is not None:
            new_used = solve(used+[tup], new_filled, new_rects)
            if new_used is not None:
                return new_used
    return None



if not is_possible():
    print("Containing rectangle incorrectly sized.")
else:
    used=solve([]," "*(puzzle_width*puzzle_height),rectangles.copy())
    if used==None:
        print("No solution.")
    else:
        for item in used:
            print(str(item[0])+ " "+str(item[1])+ " "+str(item[2])+ " "+str(item[3]))