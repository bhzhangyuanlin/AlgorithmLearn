import random


def bucket_sort(li, bucket_num, max_num):
    bucket = [[] for _ in range(bucket_num)]
    for i in li:
        bucket_gooup = min(i // (max_num // bucket_num), bucket_num - 1)
        bucket[bucket_gooup].append(i)
        for j in range(len(bucket[bucket_gooup]) - 2, -1, -1):
            if bucket[bucket_gooup][j] > i:
                bucket[bucket_gooup][j], bucket[bucket_gooup][j + 1] = bucket[bucket_gooup][j + 1], \
                                                                       bucket[bucket_gooup][j]
            else:
                bucket[bucket_gooup][j + 1] = i
                break

    res = []
    print(bucket)
    for group in bucket:
        res += group
    li[:] = res


if __name__ == '__main__':
    test_list = [random.randint(0, 101) for _ in range(20)]
    print(test_list)
    bucket_sort(test_list, 5, 100)
    print(test_list)
