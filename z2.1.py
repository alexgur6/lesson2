import numpy as np
import matplotlib.pyplot as plt

# Создание массива x на интервале от -10 до 10 с 1000 точками
x = np.linspace(-10, 10, 1000)

# Вычисление значений функции y(x)
y = (np.sin(2 * x) ** 2 * np.exp((x + 2) / 10) ** 2)

# Размер экрана
plt.figure(figsize=(8, 3))

# Построение графика функции
plt.plot(x, y, lw=4.0, color='red')

# Добавление сетки с толщиной 0.5 и стилем пунктир
plt.grid(lw=0.5, ls='--')


plt.plot(x, y, lw=5.0, color='black', zorder=0)

# Отображение графика
plt.plot(x, y)
plt.show()
