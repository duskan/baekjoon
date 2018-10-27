import sys


if __name__ == "__main__":
    # input value
    pipe_str = sys.stdin.readline().strip()

    raser_list = []
    pipe_list = []
    m_stack = []

    id = 0
    for index in range(len(pipe_str)):
        char = pipe_str[index]

        if char == "(":
            is_raser = True
            m_stack.append(index)
        elif char == ")":
            if is_raser:
                is_raser = False
                pos = m_stack.pop()  # raser이므로 파이프 목록에 추가되지 않도록 제거
                raser_list.append(pos)
            else:
                start_pos = m_stack.pop()
                pipe_list.append([start_pos, index, id])
                id += 1

    num_of_piece_list = [1 for i in range(id)]

    sorted_pipe_list = sorted(pipe_list, key=(lambda x: x[0]))

    for raser in raser_list:
        remove_list = []
        for pipe in sorted_pipe_list:
            s = pipe[0]
            e = pipe[1]
            id = pipe[2]
            if s > raser:
                break
            if e < raser:
                remove_list.append(pipe)
                continue
            num_of_piece_list[id] += 1
        for pipe in remove_list:
            sorted_pipe_list.remove(pipe)

    print(sum(num_of_piece_list))
    
