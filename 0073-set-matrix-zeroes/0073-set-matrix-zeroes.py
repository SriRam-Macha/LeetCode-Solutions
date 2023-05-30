class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r = dict()
        c = dict()
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    r[i] = True
                    c[j] = True

        for i in r.keys():
            for j in range(n):
                matrix[i][j] =0

        for j in c.keys():
            for i in range(m):
                matrix[i][j] = 0
    