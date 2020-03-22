import math


def kaibun_check(texts):
    n = len(texts)
    if texts == texts[::-1]:
        return True
    return False


def main():
    S = list(input())
    N = len(S)
    if not kaibun_check(S):
        print("No")
        return
    if not kaibun_check(S[0:(N - 1) // 2]):
        print("No")
        return
    if not kaibun_check(S[math.ceil((N + 3) / 2) - 1:]):
        print("No")
        return
    print("Yes")
    return


main()
