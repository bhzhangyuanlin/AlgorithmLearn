def linear_search(li, var):
    for idx, item in enumerate(li):
        if var == item:
            return idx

    return None


if __name__ == '__main__':
    test_li = [1, 5, 6, 7, 8, 9, 10, 3, 4, 0]
    print(linear_search(test_li, 13))
