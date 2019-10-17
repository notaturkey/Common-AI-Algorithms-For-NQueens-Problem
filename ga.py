import random
import copy

def initBoard(n):
    arr =[] 
    for i in range(n):
        arr.append(random.randint(0,n-1))
    return arr

def checkScore(board):
    temp = 0
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

def fitness(arr):
    new = arr[0:int(len(arr)/4)+1]
    return new

def mutate(arr):
    result = []
    result.append(arr[0][1])
    temp = int(len(arr)/2)
    for i in range(99):
        mutant = copy.deepcopy(arr[random.randint(0, len(arr)-1)][1])
        mutant[random.randint(0,7)] = random.randint(0,7)
        result.append(mutant)
    return result



def geneticAlgo(chromo,maxRuns):
    global bestScore
    scores = []
    if maxRuns == 0:
        print("best solution so far")
        return bestScore

    for i in chromo:
        if isSolved(i):
            print("Solved board")
            print("took " + str(300 - maxRuns) + " runs to get there")
            return i
        else:
            scores.append([checkScore(i), i])
    
    scores = sorted(scores)
    if bestScore > scores[0]:
        bestScore = scores[0]
    
    fit = fitness(scores)
    nextpop = mutate(copy.deepcopy(fit))
    return geneticAlgo(nextpop,maxRuns-1)






print("#######################################")
print("#######################################")
print("Genetic Algorithm:")
print("#######################################")
print("#######################################")

fitMax = 0
population = []
bestScore = [1000, []]
maxRuns = 300
for i in range(100):
    population.append(initBoard(8))

print(str(geneticAlgo(population, maxRuns)))