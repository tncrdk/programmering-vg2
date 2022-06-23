import numpy as np
import time

def DiagonalLeft(grid, N):
    n = N - 1 #Skal brukes når vi looper gjennom rader og kolonner
    Sum = 0
    for row in range(len(grid) - n): #Hver rad vi skal gå gjennom som base
     
        for col in range(n, len(grid)): #Hver kolonno i den raden vi har valgt som base
            y = row
            x = col
            TempSum = 1
            
            for dia in range(N): #Finne diagonalene
                TempSum *= grid[y, x]
                y += 1 #Rad
                x -= 1 #Kolonne
            
            if TempSum > Sum:
                Sum = TempSum
    return Sum


def DiagonalRight(grid, N):
    n = N - 1 #Skal brukes når vi looper gjennom rader og kolonner
    Sum = 0
    for row in range(len(grid) - n): #Hver rad vi skal gå gjennom som base
     
        for col in range(len(grid) - n): #Hver kolonno i den raden vi har valgt som base
            y = row
            x = col
            TempSum = 1
            
            for dia in range(N): #Finne diagonalene
                TempSum *= grid[y, x]
                y += 1 #Rad
                x += 1 #Kolonne
            
            if TempSum > Sum:
                Sum = TempSum
    return Sum


def Horizontally(grid, N):
    n = N - 1
    Sum = 0
    for row in range(len(grid)): #Hver rad vi skal gå gjennom som base
        
        for col in range(len(grid) - n): #Hver kolonno i den raden vi har valgt som base
            TempSum = 1
            y = row
            x = col
            
            for hor in range(N): #Finne riktig antall tall fra basen
                TempSum *= grid[y, x]
                x += 1
            
            if TempSum > Sum:
                Sum = TempSum
    return Sum


def Vertically(grid, N):
    n = N - 1
    Sum = 0
    for col in range(len(grid)): #Hver kolonne vi skal gå gjennom som base
        
        for row in range(len(grid) - n): #Hver rad i den raden vi har valgt som base
            TempSum = 1
            y = row
            x = col
            
            for ver in range(N): #Finne riktig antall tall fra basen
                TempSum *= grid[y, x]
                y += 1
            
            if TempSum > Sum:
                Sum = TempSum
    return Sum


def ReshapeArr(arr):
    return arr.reshape(int((len(arr))**(1/2)), int((len(arr))**(1/2)))


def Formatting(link: str):
    f = open(link, "r")
    txt = f.read()
    f.close()
    grid = list(map(int, txt.split()))
    return ReshapeArr(np.asarray(grid, dtype="int64"))


def Biggest_Product(link: str, N):
    # grid = np.loadtxt(link)
    grid = Formatting(link)
    
    TotSum = Horizontally(grid, N)
    
    if TotSum < Vertically(grid, N):
        TotSum = Vertically(grid, N)
    
    if TotSum < DiagonalLeft(grid, N):
        TotSum = DiagonalLeft(grid, N)
    
    if TotSum < DiagonalRight(grid, N):
        TotSum = DiagonalRight(grid, N)
    
    print(TotSum)
    

# =============================================================================
# Above: Functions
# Under: The Program
# =============================================================================

link = 'C:\\Users\\thorb\\Documents\\Project Euler\\Grid\\Tall.txt'

NumFac = 4

start = time.time()

Biggest_Product(link, NumFac)

tot_time = time.time() - start
print(f'Time: {tot_time}sek')




