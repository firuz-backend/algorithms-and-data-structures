

def quadratic(x1, x2):
    b = -(x1 + x2)
    c = x1 * x2

    res = 'x^2'
    if b < 0:
        if b == -1:
            res = f'{res} - x'
        else:
            res = f'{res} - {b * -1}x'
    elif b == 1:
        res = f'{res} + x'
    elif b == 0:
        res = res
    else:
        res = f'{res} + {b}x'

    if c == 0:
        res = f'{res} = 0'
    else:
        c = f'+ {c}' if c > 0 else f'- {c * -1}'
        res = f'{res} {c} = 0'

    return res
