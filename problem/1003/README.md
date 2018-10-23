# 피보나치 알고리즘의 0, 1 호출 횟수 구하기

이 알고리즘 재귀처럼 보이지만 DP(Dynamic Programing)을 활용하는 방법이다. 방법은 생각보다 간단하다.

fibonacci 계산시 0, 1을 호출한 회수를 가져오는 함수를 nfibo라고 하자

우선 값이 0일 때는 각각 fibonacci(0) 한번만 호출하면 된다. 1일 때도 fibonacci(1) 한번만 호출하면된다.
즉 nfibo(0), nfibo(1) 일 때
```
nfibo(0)
>>> [1, 0]
nfibo(1)
>>> [0, 1]
```
이라는 결과를 얻는다.

이제 입력값이 2, 3인 경우를 살펴보자.
우선적으로 2 인 경우에는
```
fibonacci(2) = fibonacci(0) + fibonacci(1)
nfibo(2) = [1, 0] + [0, 1]
         = [1, 1]
```
이므로 0, 1을 각각 한번씩 호출한다.

3일때에로 넘어오게되면
```
fibonacci(3) = fibonacci(1) + fibonacci(2)
             = fibonacci(1) + fibonacci(0) + fibonacci(1)

nfibo(3) = [0, 1] + [1, 0] + [0, 1]
         = [1, 2]
```
로 계산된다.

여기서 DP의 특징을 잡아낼 수 있는데
만약 fibonacci(2)의 0, 1의 호출 횟수, 즉 nfibo(2)를 미리 알고 있으므로  
```
fibonacci(3) = fibonacci(1) + fibonacci(2)

nfibo(3) = nfibo(1) + nfibo(2)
         = [0, 1] + [1, 1]
         = [1, 2]
```
와 같이 좀 더 간단히 나타낼 수 있다.

이를 좀더 일반화 해서 나타낸다면, 만약 입력받은 수가 k일때 nfibo(k)는

```
nfibo(k) = nfibo(k-1) + nfibo(k-2)
         = [nfibo(k-1)[0] + nfibo(k-2)[0], nfibo(k-1)[1] + nfibo(k-2)[1]]
```
가 되므로 미리 우리는  nfibo(k-1), nfibo(k-2) 값만 미리 알고있다면 역추적하여 매번 계산 할 필요가 없어진다.

아래 코드는 이를 구현 한 것으로. 문제의 입력값에서 입력 받을 수가 여러개가 들어오지만.
가장 값이 큰 경우를 기준으로 한번만 계산하고나면, 매번 계산할 필요 없이 이미 저장된 값을 활용하여 결과를 뿌려주는 코드이다.

```
import sys

if __name__ == "__main__":

    # input
    line = sys.stdin.readline()
    num_of_fibo = int(line)

    # save input data
    fibo_sample_list = []
    for i in range(num_of_fibo):
        line = sys.stdin.readline()
        fibo = int(line)
        fibo_sample_list.append(fibo)

    # make result using dp
    biggest_fibo = max(fibo_sample_list)
    cnt_fibo_list = [[0, 0] for i in range(biggest_fibo+1)]  # because of 1-index

    cnt_fibo_list[0] = [1, 0]  # init value 0
    cnt_fibo_list[1] = [0, 1]  # init value 1

    for i in range(2, biggest_fibo + 1):  # calc fibonacci call (using dp)
        cnt_fibo_list[i] = [
            cnt_fibo_list[i-1][0] + cnt_fibo_list[i-2][0],
            cnt_fibo_list[i-1][1] + cnt_fibo_list[i-2][1]
        ]

    # print result
    # just call saved result
    for fibo_sample in fibo_sample_list:
        print(cnt_fibo_list[fibo_sample][0], cnt_fibo_list[fibo_sample][1])
```
