def binary_search(li, var):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (right + left) // 2
        if li[mid] < var:
            left = mid + 1
        elif li[mid] > var:
            right = mid - 1
        else:
            return mid
    return None


if __name__ == '__main__':
    test_li = [1, 2, 3, 4, 5, 6, 7, 9, 11, 15, 293]
    print(binary_search(test_li, 7))
