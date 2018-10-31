# 10799
## Stack
Stack은 Queue와 더불어 자료구조를 공부하면 가장 먼저 "자료구조 뭔가 멋진 거 같아" 라고 많이들 느끼는 개념으로 LIFO(Last-In First-Out)의 원리로 동작한다.

### LIFO(Last-in First-out): 장롱안의 이불

Stack을 설멍할 때 가장 많이 예를 드는 장롱안의 이불은 LIFO의 성질을 가장 잘보여주는 예이다.  

이불을 장롱에 넣게될경우 먼저 넣은것부터 차례로 차곡 차곡 쌓이게되는데 나중에 이불을 빼기 위해서는, 맨 마지막에 넣었던
이불부터 순차적으로 하나씩 빼야 개어 논 이불을 흐터리트리지않고 뺄 수 있다.

마찬가지로 Stack역시 데이터를 집어넣는데로 차곡차곡 쌓아올린다. 하지만 데이터를 뺄때에는
맨 마지막에 넣어둔것 부터 빠져나오도록 한다.

즉 마지막에 넣은것이 맨처음에 나온다(Last-In First-out)


### ~컬렉션~ 스택 인터페이스
이 문제는 Stack의 기본적인 인터페이스를 묻는 문제이다. 일반적으로 Stack, Queue에서 사용되는 인터페이스는 다음과 같다.

(사실 Queue, Stack뿐만 아니라 대부분의 Collection에서 사용되는 인터페이스이다.)

- ```push(input_value)```
    - 컬렉션에 데이터의 입력해주는 인터페이스. input_value값을 컬랙션에 넣어준다.
- ```pop()```
    - 컬랙션의 값을 꺼내는 인터페이스. Pop()을 호출하면 컬렉션에서 값을 꺼내고, 해당 값을 리턴한다.
- ```empty()```
    - 컬렉에 값이 들어있는지 없는지 유무를 확인해주는 인터페이스. 값이 있을 경우 True, 없을경우 False를 리턴한다.
    - 사용하는 언어나 경우에 따라서는 1, 0 혹은 여러 다른값을 리턴할 수도 있다.
- ```size()```
    - 컬렉션에 저장된 데이터의 수를 출력해주는 인터페이스.
- ```top()```
    - 컬렉션에서 다음에 출력될 값을 보여주는 인터페이스.
    - ```pop()``` 인터페이스와 비슷하게 다음 우선순위의 값을 보여주지만 값을 지우는 ```pop()```과 달리, 값을 빼내지않고 단순 조회만 하는 차이점이 있다.

컬렉션의 종류에 따라 몇가지 Operator가 추가되거나 변경되는 경우가 있으나, 대부분의 컬랙선들은 위 기능들을 포함하고 있다.

이번 문제에서 역시 위 기능들을 구현하는 문제로 이를 구현하고나면 Stack의 기본적인 기능은 다 구현한거라고 보아도 무방하다.


## Stack의 구현

Python에서는 list만 잘 이용하면 추가적인 고민없이 바로 Stack처럼 사용 할 수 있다. 심지어 길이도 무제한이다.

하지만 Stack을 이해를 위해 아래와 같이 인터페이스를 직접 구현해보는걸 추천한다.

```
class Stack:
    def __init__(self):
        self.stack = []

    def top(self):
        if self.empty() == 1:
            return -1
        return self.stack[-1]

    def empty(self):
        if self.stack:
            return 0
        return 1

    def size(self):
        return len(self.stack)

    def push(self, op):
        self.stack.append(op)

    def pop(self):
        if self.empty() == 1:
            return -1
        return self.stack.pop()
```

## 전체 코드

위 스택 코드를 이용해서 전체 구현한 source는 아래와 같다.

```
import sys


class Stack():
    def __init__(self):
        self.stack = []

    def top(self):
        if self.empty() == 1:
            return -1
        return self.stack[-1]

    def empty(self):
        if self.stack:
            return 0
        return 1

    def size(self):
        return len(self.stack)

    def push(self, op):
        self.stack.append(op)

    def pop(self):
        if self.empty() == 1:
            return -1
        return self.stack.pop()


if __name__ == "__main__":
    # input
    num_of_commands = int(sys.stdin.readline())
    stack = Stack()
    for i in range(num_of_commands):
        commands = sys.stdin.readline().strip().split()

        command = commands[0]

        if command == "push":
            stack.push(commands[1])
        elif command == "top":
            print(stack.top())
        elif command == "empty":
            print(stack.empty())
        elif command == "size":
            print(stack.size())
        elif command == "pop":
            print(stack.pop())

        # print(stack.stack)

```
