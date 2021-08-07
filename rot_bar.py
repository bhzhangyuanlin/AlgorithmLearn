price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]  # 不同长度段的价格


def rot_recursion(p, n):  # 递归思路写切割钢条问题，左边不切，切右边
    if n == 0:
        return 0
    else:
        r = 0  # 总价
        for i in range(1, n + 1):
            r = max(r, p[i] + rot_recursion(p, n - i))
        return r


def rot_recursion_2(p, n):  # 比较所有情况的递归，两边都切一遍
    if n == 0:
        return 0
    else:
        r = 0
        for i in range(1, n):
            r = max(r, rot_recursion(p, i) + rot_recursion(p, n - i))
        return r


def rot_bar_dp(p, n):
    if n == 0:
        return 0
    else:
        r = 0
        k = 0  # 判断单次循环左边长度在最优的时候
        max_r = [0]
        max_r_i = [0]
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                if r < p[j] + max_r[i - j]:
                    r = p[j] + max_r[i - j]
                    k = j
            max_r.append(r)
            max_r_i.append(k)
        return max_r, max_r_i


def rot_bar_solution(p, n):
    max_r, max_r_i = rot_bar_dp(p, n)
    res = []
    while True:
        i = max_r_i[n]
        if i != 0:
            res.append(i)
            n = n - i
        else:
            break
    return res


if __name__ == '__main__':
    print(rot_recursion(price, 9))
    print(rot_recursion_2(price, 9))
    # print(rot_bar_dp(price, 9))
    print(rot_bar_solution(price, 9))
