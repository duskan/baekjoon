# 2455 (지능형 기차)

이 문제는 아주 간단한 더하고 빼면 되는 문제로, 역의 수도 4개로 고정이라 다음과 같이
간단하게 문제를 해결 할 수 있다.

```
import sys

if __name__ == "__main__":

    LIMIT_PEOPLE = 10000
    max_people = 0

    train_people = 0

    for i in range(4):
        row = sys.stdin.readline().strip().split()
        train_out = int(row[0])
        train_in = int(row[1])

        # check input
        if train_people < train_out :
            print("ERROR")
            exit()

        train_people -= train_out
        train_people += train_in

        if train_people > LIMIT_PEOPLE:
            train_people == LIMIT_PEOPLE

        if train_people > max_people:
            max_people = train_people

    print(max_people)

```
