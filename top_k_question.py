import random


def sift(li, low, high):
    i = low
    j = 2 * i + 1
    temp = li[low]
    while j <= high:
        if j + 1 <= high and li[j + 1] < li[j]:
            j = j + 1
        if temp > li[j]:
            li[j], li[i] = li[i], li[j]
            i = j
            j = 2 * i + 1
        else:
            break
    li[i] = temp


def solove_topk(li, k):
    temp_li = li[0: k]
    for i in range(k // 2 - 1, -1, -1):
        sift(temp_li, i, k-1)

    # 上面是前k个建堆完成了，下面是遍历所有的树，筛选出前k大
    rest_li = li[k:]
    for i in rest_li:
        if i > temp_li[0]:
            temp_li[0] = i
            sift(temp_li, 0, k-1)

    # 上面已经筛选了前k大的数，下面是堆排序
    for i in range(k-1, -1, -1):
        temp_li[0], temp_li[i] = temp_li[i], temp_li[0]
        sift(temp_li, 0, i - 1)

    return temp_li


if __name__ == '__main__':
    test_list = [i for i in range(100)]
    random.shuffle(test_list)
    ans = solove_topk(test_list, 10)
    print(ans)
