class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for row in range(0, numRows):
            temp = [1]
            for col in range(1, row + 1):
                if col == row:
                    temp.append(1)
                else:
                    temp.append(res[row - 1][col] + res[row - 1][col - 1])
            res.append(temp)
        return res
