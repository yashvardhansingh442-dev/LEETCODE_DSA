class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []

        for row_num in range(numRows):
            # Start each row with 1, fill with None/0 placeholders for now
            row = [1] * (row_num + 1)
            
            # Update the middle elements (excluding the first and last element)
            for j in range(1, row_num):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
            
            triangle.append(row)
            
        return triangle
