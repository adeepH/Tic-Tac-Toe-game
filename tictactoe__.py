# -*- coding: utf-8 -*-
"""TicTacToe_ .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gSjqT0jucV8ObzpHPoyA3BCv0ZZ17rFw
"""

import random 
import numpy as np
import keras
from keras.models import  Sequential
from keras.layers import Dense,Dropout
from keras.backend import reshape
from keras.utils.np_utils import to_categorical

#Let us use an empty board
# 0 indicates empty spaces
# 1 indicates an 'X' (player1)
# 2 indicates a 'O' (player 2)

#Since the board is empty we initialise it with zeros 
def initBoard():
  board = [
           [0,0,0],
           [0,0,0],
           [0,0,0]
  ]
  return board

#print the current state of the board
def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            mark = ' '
            if board[i][j] == 1:
                mark = 'X'
            elif board[i][j] == 2:
                mark = 'O'
            if (j == len(board[i]) - 1):
                print(mark)
            else:
                print(str(mark) + "|", end='')
        if (i < len(board) - 1):
            print("-----")

#Get a list of valid Moves(indices into the word)
def getMoves(board):
  moves = []
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == 0:
        moves.append((i,j))
  
  return moves

#Declaring a winner
# (-1) = Game not over
# 0 = Draw
# 1 = 'X' wins (player 1)
# 2 = 'O' wins (player 2)

def getWinner(board):
  candidate = 0
  won = 0

  #check Rows
  for i in range(len(board)):
    candidate = 0
    for j in range(len(board[i])):

      #To make sure there are no gaps
      if board[i][j] == 0:
        break
      
      #identifying any frontrunner 
      if candidate == 0:
        candidate = board[i][j]
      #Determine whether the front-runner has all the slots
      if candidate != board[i][j]:
        break
      elif j == len(board[i]) - 1:
        won = candidate
    
  if won > 0 :
    return won
    
  #check Columns 
  for j in range(len(board[0])):
    candidate = 0
    for i in range(len(board)):

      # To make sure there are no gaps
      if board[i][j] == 0:
        break
      
      #Identify the front-runner
      if candidate == 0:
        candidate = board[i][j]
      #Determine whether the front-runner has all the slots
      if candidate != board[i][j]:
        break
      elif i == len(board) - 1:
        won = candidate
  if won > 0 :
    return won
  
  #Check Diagonals
  candidate = 0 
  for i in range(len(board)):
    if board[i][i] == 0:
      break
    if candidate == 0:
      candidate = board[i][i]
    if candidate != board[i][i]:
      break
    elif i == len(board) - 1:
      won = candidate
  if won > 0:
    return won
  
  candidate = 0
  for i in range(len(board)):
    if board[2-i][2-i] == 0:
      break
    if candidate == 0:
      candidate = board[2-i][2-i]
    if candidate != board[2-i][2-i]:
      break
    elif i == len(board) -1:
      won = candidate
  
  if won > 0:
    return won
  

  #if still there is no winner
  if len(getMoves(board)) == 0:
    #Its a draw
    return 0
  else:
    #if there are more moves to make
    return -1

"""*` we Test the helper method to demonstrate that they work`*"""

#Test helper methods

b  = initBoard()
printBoard(b)
print(getWinner(b))
print(getMoves(b))

b[0][0] = 1
b[1][1] = 1
b[2][2] = 1
printBoard(b)
print(getWinner(b))

b[0][2] = 2
b[1][2] = 2
b[2][2] = 2
printBoard(b)
print(getWinner(b))

"""
for i in range(2):  
  for j in range(2):
    b[i][j]"""

b[0][1] = 1
b[1][0] = 2
b[2][0] = 1
b[2][1] = 2
b[2][2] = 1
b[0][0] = 2
printBoard(b)
print(getWinner(b))

"""*`create a random game simulator`*"""

random.seed()

#Get the best next move for the given player at the given board position
def bestMove(board, model, player, rnd=0):
    scores = []
    moves = getMoves(board)
    
    # Make predictions for each possible move
    for i in range(len(moves)):
        future = np.array(board)
        future[moves[i][0]][moves[i][1]] = player
        prediction = model.predict(future.reshape((-1, 9)))[0]
        if player == 1:
            winPrediction = prediction[1]
            lossPrediction = prediction[2]
        else:
            winPrediction = prediction[2]
            lossPrediction = prediction[1]
        drawPrediction = prediction[0]
        if winPrediction - lossPrediction > 0:
            scores.append(winPrediction - lossPrediction)
        else:
            scores.append(drawPrediction - lossPrediction)

    # Choose the best move with a random factor
    bestMoves = np.flip(np.argsort(scores))
    for i in range(len(bestMoves)):
        if random.random() * rnd < 0.5:
            return moves[bestMoves[i]]

    # Choose a move completely at random
    return moves[random.randint(0, len(moves) - 1)]

#Simulate the game
def SimulateGame(p1=None,p2=None,rnd=0):
  history = []
  board = initBoard()
  playerToMove = 1
  #while there are still moves to make 
  while getWinner(board) == -1:
    #choose a move at random or use a player model if provided
    move = None
    if playerToMove == 1 and p1 != None:
      move = bestMove(board,p1,playerToMove,rnd)
    elif playerToMove == 2 and p2 != None:
      move = bestMove(board,p2,playerToMove,rnd)
    else:
      moves = getMoves(board)
      move = moves[random.randint(0,len(moves)-1)]
    
    #Make the move
    board[move[0]][move[1]] = playerToMove

    #Add the movie to history
    history.append((playerToMove,move))

    #Switch to anotner player after one move
    playerToMove = 1 if playerToMove == 2 else 2
  
  return history

#Simulate the game
history = SimulateGame()
print(history)

#Reconstruct the board from the move list 

def movesToBoard(moves):
  board = initBoard()
  for move in moves:
    player = move[0]
    coords = move[1]
    board[coords[0]][coords[1]] = player
  return board

board = movesToBoard(history)
printBoard(board)
print(getWinner(board))

"""We now generate a set of simulated games to train our neural network and calculate some win statistics for each random player. We predict that 'X'(player1) should have a slightly bigger advantage as it starts first"""

games = [SimulateGame() for _ in range(10000)]

#Aggregate win/loss/draw stas for players

def gameStats(games,player=1):
  stats = {"Win": 0,"Loss": 0, "Draw": 0}
  for game in games:
    result = getWinner(movesToBoard(game))
    if result == -1:
      continue
    elif result == player:
      stats["Win"] += 1
    elif result == 0:
      stats["Draw"] += 1
    else:
      stats["Loss"] += 1
  #Let us define the win ,draw and loss percentages
  WinPct = stats["Win"]/len(games) * 100
  LossPct = stats["Loss"]/len(games) * 100
  DrawPct = stats["Draw"]/len(games) * 100


  print("Results for player %d:" % (player))
  print("Wins: %d (%.1f%%)" % (stats["Win"], WinPct))
  print("Loss: %d (%.1f%%)" % (stats["Loss"], LossPct))
  print("Draw: %d (%.1f%%)" % (stats["Draw"], DrawPct))

gameStats(games)
print()
gameStats(games,player=2)

"""Let us define the model
`input_shape = (9,)`
`output = 3`
"""

def getModel():
  numCells = 9 #number of cells in a 3x3 grid
  outcomes = 3 #Win , Loss, Draw
  model = Sequential()
  model.add(Dense(400,activation='relu',input_shape = (9,)))
  model.add(Dropout(0.3))
  model.add(Dense(250,activation='relu'))
  model.add(Dense(125,activation='relu'))
  model.add(Dropout(0.3))
  model.add(Dense(75,activation='relu'))
  model.add(Dense(outcomes,activation='softmax'))
  model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])
  return model

model = getModel()
print(model.summary())

"""Let us preprocess the data in order to train the model"""

#Reshape our data to train
#Get a set of board states labelled by who eventually won that game

def gamesToWinLossData(games):
    X = []
    y = []
    for game in games:
        winner = getWinner(movesToBoard(game))
        for move in range(len(game)):
            X.append(movesToBoard(game[:(move + 1)]))
            y.append(winner)

    X = np.array(X).reshape((-1, 9))
    y = to_categorical(y)
    
    # Return an appropriate train/test split
    trainNum = int(len(X) * 0.8)
    return (X[:trainNum], X[trainNum:], y[:trainNum], y[trainNum:])

# Split out train and validation data
X_train, X_test, y_train, y_test = gamesToWinLossData(games)

epochs = 100
batchsize = 100
history = model.fit(X_train,y_train,validation_data=(X_test,y_test),epochs=epochs,batch_size=batchsize)

games2 = [SimulateGame(p1=model) for _ in range (1000)]

gameStats(games2)

games3 = [SimulateGame(p2=model) for _ in range (1000)]
gameStats(games3,player=2)

games4 = [SimulateGame(p1=model, p2=model, rnd=0.6) for _ in range(1000)]

gameStats(games4, player=1)
print()
gameStats(games4, player=2)

print("Average length of fully random game is %f moves" % (np.mean([float(len(game)) for game in games])))
print("Average length of game where P1 uses NN is %f moves" % (np.mean([float(len(game)) for game in games2])))
print("Average length of game where P2 uses NN is %f moves" % (np.mean([float(len(game)) for game in games3])))
print("Average length of game where both use NN is %f moves" % (np.mean([float(len(game)) for game in games4])))

"""`Lets play a game against our agent`"""

#Create a new board
board = initBoard()

#Move 1 (computer)
move = bestMove(board,model,1)
board[move[0]][move[1]] = 1
printBoard(board)

#Move 2(human)
board[1][1] = 2
printBoard(board)

#Move 3 (computer)
move = bestMove(board,model,1)
board[move[0]][move[1]] = 1
printBoard(board)

#Move 4(human)
board[0][1] = 2
printBoard(board)

#Move 5 (computer)
move = bestMove(board,model,1)
board[move[0]][move[1]] = 1
printBoard(board)

#Move 6(human)
board[1][2] = 2
printBoard(board)

#Move 7 (computer)
move = bestMove(board,model,1)
board[move[0]][move[1]] = 1
printBoard(board)

#Move 8(human)
board[2][0] = 2
printBoard(board)

#Move 9 (computer)
move = bestMove(board,model,1)
board[move[0]][move[1]] = 1
printBoard(board)

#Move 8(human)
board[2][2] = 2
printBoard(board)

