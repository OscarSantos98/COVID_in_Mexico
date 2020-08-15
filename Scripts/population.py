import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm

plt.style.use('seaborn')

os.chdir('..')
os.chdir('data')
df = pd.read_csv('Casos_Diarios_Estado_Nacional_Confirmados_20200812.csv')

population = df['poblacion'].iloc[:-1]
state = df['nombre'].iloc[:-1]

for i in range(0,len(state)):
    if i % 2 == 0:
        plt.barh(state[i],population[i],color=cm.tab20b(1.*i/len(state)))
    else:
        plt.barh(state[i],population[i],color=cm.tab20(1.*i/len(state)))

plt.title('Population of México')
plt.xlabel('Population')
plt.tight_layout()
plt.show()