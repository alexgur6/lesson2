import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3*np.pi, 3*np.pi, 250)
y = np.sin(x) + np.random.normal(loc=0.1, scale=0.3, size=250)

plt.figure(figsize=(10, 5))
plt.scatter(x, y)



plt.scatter(x, y,
 s=300,
 marker='s',
 c='violet',
 lw=2,
 edgecolor='black',
 hatch='**'
 )

plt.title(
 label='$sin(x)$ with random noise', # Заголовок
 fontsize=20 # Размер шрифта
)
plt.xlabel('Ось x', fontsize=18)
plt.ylabel('Ось y', fontsize=18)
plt.tick_params(labelsize = 16)

plt.xticks(
 ticks=np.arange(-10, 11, 2) # Нужные значения по оси x
)
plt.yticks(
 ticks=np.arange(-1.5, 2, 0.5)
)

plt.show()