import matplotlib.pyplot as plt
import random
'''
xs = range(0, 10)
# Символ ; здесь используется, чтобы не выводить служебную информацию на экран
plt.plot(xs, [random.random() for _ in xs]);
plt.plot(xs, [random.random() for _ in xs], label='$f_1$') # Нотация LaTeX
plt.plot(xs, [2 * random.random() for _ in xs], label='$f_2$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График')
plt.legend();
plt.show()

colors = [random.choice(['red', 'blue']) for _ in xs]
fig, axs = plt.subplots(2, 2, figsize=(15, 5))
axs[0, 0].plot([random.random() for _ in xs])
axs[0, 1].scatter([random.random() for _ in xs], [random.random() for _ in xs], c=colors)
axs[1, 0].bar(xs, [random.random() for _ in xs])
axs[1, 1].imshow([[random.random() for _ in xs] for _ in xs]);
'''
def mas_sv(digit):
    a = [[0 for i in range(5)]for j in range(5)]
    for i in range(5):
        for j in range(3):
            a[i][j] = random.randint(0, digit)
            if j != 2:
                a[i][4-j] = a[i][j]
    #print(a)
    return a

def mas_sc(digit):
    a = [[0 for i in range(5)]for j in range(5)]
    for i in range(3):
        for j in range(3):
            a[i][j] = random.randint(0, digit)
            a[i][4-j] = a[i][j]
            a[4-i][j] = a[i][j]
            a[4-i][4-j] = a[i][j]

    #print(a)
    return a

if __name__ == "__main__":
    fig, axs = plt.subplots(20, 20, figsize=(10, 10))

    for i in range(20):
        for j in range(20):
            if i < 10 and j < 10:
                axs[i][j].imshow(mas_sv(1), cmap='gray', interpolation='nearest')
            elif i >= 10 and j >= 10:
                axs[i][j].imshow(mas_sc(1), cmap='gray', interpolation='nearest')
            elif i < 10 and j >= 10:
                axs[i][j].imshow(mas_sv(5), cmap='autumn', interpolation='nearest')
            elif i >= 10 and j < 10:
                axs[i][j].imshow(mas_sc(5), cmap='winter', interpolation='nearest')
            axs[i][j].axis('off')

    plt.show()