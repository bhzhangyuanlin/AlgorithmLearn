s1 = 'ABCBDAB'
s2 = "BDCABA"


def max_substr(s1, s2):
    res_array = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    res_arrow = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    len_s1 = len(s1)
    len_s2 = len(s2)
    str_content = ''
    for i in range(len_s1):
        for j in range(len_s2):
            if s1[i] != s2[j]:
                if res_array[i + 1][j] > res_array[i][j + 1]:
                    res_array[i + 1][j + 1] = res_array[i + 1][j]
                    res_arrow[i + 1][j + 1] = 1  # 表示左边来的
                elif res_array[i + 1][j] < res_array[i][j + 1]:
                    res_array[i + 1][j + 1] = res_array[i][j + 1]
                    res_arrow[i + 1][j + 1] = -1  # 表示上边来的
            else:
                res_array[i + 1][j + 1] = res_array[i][j] + 1
                res_arrow[i + 1][j + 1] = 0  # 表示上边来的

    m, n = len_s1, len_s2
    while m > 0 and n > 0:
        tmp = res_arrow[m][n]
        if tmp == 0:
            str_content += s1[m - 1]
            m -= 1
            n -= 1
        elif tmp == -1:
            m -= 1
        elif tmp == 1:
            n -= 1
    return res_array[len_s1][len_s2], str_content[::-1]


if __name__ == '__main__':
    print(max_substr(s1, s2))
