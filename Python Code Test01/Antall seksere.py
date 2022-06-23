from pylab import *

gjennomsnitt = 0
for j in range(1000):
    Antall6 = 0
    for i in range(600):
        number = 6
        random = randint(1,7)
        if number == random:
            Antall6 = Antall6 + 1
    gjennomsnitt = (gjennomsnitt + Antall6)
print(gjennomsnitt/1000/600)
