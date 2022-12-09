import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class RPS {
    static int calculateScore(char player, char opp) {
        switch (player) {
            case 'X':
                player = 'R';
                break;
            case 'Y':
                player = 'P';
                break;
            case 'Z':
                player = 'S';
                break;
        }

        switch (opp){
            case 'A':
                opp = 'R';
                break;
            case 'B':
                opp = 'P';
                break;
            case 'C':
                opp = 'S';
                break;
        }

        int score = 0;

        switch (player) {
            case 'R':
                switch (opp) {
                    case 'R':
                        score += 3;
                        break;
                    case 'P':
                        score += 0;
                        break;
                    case 'S':
                        score += 6;
                        break;
                }
                score += 1;
                break;    
            case 'P':
                switch (opp) {
                    case 'R':
                        score += 6;
                        break;
                    case 'P':
                        score += 3;
                        break;
                    case 'S':
                        score += 0;
                        break;
                }   
                score += 2;
                break;
            case 'S':
                switch (opp) {
                    case 'R':
                        score += 0;
                        break;
                    case 'P':
                        score += 6;
                        break;
                    case 'S':
                        score += 3;
                        break;
                }
                score += 3;
                break;
        }
        return score;
    }

    public static void main(String[] args) {
        String inputPath = "input.txt";
        if (args.length > 0) {
            inputPath = args[0];
        }

        File f = new File(inputPath);
        f.setReadOnly();

        try (Scanner reader = new Scanner(f)) {
            int totalScore = 0;
            while (reader.hasNextLine()) {
                String line = reader.nextLine().stripTrailing();
                String[] choices = line.split(" ");
                totalScore +=  calculateScore(choices[1].charAt(0), choices[0].charAt(0));
            }
            System.out.println(totalScore);
        } catch (FileNotFoundException ex) {
            System.out.println("Error while opening file");
            ex.printStackTrace();
            return;
        }
    }
}
