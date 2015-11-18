import matplotlib.pyplot as plt
import numpy as np


###opdracht1
##plt.plot([1,2,4,9,16,25,36,1])
##plt.show()

###opdracht 2+3
##plt.plot([7,8,9,10,11,12,13,14,15,16,17,18],[10, 10, 10, 30, 20, 25, 30, 35, 70, 75, 80, 10],label='Belasting')
##plt.axis([7,18,0,100])
##plt.title('Processorbelasting')
##plt.xlabel('Uren')
##plt.ylabel('Belasting (uitgedruikt in gemiddeld % per uur)')
##plt.legend(loc='upper left')
##plt.annotate('Wat gebeurt hier?!', xy=(17,80), xytext=(15,90),arrowprops=dict(facecolor='black'))
##plt.grid(True)
##plt.show()

plt.plot([2011,2012,2013,2014,2015], [35.15,50.4,55.55,55.02,53.21], label='Win7')
plt.plot([2011,2012,2013,2014,2015], [43.63,30.47,22.53,15.73,10.51], label='WinXP')
plt.plot([2011,2012,2013,2014,2015], [6.6,7.47,7.67,8.73,9.29], label='OSx')
plt.plot([2011,2012,2013,2014,2015], [12.36,8.43,5.85,3.42,2.18], label='WinVista')
plt.plot([2013,2014,2015], [0.3,7.4,15.03],label='Win8.1')
plt.plot([2012,2013,2014,2015], [0.36,6.12,7.11,3.75],label='Win8')
plt.plot([2011,2012,2013,2014,2015], [0.79,0.85,1.1,1.33,1.64],label='Linux')
plt.axis([2011,2015,0,60])
plt.title('Top 7 besturingssystemen 2011-2015')
plt.xlabel('Jaartal')
plt.ylabel('Populairiteit (in procenten)')
plt.legend(loc='upper right')
plt.show()