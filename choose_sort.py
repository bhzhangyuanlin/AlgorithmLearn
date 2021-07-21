def choose_sort(li):
    li_len = len(li)
    for i in range(li_len):
        max_index = 0
        for j in range(1, li_len - i):
            if li[j] > li[max_index]:
                max_index = j
        if max_index != li_len - i-1:
            li[max_index], li[li_len - i - 1] = li[li_len - i - 1], li[max_index]


if __name__ == '__main__':
    test_li = [78, 1, 8, 9, 0, 4, 2, 7, 3, 6, 5, -1, 19, 5, -9, 0, 5, 79, -79]
    choose_sort(test_li)
    print(test_li)
