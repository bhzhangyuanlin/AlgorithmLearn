class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        n = len(matrix) - 1
        m = len(matrix[0]) - 1
        if matrix[0][0] > target:
            return False
        elif matrix[n][-1] < target:
            return False
        else:
            row_low = 0
            row_high = n
            is_find = False
            while not is_find and row_high >= row_low:
                mid = (row_low + row_high) // 2
                if matrix[mid][0] < target < matrix[mid][-1]:
                    left = 1
                    right = len(matrix[mid]) - 2
                    while right >= left:
                        row_mid = (left + right) // 2
                        if matrix[mid][row_mid] < target:
                            left = row_mid + 1
                        elif matrix[mid][row_mid] > target:
                            right = row_mid - 1
                        else:
                            is_find = True
                            break
                    break
                elif matrix[mid][0] > target:
                    row_high = mid - 1
                elif matrix[mid][-1] < target:
                    row_low = mid + 1
                else:
                    is_find = True
        return is_find


if __name__ == '__main__':
    c = Solution()
    matrix = [[1, 3, 5]]
    target = 4
    print(c.searchMatrix(matrix, target))
