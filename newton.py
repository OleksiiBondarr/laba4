import numpy
import sympy
e = 0.00001


def f3(x, y):
    return sympy.cos(x + 0.445) + 0.813 * y - 1.519


def f4(x, y):
    return x + sympy.sin(y - 1.076) - 0.144


def df3x(c1, c2):
    x = sympy.Symbol('x')
    y = sympy.Symbol('y')
    r = sympy.diff(f3(x, y), x)
    return r.evalf(subs={x: c1, y: c2})


def df3y(c1, c2):
    x = sympy.Symbol('x')
    y = sympy.Symbol('y')
    r = sympy.diff(f3(x, y), y)
    return r.evalf(subs={x: c1, y: c2})


def df4x(c1, c2):
    x = sympy.Symbol('x')
    y = sympy.Symbol('y')
    r = sympy.diff(f4(x, y), x)
    return r.evalf(subs={x: c1, y: c2})


def df4y(c1, c2):
    x = sympy.Symbol('x')
    y = sympy.Symbol('y')
    r = sympy.diff(f4(x, y), y)
    return r.evalf(subs={x: c1, y: c2})


def obr(fu):
    det = fu[0, 0]*fu[1, 1] - fu[0, 1]*fu[1, 0]
    aa = fu[0, 0]
    fu[0, 0] = fu[1, 1]/det
    fu[1, 1] = aa/det
    aa = fu[0, 1]
    fu[1, 0] = -fu[1, 0]/det
    fu[0, 1] = -aa/det
    return fu


def ne(r1, r2):
    func = numpy.array([[df3x(r1, r2), df3y(r1, r2)],
                        [df4x(r1, r2), df4y(r1, r2)]])

    func1 = obr(func)
    func = func1
    resh = numpy.zeros(2)
    nach = numpy.array([1., 1.])
    nach1 = numpy.array([r1, r2])
    norm = norm1 = 1.
    count = 0
    while norm >= e or norm1 >= e:
        nach[0] = nach1[0]
        nach[1] = nach1[1]

        resh[0] = f3(nach[0], nach[1])
        resh[1] = f4(nach[0], nach[1])
        func = numpy.array([[df3x(nach[0], nach[1]), df3y(nach[0], nach[1])],
                            [df4x(nach[0], nach[1]), df4y(nach[0], nach[1])]])
        func1 = obr(func)
        func = func1
        d = numpy.dot(func, resh)

        nach1[0] = -d[0] + nach[0]
        nach1[1] = -d[1] + nach[1]
        norm = numpy.linalg.norm(resh)
        re2 = nach1 - nach
        norm1 = sympy.sqrt(re2[0]**2 + re2[1]**2)

        count += 1
        print 'iter ' + str(count) + ' x:' + str(nach[0]) + ' y:' + str(nach[1]) + ' norma:' + str(norm1) + ' norma2:' + str(norm) + '\n'
    print 'result: x:' + str(nach[0]) + ' y:' + str(nach[1]) + '\n\n'
    return count
