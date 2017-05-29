import numpy
e = 0.00001


def f1(x, y):
    return numpy.sin(x + 0.445) - 0.813 * y - 1.519


def f2(x, y):
    return x + numpy.cos(y - 1.078) - 0.144


def l(x, y):
    h = -numpy.cos(y - 1.078) + 0.144
    g = (-1.519 + numpy.sin(x + 0.445)) / 0.813
    return h, g


def iter():
    nach1 = numpy.array([0.5, -0.85])
    nach = numpy.array([0.5, -0.85])
    resh = numpy.zeros(2)
    norm = norm1 = 1.
    count = 0
    while norm > e or norm1 > e:
        nach[0] = nach1[0]
        nach[1] = nach1[1]
        nach1[0], nach1[1] = l(nach[0], nach[1])
        resh[0] = f1(nach[0], nach[1])
        resh[1] = f2(nach[0], nach[1])
        norm = numpy.linalg.norm(resh)
        norm1 = numpy.linalg.norm(nach1 - nach)
        count += 1
        print 'iter ' + str(count) + ' x:' + str(nach[0]) + ' y:' + str(nach[1]) + ' norma:' + str(norm1) + ' norma2:' + str(norm) + '\n'
    print 'result: x:' + str(nach[0]) + 'y:' + str(nach[1]) + '\n\n'
    return resh
