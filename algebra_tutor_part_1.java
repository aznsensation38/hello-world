import java.util.*;

public class algebra_tutor_part_1{
    
    /** 
     * numGenerator method
     * Uses the java.util.Random class to generate a random Number.  
     * While loop ensures that the number is between 1 and 15, inclusively.
     * @param None
     * @return A random number betwee 1 and 15 <iint>
     */
    private static int numGenerator() {
        Random rand = new Random();
        int randNum = rand.nextInt(16);
        
        while (randNum == 0) {
            randNum = rand.nextInt(16);
        }

        return randNum;
    }

      /** 
     * getAnswerInput method
     * Uses the java.util.Scanner class to read a user's input number answer  
     * @param None
     * @return Returns the user's input <int>.
     */
    private static int getAnswerInput() throws Exception {
        Scanner input = new Scanner(System.in);
        int answerInput = input.nextInt();
        
        return answerInput;
    }
    /** 
     * greeting method
     * Greets the user with the assignment of the program.  
     * @param None
     * @return None
     */
    private static void greeting() {
        System.out.println("\n###########################################");
        System.out.println("#     Beginning Algebra Tutor Program     #");
        System.out.println("#                 Part 1                  #");
        System.out.println("#             by: Emil Pham               #");
        System.out.println("###########################################\n");
    }

    /** 
     * Main program
     * Generates random numbers for y = m*x+b and calculates the answer y.
     * Takes the user's input and compares the input with the answer.  
     * Will let user know if he/she is right or wrong.
     * **** Checking/Looping of the user input is currently still broken.  
     */
     public static void main(String[] args) throws Exception {
        
        int y, x, m, b, userAnswer;
        y = userAnswer = 0;
        boolean tryAgain = true;
       
        m = numGenerator();
        x = numGenerator();
        b = numGenerator();
        y = (m * x) + b;

        greeting();

        System.out.println("\nUsing a random number generator:");
        System.out.println("\nm: " + m);
        System.out.println("x: " + x);
        System.out.println("b: " + b);
        System.out.println("\n\t\ty = " + m + " * " + x + " + " + b);
        
        System.out.print("What is the answer for y?: ");
        userAnswer = getAnswerInput();       

                       
        while (y != userAnswer && tryAgain == true) {
            Scanner tryAgainInput = new Scanner(System.in);
            System.out.print("\nSorry that is incorrect. Do you want to try again, Y or N?: ");
            String tryAgainIn = tryAgainInput.nextLine();
                        
            if (tryAgainIn.equalsIgnoreCase("y") == true) {
                System.out.print("\nWhat is the answer for y?: ");
                userAnswer = getAnswerInput();
                tryAgain = true;
            }                 
            else {
                tryAgain = false;
                tryAgainInput.close();                  
            }
               
        }      

        if(userAnswer == y) {
            System.out.println("\nCorrect!");
        }
        else {
            System.out.println("\nSorry, that is incorrect.");
        }

        System.out.println("The correct answer is y = " + y);
       
    }
}