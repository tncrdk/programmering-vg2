
def Formatting(link):
    with open(link) as f:
        txt = f.read().split("\n")
    
    arr = [[int(x) for x in i.split()] for i in txt]
    
    return arr



# =============================================================================
# Functions
# Execution
# =============================================================================

link = "C:\\Users\\thorb\\Documents\\Project Euler\\Problem 18\\Triangle.txt"

Formatting(link)