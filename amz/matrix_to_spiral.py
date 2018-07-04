
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        [          col0     col1    col2    col3
          row 0    [1,      2,      3,      4],
          row 1    [5,      6,      7,      8],
          row 2    [9,      10,     11,     12]
        ]
        """
        if not matrix:
            return []

        min_row = min_col = 0
        max_row = len(matrix) - 1
        max_col = len(matrix[0]) - 1
        result = []
        while min_row <= max_row and min_col <= max_col:
            for i in range(min_col, max_col+1):
                result.append(matrix[min_row][i])
            min_row += 1

            for i in range(min_row, max_row+1):
                result.append(matrix[i][max_col])
            max_col -= 1

            if max_row >= min_row:
                for i in range(max_col, min_col-1, -1):
                    result.append(matrix[max_row][i])
                max_row -= 1

            if max_col >= min_col:
                for i in range(max_row, min_row-1, -1):
                    result.append(matrix[i][min_col])
                min_col += 1

        return result

input = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12]
]
input = [[2,5,8],
         [4,0,-1]]
s = Solution()
res = s.spiralOrder(input)
print (res)
