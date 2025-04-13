package udpated;

public class GoldCalculator {
    private int[][] matrixSum;

    public GoldCalculator(int[][] matrix) {
        this.matrixSum = calculateMatrixSum(matrix);
    }

    private int[][] calculateMatrixSum(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        int[][] matrixSum = new int[rows][cols];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                int top = (i > 0) ? matrixSum[i - 1][j] : 0;
                int left = (j > 0) ? matrixSum[i][j - 1] : 0;
                int topLeft = (i > 0 && j > 0) ? matrixSum[i - 1][j - 1] : 0;
                matrixSum[i][j] = top + left - topLeft + matrix[i][j];
            }
        }

        return matrixSum;
    }

    public int howMuchGold(int row, int col, int height, int width) {
        int endRow = row + height - 1;
        int endCol = col + width - 1;

        if (row < 0 || col < 0 || endRow >= matrixSum.length || endCol >= matrixSum[0].length) {
            return 0;
        }

        int total = matrixSum[endRow][endCol];

        if (row > 0) {
            total -= matrixSum[row - 1][endCol];
        }
        if (col > 0) {
            total -= matrixSum[endRow][col - 1];
        }
        if (row > 0 && col > 0) {
            total += matrixSum[row - 1][col - 1];
        }

        return total;
    }

    // Unit test helper
    public static void main(String[] args) {
        int[][] matrix = {
                {1, 2, 3, 4},
                {5, 6, 7, 8},
                {9, 10, 11, 12},
                {13, 14, 15, 16}
        };

        GoldCalculator gc = new GoldCalculator(matrix);

        assert gc.howMuchGold(0, 0, 4, 4) == 136;
        assert gc.howMuchGold(0, 0, 2, 2) == 14;
        assert gc.howMuchGold(1, 1, 2, 2) == 34;
        assert gc.howMuchGold(3, 3, 1, 1) == 16;
        assert gc.howMuchGold(0, 2, 2, 2) == 22;

        assert gc.howMuchGold(-5, -5, 0, 0) == 0;
        assert gc.howMuchGold(6, 6, 2, 2) == 0;
        assert gc.howMuchGold(0, -5, 2, 3) == 0;
        assert gc.howMuchGold(-2, 3, 2, 3) == 0;

        System.out.println("All tests passed!");
    }
}
