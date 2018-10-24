# 하노이 탑

이 문제는  Stack(Recursive call)과 DP 두개 다 사용해야하는 문제이다.

## 하노이 탑 (DP문제, 재귀함수)

1 개일떄는 당연히 이동횟수가 1이다. 2개 일때 이동횟수를 구해보자.
```
1                                               1
2         ->  2  1      ->     1  2  ->         2        
a  b  c       a  b  c       a  b  c       a  b  c      
```

그림을 올리기 힘들어 ~~(귀찮아서)~~ 텍스트로 대채하였다.
~~(근데 밑에까지 다쓰고보니 이게 훨 귀찮은거같다.)~~

총 이동횟수는 위에서 보이는것과 같이 총 3회이다.

이제 블럭의 수가 3일 때 보자.

```
1                                         
2            2                            1     
3        ->  3     1  ->  3  2  1  ->  3  2                                   
a  b  c      a  b  c      a  b  c      a  b  c      


                                                1
 ->    1     ->            ->       2  ->       2
       2  3      1  2  3      1     3           3
    a  b  c      a  b  c      a  b  c     a  b  c

```

총 7회를 이동하였다.

그런데 조금 자세히보면 특이한 상황이보인다.


```
# 초기상태
1
2
3
a  b  c

# 2, 1번 블록을 b로 이동

   2                            1
-> 3     1  ->  3  2  1  ->  3  2
   a  b  c      a  b  c      a  b  c

# 3번 블록 c(목적지) 이동

       1
->     2  3
    a  b  c

# 2, 1번 블록을 c로 이동
                                   1
                      2            2
-> 1  2  3  ->  1     3  ->        3
   a  b  c      a  b  c      a  b  c
```

즉 이걸 간단하게 정의하면 만약 하노이 탑을 옮기는 함수를

```
move_hanoi(n, s, d)  # n == 옮길 블럭수, s == 출발점, d == 목적지
```

라고 한다면

```
move_hanoi(3, a, c) = move_hanoi(2, a, b)\    # 3번 블럭을 제외한 블럭을 b로 이동
                      + 1\                    # 3번 블럭을 c로이동
                      + move_hanoi(2, b, c)   # b에 옮겨둔 블럭을 다시 c로 이동
```

가 된다.

다만,  a->b로 옮기든 b->c로 옮기든 횟수는 동일하므로 횟수만 세는 함수를
```
count_hanoi(n)
```

라고 할때, 이동 횟수만 가지고 다시 정리하면

```
count_hanoi(3) = count_hanoi(2)\    # 3번 블럭을 제외한 블럭을 b로 이동
                 + 1\               # 3번 블럭을 c로이동
                 + count_hanoi(2)   # b에 옮겨둔 블럭을 다시 c로 이동
               = 2 * count_hanoi(2) + 1
```

이 된다.

위 과정을 다음과 같이 일반화 가능하다 (직접 몇가지 케이스를 더 해보길 추천)

```
count_hanoi(n) = 2 * count_honoi(n-1) + 1
````

위 점화식을 이용해서 DP 알고리즘 방법으로 간단하게 하노이탑의 이동횟수는 구할 수 있다.

### Tips
사실

```
count_hanoi(n) = 2 * count_honoi(n-1) + 1
````

와 같이 간단한 형태의 점화식은 쉽게 아래와 같이 식을 전개해보므로써 다항식으로 바꿀수 있다.

```
count_hanoi(n) = 2 * count_honoi(n-1) + 1
               = 2 * (2 * count_honoi(n-2) + 1) + 1
               = 2 * (2 * (2 * count_honoi(n-3) + 1) + 1) + 1
               = ...
               = 2 * (2 * (2 * ... (2 * (2 * count_honoi(1) + 1) +1) ... + 1) + 1 ) + 1  # count_honoi(1) 은 1이다.
               = 2 * 2 * 2 * ... (2 * (2 * 1 + 1) + 1) ... + 1) + 1 ) + 1   
               = 2 * 2 * 2 * ... 2 * 2 * 1 +  2^(n-2) + 2^(n-3) ...  + 4 + 2 + 1
               = 2^(n-1) + 2^(n-2) + 2^(n-3) ...  + 4 + 2 + 1
````

또한 2의 지수승은 그 특징으로 인해 다음과 같이 간단히 바꿔진다.
```
count_hanoi(n) = 2^(n-1) + 2^(n-2) ...  + 4 + 2 + 1
               = 2^n - 1
````

단 여기선 DP를 연습하는 측면에서 위와 같이 _*문제로 부터 점화식 도출 -> DP 알고리즘 도출*_ 과정을 거쳤다.

### Source code

#### 이동 횟수 구하기 (DP)

DP 문제로 아래와 같이 간단하게 코드를 작성 할 수 있다.

```
def count_hanoi(N):
    count_list = [0 for i in range(N)]  # 0-indexing
    count_list[0] = 1

    for i in range(1, N):
        count_list[i] = 2 * count_list[i-1] + 1

    return count_list[-1]
```

하지만 앞서 Tips에서 이야기했듯이. 간단하게 결론을 도출할 수 있으므로 나는 이렇게 코드를 작성하였다.

```
def count_hanoi(N):
    return int(pow(2, N) - 1)
```

#### 블럭의 경로 출력하기 (재귀)

블럭의 개수 같은경우 앞서 설명했던

```
move_hanoi(3, a, c) = move_hanoi(2, a, b)\    # 3번 블럭을 제외한 블럭을 b로 이동
                      + 1\                    # 3번 블럭을 c로이동
                      + move_hanoi(2, b, c)   # b에 옮겨둔 블럭을 다시 c로 이동
```

이부분을 코드로 변경하면 정말 간단히 해결 할 수 있다.
```
def run_hanoi(N, a, b, c):
    # a = 1, b = 2, c = 3

    if N == 0:  # 재귀가 종료되는 시점이 있어야 한다.
        return

    run_hanoi(N-1, a, c, b)
    print(a, c)
    run_hanoi(N-1, b, a, c)
```

즉 전체 소스코드는 아래와 같다.

```
import sys
import math


def run_hanoi(N, a, b, c):
    # a = 1, b = 2, c = 3

    if N == 0:  # 재귀가 종료되는 시점이 있어야 한다.
        return

    run_hanoi(N-1, a, c, b)
    print(a, c)
    run_hanoi(N-1, b, a, c)


def count_hanoi(N):
    return int(math.pow(2, N) - 1)


if __name__ == "__main__":

    # input
    line = sys.stdin.readline()
    num_of_block = int(line)

    result = count_hanoi(num_of_block)
    print(result)

    if num_of_block <= 20:
        run_hanoi(num_of_block, 1, 2, 3)

```
