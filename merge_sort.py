import random


def merge_data(li, start, mid, end):
    i = start
    j = mid + 1
    li_tmp = []
    while i <= mid and j <= end:
        if li[i] < li[j]:
            li_tmp.append(li[i])
            i += 1
        else:
            li_tmp.append(li[j])
            j += 1
    if i <= mid:
        li_tmp = li_tmp + li[i:mid+1]
    else:
        li_tmp = li_tmp + li[j:end+1]
    li[start:end+1] = li_tmp


def merge_recursion(li, start, end):
    mid = (start + end) // 2
    if start < end:
        merge_recursion(li, start, mid)
        merge_recursion(li, mid+1, end)
        merge_data(li, start, mid, end)


def merge_sort(li):
    merge_recursion(li, 0, len(li) - 1)


if __name__ == '__main__':
    test_list = [i for i in range(16)]
    random.shuffle(test_list)
    merge_sort(test_list)
    print(test_list)

