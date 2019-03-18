import java.util.*;
public class sockMerchant {

    // Uses HashSet. A set with no duplicate elements.
    // Methods: .add and .remove
    
    static int sockMerchant(int n, int[] ar) {
        int totalPairs = 0;
        Set<Integer> colours = new HashSet<>();

        for (int i = 0; i < n; i++)
        {
            if (!colours.contains(ar[i]))
            {
                colours.add(ar[i]);
            }
            else
            {
                totalPairs++;
                colours.remove(ar[i]);
            }
        }
        return totalPairs;

    }
}