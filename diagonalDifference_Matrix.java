public class diagonalDifference_Matrix {

    // Return absolute difference of diagonals in a matrix
    static int diagonalDifference(int[][] arr) {
        int sumPrimary=0,sumSecondary = 0;

        int i = 0;
        int j = 0;

        while (i < arr.length)
        {
            sumPrimary += arr[i][j];
            i++;
            j++;
        }
        i = arr.length - 1;
        j = 0;
        while (i >= 0)
        {
            sumSecondary += arr[i][j];
            i--;
            j++;
        }
        return (Math.abs(sumPrimary - sumSecondary));

    }
}