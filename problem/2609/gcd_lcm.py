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
    print(gcd(A, B))
    print(lcm(A, B))
