import matplotlib.pyplot as plt

line_blue = plt.plot([1, 5, -3, -0.5], [1, 25, 9, 0.25], label='Синяя линия')
line_red = plt.plot([-6, -5, 0, 8], [-5, -2, -3, 4])

plt.setp(line_blue, color='blue', linewidth=2, marker='v')
plt.setp(line_red, color='red', linewidth=2, marker='o', label='Красная линия')

plt.legend()
plt.title('Пример построения')

plt.show()
