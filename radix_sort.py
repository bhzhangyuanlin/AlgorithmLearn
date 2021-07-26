def radix_sort(li):
    max_num = max(li)
    max_bit = 0
    while max_num % 10:
        max_bit += 1
        max_num = max_num // 10

    for i in range(max_bit):
        group = [[] for _ in range(10)]
        new_li = []
        for item in li:
            n = (item // (10 ** i)) % 10
            group[n].append(item)
        for k in group:
            new_li += k
        li[:] = new_li


if __name__ == '__main__':
    test_li = [10, 2, 5, 15, 96, 198, 5876, 25, 0, 54, 12, 456, 123, 8, 11]
    radix_sort(test_li)
    print(test_li)
