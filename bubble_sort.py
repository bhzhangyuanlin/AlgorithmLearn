def bubble_sort(li):
    li_len = len(li)
    for i in range(li_len):
        for j in range(li_len - i - 1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]


def bubble_sort_optimize(li):
    li_len = len(li)
    for i in range(li_len):
        is_exchange = False
        for j in range(li_len - i - 1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                is_exchange = True
        if not is_exchange:  # 没交换，说明已经排好了，不需要后续冒泡了
            break


if __name__ == '__main__':
    li_list = [9, 6, 4, 3, 2, 8, 5, 1, 0, 7]
    # li_list = [9, 8, 7, 1, 2, 3, 4, 5, 6]
    bubble_sort_optimize(li_list)
    # bubble_sort(li_list)
    print(li_list)
