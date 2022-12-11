import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.IntStream;

public class CampCleanup1 {
    public static void main(String[] args) {
        File f = new File("input.txt");
        f.setReadOnly();
        try (Scanner fileReader = new Scanner(f)) {
            final Pattern p = Pattern.compile("(\\d+)-(\\d+),(\\d+)-(\\d+)");
            int contains = 0;
            while (fileReader.hasNextLine()) {
                String line = fileReader.nextLine();
                Matcher m = p.matcher(line);
                m.find();
                int[] rangeIndexList = IntStream.range(1, 5).map(i -> Integer.parseInt(m.group(i))).toArray();
                if ((rangeIndexList[0] <= rangeIndexList[2] && rangeIndexList[1] >= rangeIndexList[3]) ||
                    (rangeIndexList[2] <= rangeIndexList[0] && rangeIndexList[3] >= rangeIndexList[1])) {
                    contains += 1;
                }
            }
            System.out.println(contains);
        } catch (FileNotFoundException ex) {
            ex.printStackTrace();
        }
    }
}