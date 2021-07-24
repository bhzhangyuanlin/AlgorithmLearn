import random


def insert_sort_gap(li, gap):
    for i in range(gap, len(li)):
        j = i - gap
        temp = li[i]
        while j >= 0:
            if temp < li[j]:
                li[j + gap] = li[j]
                j -= gap
            else:
                break
        li[j + gap] = temp


def shell_sort(li):
    li_len = len(li)
    if li_len > 1:
        d = li_len // 2
        while d >= 1:
            insert_sort_gap(li, d)
            d = d // 2r


if __name__ == '__main__':
    li = [i for i in range(11)]
    random.shuffle(li)
    # insert_sort(li)
    shell_sort(li)
    print(li)
