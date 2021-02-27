from gaus import gaus

def fixresult(cnt, eoutM, answer, a):
    nev = []
    for i in range(cnt):
        nev.append([0])

    win = [0] * cnt

    for i in range(cnt):
        s = 0
        for j in range(cnt):
            x = eoutM[i][j]
            s += x * answer[j]

        nev[i][0] = eoutM[i][cnt] - s

    cnt, popravki, x, xx = gaus(a, nev)

    for i in range(cnt):
        win[i] = answer[i] + popravki[i]

    return win