# Large SUM
import numpy as np
import time

def formatting(link: str):
    f = open(link, "r")
    txt = f.read()
    f.close()
    return np.asarray([int(x) for x in txt.replace("\n", "")])


def LargeSum(link: str):
    arr = np.loadtxt(link)
    print(str(sum(arr))[0:10])
    

# =============================================================================
# Functions
# 
# Program
# =============================================================================

start = time.time()

link = "C:\\Users\\thorb\\Documents\\Project Euler\\Problem_13 Large Sum\\Stort Tall.txt"

LargeSum(link)

tot_time = time.time() - start

print(f'Total tid: {tot_time} sek')