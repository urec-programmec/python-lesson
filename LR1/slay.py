from gaus import gaus
from pcontrol import pcontrol
from fixresult import fixresult

def slay(a, b, e):
    cnt, answer, outM, eoutM = gaus(a, b)
    res = pcontrol(cnt, answer, eoutM, e)

    while res != 1:
        answer = fixresult(cnt, eoutM, answer, a)
        res = pcontrol(cnt, answer, eoutM, e)

    return answer
