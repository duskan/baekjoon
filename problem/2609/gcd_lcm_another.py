import sys


# 또 다른 방법
# 직접 소인수 분해를 해서 계산 할 수도 있다.
def fractional_decomposition(a):
    # 소인수 분해
    res = []
    mod = 2
    v = a

    while v != 1:
        if mod > v:
            print(res)
            raise RuntimeError("Cannot escape this while expression")

        remainder = v % mod
        if remainder != 0:
            mod += 1
            continue
        else:
            v = v / mod
            res.append(mod)

    return res


def gcd_2(a, b):
    a_list = fractional_decomposition(a)
    b_list = fractional_decomposition(b)

    i = 0
    j = 0

    res_list = []

    while True:
        # check index
        if i >= len(a_list):
            break
        if j >= len(b_list):
            break

        v1 = a_list[i]
        v2 = b_list[j]

        if v1 == v2:
            res_list.append(v1)
            i += 1
            j += 1
        elif v1 > v2:
            j += 1
        elif v1 < v2:
            i += 1

    res = 1
    for v in res_list:
        res *= v

    return res


def lcm_2(a, b):
    a_list = fractional_decomposition(a)
    b_list = fractional_decomposition(b)

    i = 0
    j = 0

    res_list = []

    while True:
        # check index
        if i >= len(a_list):
            if j < len(b_list):
                res_list += b_list[j:]
            break
        if j >= len(b_list):
            if i < len(a_list):
                res_list += a_list[i:]
            break

        v1 = a_list[i]
        v2 = b_list[j]

        if v1 == v2:
            res_list.append(v1)
            i += 1
            j += 1
        elif v1 > v2:
            res_list.append(v2)
            j += 1
        elif v1 < v2:
            res_list.append(v1)
            i += 1

    res = 1
    for v in res_list:
        res *= v

    return res


if __name__ == "__main__":
    # 입력
    line = sys.stdin.readline()
    mlist = line.split()
    A = int(mlist[0])
    B = int(mlist[1])
    # print(gcd(A, B))
    # print(lcm(A, B))

    print(gcd_2(A, B))
    print(lcm_2(A, B))
