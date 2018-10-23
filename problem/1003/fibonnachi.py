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
