import random


def quick_sort(li, left, right):
    if left < right:
        mid = separate_data(li, left, right)
        quick_sort(li, 0, mid - 1)
        quick_sort(li, mid + 1, right)


def separate_data(li, left, right):
    rand_num = random.randint(left, right)  # 降低最坏情况的概率
    li[left], li[rand_num] = li[rand_num], li[left]  # 将随机下标的值和最左侧的值互换位置
    temp = li[left]
    left_is_blank_flag = True
    while left < right:
        if left_is_blank_flag:
            if li[right] < temp:
                li[left] = li[right]
                left_is_blank_flag = False
            else:
                right -= 1
        else:
            if li[left] > temp:
                li[right] = li[left]
                left_is_blank_flag = True
            else:
                left += 1
    li[left] = temp  # left = right at this step
    return left


if __name__ == '__main__':
    test_li = [-1, 0, 5, 3, 1, 2, 9, 6, 8, 7, -1, 4]
    quick_sort(test_li, 0, len(test_li)-1)
    print(test_li)
