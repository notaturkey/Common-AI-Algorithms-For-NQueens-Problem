import random
import copy

def initBoard(n):
    arr =[] 
    for i in range(n):
        arr.append(random.randint(0,n-1))
    return arr

def checkScore(i,n,board):
    temp = 0
    board[i] = n
    for j in range(len(board)):
        for k in range(len(board)):
            if j == k:
                continue
            if board[j]==board[k]:
                temp = temp+1
            if abs((board[j] - board[k]) / (j-k))==1:
                temp = temp+1
    
    return temp  

def isSolved(board):
    temp = 0
    for j in range(len(board)):
        for k in range(len(board)):
            if j == k:
                continue
            if board[j]==board[k]:
                temp = temp+1
            if abs((board[j] - board[k]) / (j-k))==1:
                temp = temp+1

    if temp == 0:
        return True
    return False


def checkBoard(board):
    temp = []
    temp2 = []
    for i in range(len(board)):
        for n in range(len(board)):
            temp.append(checkScore(i , n, copy.deepcopy(board)))
        temp2.append(temp)
        temp = []

    return temp2

def bestMove(arr, board):
    mini = 500
    for i in arr:
        for j in i:
            if j == "X":
                continue
            if mini > j:
                x = arr.index(i)
                y = i.index(j)
                mini = j
    temp = arr[x]
    temp[y] = "X"

    board[x] = y
    return board


def hillClimb(board):
    if isSolved(copy.deepcopy(board)):
        return board

    moves = checkBoard(board)
    bmove = bestMove(moves, copy.deepcopy(board))

    if board != bmove:
        return hillClimb(copy.deepcopy(bmove))
    else:
        return hillClimb(copy.deepcopy(initBoard(8)))


board = initBoard(8)

print("#######################################")
print("#######################################")
print("Hill climbing technique:")
print("#######################################")
print("#######################################")

print("initialized board (may re initialize):")
print(board)

print("solution: ")
print(str(hillClimb(copy.deepcopy(board))))



