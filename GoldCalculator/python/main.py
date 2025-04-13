

class GoldCalculator: 
    def __init__(self, matrix):
        self.matrix_sum = self.calculate_matrix_sum(matrix)

    def calculate_matrix_sum(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        matrix_sum = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):

                top = matrix_sum[i - 1][j] if i > 0 else 0
                left = matrix_sum[i][j - 1] if j > 0 else 0
                top_left = matrix_sum[i - 1][j - 1] if i > 0 and j > 0 else 0
                matrix_sum[i][j] = top + left - top_left + matrix[i][j];
    
        return matrix_sum

    def how_much_gold(self, row, col, height, width):
        endRow = row + width - 1; 
        endCol = col + height - 1;

        if (row < 0 or col < 0 or endRow >= len(self.matrix_sum) or endCol >= len(self.matrix_sum[0])):
            return 0
        
        total = self.matrix_sum[endRow][endCol];

        if (row > 0): total -= self.matrix_sum[row - 1][endCol]
        if (col > 0): total -= self.matrix_sum[endRow][col - 1]
        if (row > 0 and col > 0): total += self.matrix_sum[row - 1][col - 1]

        return total
        
        

def unit_tests():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    nc = GoldCalculator(matrix)
    # Test full matrix sum
    assert nc.how_much_gold(0, 0, 4, 4) == sum(range(1, 17))

    # Test top-left 2x2 block
    assert nc.how_much_gold(0, 0, 2, 2) == 1 + 2 + 5 + 6  # 14

    # Test center 2x2 block
    assert nc.how_much_gold(1, 1, 2, 2) == 6 + 7 + 10 + 11  # 34

    # Test bottom-right 1x1 block
    assert nc.how_much_gold(3, 3, 1, 1) == 16

    # Test top-right block 
    assert nc.how_much_gold(0, 2, 2, 2) == 3 + 4 + 7 + 8

    # Test out of range 
    assert nc.how_much_gold(-5, -5, 0, 0) == 0
    assert nc.how_much_gold(6, 6, 2, 2) == 0
    assert nc.how_much_gold(0, -5, 2, 3) == 0
    assert nc.how_much_gold(-2, 3, 2, 3) == 0

    print("All tests passed!")

if __name__ == "__main__":
    print("Hello World")
    unit_tests()

