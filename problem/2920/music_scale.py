import sys

if __name__ == "__main__":
    line = sys.stdin.readline()
    note_list = [int(node) for node in line.split()]
    kinds_of_note = 8

    interval = note_list[1] - note_list[0]
    status = "ascending" if interval == 1 else "descending"

    for i in range(len(note_list) - 1):
        gap = note_list[i+1] - note_list[i]
        if gap != interval:
            status = "mixed"
            break

            # # 만약에 7 8 1 2 3 4 5 6 도 accending이 되려면 아래 주석을 해제하면 된다.
            # gap = (note_list[i+1] % kinds_of_note) - (note_list[i] % kinds_of_note)
            # if gap != interval:
            #     status = "mixed"
            #     break

    print(status)
