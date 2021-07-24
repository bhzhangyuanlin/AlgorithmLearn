def insert_sort(li):
    for i in range(1, len(li)):
        temp = li[i]
        j = i - 1
        while j >= 0 and li[j] > temp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = temp


if __name__ == '__main__':
    test_li = [0, 8, 7, 6, 4, 5, 9, 3, 1, 2]
    insert_sort(test_li)
    print(test_li)
