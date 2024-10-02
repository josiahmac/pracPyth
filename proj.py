import random

theGrid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def displayTheGrid():
    for i in theGrid:
        print(i)
    
def init2048():
    theGrid[random.randint(0,3)][random.randint(0,3)] = 2
    theGrid[random.randint(0,3)][random.randint(0,3)] = 2
    displayTheGrid()

init2048()

