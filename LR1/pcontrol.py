def pcontrol(cnt, answer, eoutM, err):
    two = [0] * cnt
    two[cnt - 1] = eoutM[cnt - 1][cnt + 1]

    for j in range(1, cnt):
        s = 0
        for k in range(0, j):
            s += eoutM[cnt - j - 1][cnt - k - 1] * two[cnt - k - 1]
        if (eoutM[cnt - j - 1][cnt - j - 1] != 0):
            two[cnt - j - 1] = (eoutM[cnt - j - 1][cnt + 1] - s) / eoutM[cnt - j - 1][cnt - j - 1]

    result = 0
    for i in range(cnt):
        if (err ** 2 >= (two[i] - 1 - answer[i]) ** 2):
            result += 1

    if result == cnt:
        res = 1
    else:
        res = 0

    return res
