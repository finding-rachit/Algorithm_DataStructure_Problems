import java.util.*;

public class compareTriplets_List {

    // Complete the compareTriplets function below.
    static List<Integer> compareTriplets(List<Integer> a, List<Integer> b) {
        int aliceScore=0;
        int bobScore=0;
        List<Integer> result = new ArrayList<Integer>();

        for (int i=0; i < 3; i++)
        {
            if (a.get(i) > b.get(i))
            {
                aliceScore += 1;
            }
            else if (b.get(i) > a.get(i))
            {
                bobScore += 1;
            }
        }
        result.add(aliceScore);
        result.add(bobScore);

        return result;

    }
}