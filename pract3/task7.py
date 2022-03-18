import matplotlib.pyplot as plt
import random

xs = range(0, 10)
# Символ ; здесь используется, чтобы не выводить служебную информацию на экран
plt.plot(xs, [random.random() for _ in xs]);
plt.plot(xs, [random.random() for _ in xs], label='$f_1$') # Нотация LaTeX
plt.plot(xs, [2 * random.random() for _ in xs], label='$f_2$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График')
plt.legend();
'''
colors = [random.choice(['red', 'blue']) for _ in xs]
fig, axs = plt.subplots(2, 2, figsize=(15, 5))
axs[0, 0].plot([random.random() for _ in xs])
axs[0, 1].scatter([random.random() for _ in xs], [random.random() for _ in xs], c=colors)
axs[1, 0].bar(xs, [random.random() for _ in xs])
axs[1, 1].imshow([[random.random() for _ in xs] for _ in xs]);
'''