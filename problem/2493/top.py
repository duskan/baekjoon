import sys

if __name__ == "__main__":
    # input
    num_of_top = int(sys.stdin.readline())
    buildings = sys.stdin.readline().split()

    top_stack = []

    result = [0 for i in range(len(buildings)+1)]

    for i in range(len(buildings)):
        pos = i+1
        building = int(buildings[i])
        while(top_stack):
            top = top_stack[-1]
            if top[1] > building:
                result[pos] = top[0]
                break
            else:
                top_stack.pop()
        top_stack.append([pos, building])

    print(" ".join([str(v) for v in result[1:]]))
