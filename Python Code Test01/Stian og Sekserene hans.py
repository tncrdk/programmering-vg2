# -*- coding: utf-8 -*-
from pylab import *

 

antallKast = 6000
print("Antall kast = ",antallKast)

 

# array med resultat fra hvert kast, y-verdi
terning = zeros(antallKast + 1)

 

# array med x-verdier
x = linspace(1, antallKast, antallKast + 1)

 

# Antall 6ere / totalt antall kast
relFrek = zeros(antallKast+1)

 

antall6ere = 0

 

for i in range(1, antallKast+1):
    terning[i] = randint(1,7)
    # hvis 6, tell opp antall 6ere
    if terning[i] == 6:
        antall6ere = antall6ere + 1
    
    relFrek[i] = antall6ere / i
    
# Lager graf
title("Simulering av terningkast")
plot(x, relFrek)
xlabel("Antall kast")
ylabel("Relativ frekvens") 

show()

