import matplotlib.pyplot as plt
import numpy as np
import it
import newton


def f1(x, y):
    return np.sin(x + 0.445) - 0.813 * y - 1.519


def f2(x, y):
    return x + np.cos(y - 1.078) - 0.144


def f3(x, y):
    return np.cos(x + 0.445) + 0.813 * y - 1.519


def f4(x, y):
    return x + np.sin(y - 1.076) - 0.144

print 'simple iterations'
it.iter()

t = np.linspace(-10, 10)
x, y = np.meshgrid(t, t)
plt.figure()

plt.contour(x, y, f1(x, y), [0], linewidths=3, colors='b')
plt.contour(x, y, f2(x, y), [0], linewidths=3, colors='r')
plt.gcf().set_facecolor('w')
plt.gcf().gca().axis('image')
plt.gcf().gca().grid(True)
plt.show()

t = np.linspace(-10, 10)
x, y = np.meshgrid(t, t)
plt.figure()

print 'Neewton: '
newton.ne(0.25, 0.85)


plt.contour(x, y, f3(x, y), [0], linewidths=3, colors='b')
plt.contour(x, y, f4(x, y), [0], linewidths=3, colors='r')
plt.gcf().set_facecolor('w')
plt.gcf().gca().axis('image')
plt.gcf().gca().grid(True)
plt.show()
