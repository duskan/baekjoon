import sys


def run_hanoi(N, a, b, c):
    # a = 1, b = 2, c = 3

    if N == 0:  # 재귀가 종료되는 시점이 있어야 한다.
        return

    run_hanoi(N-1, a, c, b)
    print(a, c)
    run_hanoi(N-1, b, a, c)


def count_hanoi(N):
    return int(pow(2, N) - 1)


if __name__ == "__main__":
    # input
    line = sys.stdin.readline()
    num_of_block = int(line)

    result = count_hanoi(num_of_block)
    print(result)

    if num_of_block <= 20:
        run_hanoi(num_of_block, 1, 2, 3)
