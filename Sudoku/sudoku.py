import sys, time

N, subblock_height, subblock_width, symbol_set, indToBox, boxToInd = 0, 0, 0, set(), dict(), dict()


def print_board(board):
    for row in range(N):
        if row % subblock_height == 0:
            print()
        for split in range(subblock_height):
            left = (N * row + split * subblock_width)
            right = N * row + (split + 1) * subblock_width
            print(" ".join(board[left:right]), end="   ")
        print()


def make_constraints(board):
    N = int(len(board) ** .5)
    symbols = "123456789ABCDEFGHIJKLMNOPQRSTUVQXYZ"
    symbols = symbols[:N]
    symbol_set = set(symbols)
    if "." in symbol_set:
        symbol_set.remove(".")
    height = -1
    i = int(N ** .5)
    while i < N and height == -1:
        if N % i == 0:
            height = i
        i += 1
    width = N // height

    indToBox = {}  # {0:0,1:0,2:1}
    boxToInd = {}  # {0:[0,1],1:[2,3]}
    box = -1
    for x in range(height * width):
        if x % height != 0:
            box -= height
        for y in range(height * width):
            ind = x * height * width + y
            if y % width == 0:
                box += 1
            indToBox[ind] = box
            lis = boxToInd.get(box, [])
            boxToInd[box] = lis + [ind]
    return N, height, width, symbol_set, indToBox, boxToInd


def is_valid(state, ind, symbol):
    row = ind // N
    col = ind % N
    box = indToBox[ind]
    for r in range(N):  # checks every character in column
        indy = r * N + col
        if state[indy] == symbol:
            return False
        # for r in range(N): #checks every character in row
        indl = row * N + r
        if state[indl] == symbol:
            return False
    for index in boxToInd[box]:
        if state[index] == symbol:
            return False
    return True


def get_sorted_values(dictionary, ind):
    return dictionary[ind]
    # mylis=[item for item in symbol_set if is_valid(state,ind,item)]
    # return mylis


def get_next_unassigned_variable(state, possible, ones):
    if len(ones) > 0:
        return ones.pop()
    minNum = 10
    minInd = -1
    for index in range(N ** 2):
        if 0 < len(possible[index]) < minNum:
            minNum = len(possible[index])
            minInd = index
    return minInd


def forward_look(state, mdict, index, symbol, ones):
    mdict[index] = ""
    box = indToBox[index]
    for ind in boxToInd[box]:
        # if ind!=index and state[ind]==".":
        a = mdict[ind]
        if symbol in a:
            a = a.replace(symbol, "")
            if len(a) == 1:
                ones.add(ind)
            if len(a) == 0:
                return None, None
            mdict[ind] = a
    row = index // N
    for ind in range(N * row, N * (row + 1)):
        a = mdict[ind]
        if symbol in a:
            a = a.replace(symbol, "")
            if len(a) == 1:
                ones.add(ind)
            if len(a) == 0:
                return None, None
            mdict[ind] = a
    col = index % N
    for ind in range(col, N * (N) + col, N):
        a = mdict[ind]
        if symbol in a:
            a = a.replace(symbol, "")
            if len(a) == 1:
                ones.add(ind)
            if len(a) == 0:
                return None, None
            mdict[ind] = a
    return mdict, ones


def populate(board):
    options = []
    ones = set()
    for index in range(len(board)):
        ad = ""
        if board[index] == ".":
            ad = "".join([symbol for symbol in symbol_set if is_valid(board, index, symbol)])
            if len(ad) == 1:
                ones.add(index)
        options.append(ad)
    return options, ones


def constraint_propagation(state, dict):
    for box in range(N):
        objects = [state[index] for index in boxToInd[box]]
        for symbol in symbol_set:
            if symbol not in objects:
                present = [symbol in dict[index] for index in boxToInd[box]]
                if present.count(True) == 0:
                    return None, None
                if present.count(True) == 1:
                    index = boxToInd[box][present.index(True)]
                    state = state[:index] + symbol + state[index + 1:]
                    dict[index] = ""
    for row in range(N):
        objects = [state[index] for index in range(N * row, N * (row + 1))]
        for symbol in symbol_set:
            if symbol not in objects:
                present=[symbol in dict[index] for index in range(N*row,N*row+N)]
                if present.count(True) == 0:
                    return None, None
                if present.count(True) == 1:
                    index = row*N+present.index(True)
                    state = state[:index] + symbol + state[index + 1:]
                    dict[index] = ""
    for col in range(N):
        for row in range(N):
            objects = [state[index] for index in range(col, N **2+col,N)]
            for symbol in symbol_set:
                if symbol not in objects:
                    present = [symbol in dict[index] for index in range(col, N **2+col,N)]
                    if present.count(True) == 0:
                        return None, None
                    if present.count(True) == 1:
                        index = col+N * present.index(True)
                        state = state[:index] + symbol + state[index + 1:]
                        dict[index] = ""
    return state,dict


def csp_backtracking2(state, dict, ones):
    #print_board(state)
    if "." not in state:
        return state
    if len(ones)==0:
        state,dict=constraint_propagation(state,dict)
        if dict is None:
            return None
        if "." not in state:
            return state

        #print_board(state)
    index = get_next_unassigned_variable(state, dict, ones)
    for symbol in dict[index]:  # get_sorted_values(dict,index):
        new_state = state[:index] + symbol + state[index + 1:]
        new_dict=dict.copy()
        new_dict[index]=""
        new_dict, new_ones = forward_look(state, new_dict, index, symbol, ones.copy())
        if new_dict is not None:

            result = csp_backtracking2(new_state, new_dict, new_ones)
            if result is not None:
                return result
    return None


def csp_backtracking(state):
    print_board(state)
    if "." not in state:
        return state
    var = get_next_unassigned_variable(state)  # state.index(".")
    for variable in get_sorted_values(state, var):
        new_state = state[:var] + variable + state[var + 1:]
        result = csp_backtracking(new_state)
        if result is not None:
            return result
    return None


def crude_check(board):
    if board is None:
        return False
    counts = set()
    for item in symbol_set:
        counts.add(board.count(item))
    return len(counts) == 1


def check(board):
    for box in range(N):
        myset = set()
        count = 0
        for i in boxToInd[box]:
            if board[i] == ".":
                count += 1
            else:
                myset.add(board[i])
        if len(myset) + count < N:
            return False
    for row in range(N):
        myset = set()
        count = 0
        for i in range(N * row, N * (row + 1)):
            if board[i] == ".":
                count += 1
            else:
                myset.add(board[i])
        if len(myset) + count < N:
            return False
    for col in range(N):
        myset = set()
        count = 0
        for i in range(col, N ** 2 + col, N):
            if board[i] == ".":
                count += 1
            else:
                myset.add(board[i])
        if len(myset) + count < N:
            return False
    return True


boardList = []
with open("Sudoku/" + sys.argv[1]) as f:
#with open("sudoku_puzzles_1.txt") as f:
    boardList = [line.strip() for line in f]

#boardList=[]
#boardList.append("..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..")
#boardList.append("682457913971823645354162872435728169716934258829516734548271396267349581193685427")

mtime = time.perf_counter()
count = 1
for board in boardList:
    N, subblock_height, subblock_width, symbol_set, indToBox, boxToInd = make_constraints(board)
    #print(len(board))
    # print_board(board)
    if check(board):
        dict, ones = populate(board)
        result = csp_backtracking2(board, dict, ones)
        print(result)
        print(str(count) + " " + str(crude_check(result)))
    else:
        print(board)
        #print(str(count) + " False")
    count += 1

print("Total Time: %ss" % (time.perf_counter() - mtime))
