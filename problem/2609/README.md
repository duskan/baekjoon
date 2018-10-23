# 2609 최대공약수, 최소공배수

  * 기본적으로 최대공약수는 소인수 분해를 이용해서 계산
  * 하지만 유클리디안 호제법을 이용하면 간단히 구할 수 있음

```
import sys


def gcd(a, b):
    # 유클리드 호제법
    while (b != 0):
        r = a % b
        a = b
        b = r
    return int(a)


def lcm(a, b):
    # 최대공약수 * 최소공배수 == a * b
    return int(a * b / gcd(a, b))


if __name__ == "__main__":
    # 입력
    line = sys.stdin.readline()
    mlist = line.split()
    A = int(mlist[0])
    B = int(mlist[1])

    # 결과 출력
    print(gcd(A, B))
    print(lcm(A, B))
```

### 추가사항
직접 소인수 분해를 이용해서도 구해 봄

  * 알고리즘:
    1. 입력한 a, b 숫자를 각각 소인수 분해
    2. 다음의 방법으로 최대공약수 최소공배수 계산
      * 최대공약수 : a, b 의 약수들 중 공약수들만 찾아서 곱함 (즉, a, b의 약수들이 집합이면 교집합을 구하면됨)
      * 최소공배수 : a, b 의 약수들을 전부 곱함, 단 공약수는 한번만 곱하면됨 (즉, a, b의 약수들이 집합이면 합집합을 구하면됨)
  * 주의사항: 합집합, 교집합으로 이야기했으나, 중복이 허용되는 리스트임

```
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
```
