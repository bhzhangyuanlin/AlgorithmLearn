import random


def sift(li, low, high):
    i = low
    j = 2 * i + 1
    temp = li[low]
    while j <= high:
        if j + 1 <= high and li[j + 1] > li[j]:
            j = j + 1
        if temp < li[j]:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break
    li[i] = temp


def creat_heap(li):
    for i in range(len(li) // 2 - 1, -1, -1):
        sift(li, i, len(li) - 1)


def heap_sort(li):
    creat_heap(li)
    for i in range(len(li) - 1, -1, -1):
        li[i], li[0] = li[0], li[i]
        sift(li, 0, i - 1)


if __name__ == '__main__':
    test_list = [i for i in range(100)]
    random.shuffle(test_list)
    print(test_list)
    heap_sort(test_list)
    print(test_list)
