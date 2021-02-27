def gaus(a, b):

    outM = []

    for i in range(len(a)):
        outM.append([])
        for j in range(len(a[0])):
            outM[i].append(a[i][j])

    for i in range(len(outM)):
        outM[i].append(b[i][0])

    cnt = len(b)

    tempC = [0] * cnt

    for i in range(cnt):
        for j in range(cnt + 1):
            tempC[i] += outM[i][j]

    eoutM = []

    for i in range(len(outM)):
        eoutM.append([])
        for j in range(len(outM[0])):
            eoutM[i].append(outM[i][j])


    for i in range(cnt):
        eoutM[i].append(tempC[i])

    for i in range(cnt):
        prevK = eoutM[i][i]
        for j in range(cnt + 2):
            if(prevK != 0):
                eoutM[i][j] /= prevK
        for j in range(i + 1, cnt):
            prevK = eoutM[j][i]
            for jj in range(i, cnt + 2):
                eoutM[j][jj] -= prevK * eoutM[i][jj]

    answer = [0] * cnt
    answer[cnt - 1] = eoutM[cnt - 1][cnt]

    for j in range(1, cnt):
        s = 0
        for k in range(0, j):
            s += eoutM[cnt - j - 1][cnt - k - 1] * answer[cnt - k - 1]
        if(eoutM[cnt - j - 1][cnt - j - 1] != 0):
            answer[cnt - j - 1] = (eoutM[cnt - j - 1][cnt] - s) / eoutM[cnt - j - 1][cnt - j - 1]

    return [cnt, answer, outM, eoutM]

