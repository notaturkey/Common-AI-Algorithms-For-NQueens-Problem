import random
import copy

def initBoard(n):
    arr =[] 
    for i in range(n):
        arr.append(random.randint(0,n-1))
    return arr

class Particle():
    def __init__(self):
        self.state = initBoard(8)
        self.pBestScore = 1000000
        self.pBestArr = initBoard(8)
        self.vlast = []
        self.score = 1000000
        self.solved = ""
        for i in range(8):
            self.vlast.append(random.randint(-8,8))
    def isBest(self):
        global gBestScore
        global gBestArr
        if self.score < self.pBestScore:
            self.pBestScore = self.score
            self.pBestArr = self.state
        if self.score < gBestScore:
            gBestScore = self.score
            gBestArr = self.state

    def move(self):
        global gBestScore
        global gBestArr
        w = 0.7
        c1 = 2.5
        c2 = 1.0

        index = 0
        newVel = []
        for i in self.state:
            temp = (w*self.vlast[index]) + (c1*random.random()*(self.pBestArr[index] - i))
            temp = temp + (c2*random.random()*(gBestArr[index]-i))
            index = index + 1
            newVel.append(round(temp))

        index = 0
        newState = []
        for n in self.state:
            n = n+newVel[index]
            if n>7:
                n = 7
            elif n<0:
                n= 0 
            index = index +1
            newState.append(n)
        self.state = newState
        self.vlast = newVel
            
    def checkScore(self):
        global gBestScore
        global gBestArr
        board = self.state
        temp = 0
        for j in range(len(board)):
            for k in range(len(board)):
                if j == k:
                    continue
                if board[j]==board[k]:
                    temp = temp+1
                if abs((board[j] - board[k]) / (j-k))==1:
                    temp = temp+1
        
        self.score = temp
        
        if temp == 0:
            self.solved = True
        else:
            self.solved = False
            self.isBest()



print("#######################################")
print("#######################################")
print("PSO:")
print("#######################################")
print("#######################################")

def checkSwarm(swarm):
    global gBestScore
    global gBestArr
    for i in swarm:
        i.checkScore()
        if i.solved == True:
            return i
    return 0

def moveSwarm(swarm):
    global gBestArr
    for i in swarm:
        i.move()
    

swarm = []
gBestScore = 1000000
gBestArr = initBoard(8)
for i in range(500):
    swarm.append(Particle())

for i in range(1000):
    check = checkSwarm(swarm)
    if check != 0:
        print("took "+str(i)+" iterations")
        break
    moveSwarm(swarm)

print(check.state)

