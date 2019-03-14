public class plusMinus_RoundDecimals {

    // Void ==> No Return Value
    static void plusMinus(int[] arr) {
        double pos=0,neg=0,zero=0,length = arr.length;
        double posRatio, negRatio, zeroRatio;
        
        for (int item : arr)
        {
            if (item > 0){
                pos += 1;
            }
            else if (item < 0){
                neg += 1;
            }
            else {
                zero += 1;
            }
        }
        posRatio = (pos/length);
        negRatio = (neg/length);
        zeroRatio = (zero/length);
        System.out.printf("%.6f%n", posRatio);
        System.out.printf("%.6f%n", negRatio);
        System.out.printf("%.6f%n", zeroRatio);

    }
}