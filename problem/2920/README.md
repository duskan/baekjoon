# 2920 음계

알고리즘
 1. 첫번째, 두번째 음의 차이를 비교 (증가인지 감소인지)
 2. 반복문 돌면서 첫 두음의 음차이랑 같은지 다른지 확인 

소스코드 
```
import sys

if __name__ == "__main__":
    # 입력
    line = sys.stdin.readline()
    
    # 값들 초기화
    note_list = [int(node) for node in line.split()]
    kinds_of_note = 8

    # 1, 2 번째 음 비교 (1이면 오름차순, -1이면 내림차순)
    interval = note_list[1] - note_list[0]
    status = "ascending" if interval == 1 else "descending"

    # 반복 수행, 만약 interval 과, 각 roop에서 계산한 gab이 다르면 mixed 
    # mixed 일때는 더이상 확인 할 필요 없으니 종료 
    for i in range(len(note_list) - 1):
        gab = note_list[i+1] - note_list[i]
        if gab != interval:
            status = "mixed"
            break


    print(status)
```

### 추가사항 

  * 처음엔 문제가 간단해서 cyclic 한경우도 고려해야하는줄 알았음 ( ```[4, 5, 6 ,7, 8, 1, 2, 3] # accending```)
  * 이항목을 고려한 코드(버리기 아까워서) 추가 
  
```
import sys

if __name__ == "__main__":
    # 입력
    line = sys.stdin.readline()
    
    # 값들 
    note_list = [int(node) for node in line.split()]
    kinds_of_note = 8

    # 1, 2 번째 음 비교 (1이면 오름차순, -1이면 내림차순)
    interval = note_list[1] - note_list[0]
    status = "ascending" if interval == 1 else "descending"

    # 반복 수행, 만약 interval 과, 각 roop에서 계산한 gab이 다르면 mixed 
    # mixed 일때는 더이상 확인 할 필요 없으니 종료 
    for i in range(len(note_list) - 1):
        gab = note_list[i+1] - note_list[i]
        if gab != interval:

            gab = (note_list[i+1] % kinds_of_note) - (note_list[i] % kinds_of_note)
            if gab != interval:
                status = "mixed"
                break


    print(status)
```
