def for_asd(a, b):
    sa = str(a)
    sb = str(b)
    la = len(sa)
    lb = len(sb)
    if la >= lb:
        if la % 2 == 0:
            big = int(la/2)
            for i in range(0, la - lb):
                sb = '0' + sb
            a1 = int(sa[0:big])
            a0 = int(sa[big:])
            b1 = int(sb[0:big])
            b0 = int(sb[big:])
            c2 = for_asd(a1, b1)
            c0 = for_asd(a0, b0)
            c1 = (a1 + a0) * (b1 + b0) - c2 - c0
            fin = c2 * 10**(big*2) + c1 * 10 ** big + c0
        else:
            fin = a * b
    else:
        if lb % 2 == 0:
            big = int(lb / 2)
            for i in range(0, lb - la):
                sa = '0' + sa
            a1 = int(sa[0:big])
            a0 = int(sa[big:])
            b1 = int(sb[0:big])
            b0 = int(sb[big:])
            c2 = for_asd(a1, b1)
            c0 = for_asd(a0, b0)
            c1 = (a1 + a0) * (b1 + b0) - c2 - c0
            fin = c2 * 10 ** (big * 2) + c1 * 10 ** big + c0
        else:
            fin = a * b
    return fin


print(for_asd(14456465464654, 45343643644))