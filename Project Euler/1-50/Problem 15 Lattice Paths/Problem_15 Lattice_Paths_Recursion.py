import numpy as np
import time

x = 0 #x-axis ----- if x = len(grid) --> only one option
y = 0 #y-axis ----- if y = len(grid) --> only one option

# =============================================================================
# Need to store number of options from each point for future reference.
# =============================================================================

def Lattice(grid, x = 0, y = 0):
    
    if grid[y, x] != 0:
        return grid[y, x]
    
    elif x == len(grid) - 1 or y == len(grid) - 1:
        grid[y, x] = 1
        return 1
    
    else:
        options = Lattice(grid, x + 1, y) + Lattice(grid, x, y + 1)
        grid[y, x] = options
        return options    

# =============================================================================
# Program
# =============================================================================

N = int(input("Hvor mange ruter? ")) + 1

start = time.time()
   
grid = np.zeros((N, N))

print(Lattice(grid))

Tot_time = time.time() - start
print(f'Total tid: {Tot_time} sek')