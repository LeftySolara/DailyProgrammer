/**
 * For r/DailyProgrammer challenge #2
 */

import java.lang.Math;
import java.util.Scanner;
import java.util.InputMismatchException;
import java.text.DecimalFormat;

public class InterestCalculator {

    public static void main(String[] args) {

        int userChoice;
        int years;
        double rate;
        double result;
        Scanner userInput = new Scanner(System.in);

        System.out.println("1) Calculate future value");
        System.out.println("2) Calculate initial value");
        System.out.print("Please choose an option: ");

        try {
            userChoice = userInput.nextInt();

            if (userChoice != 1 && userChoice != 2) {
                throw new InputMismatchException();
            }

            System.out.print("Please enter the interest rate: ");
            rate = userInput.nextDouble();

            System.out.print("Please enter the number of years of the investment: ");
            years = userInput.nextInt();

            if (userChoice == 1) {
                System.out.print("Please enter the amount of the principle investment: ");
                double principle = userInput.nextDouble();
                result = calculateFuture(principle, rate, years);
            } else {
                System.out.print("Please enter the future value of the investment: ");
                double futureValue = userInput.nextDouble();
                result = calculatePrinciple(futureValue, rate, years);
            }

        } catch (InputMismatchException e) {
            System.out.println("Incorrect input type entered.");
            return;
        }

        DecimalFormat df = new DecimalFormat("#.00");
        System.out.println("Your calculated result is $" + df.format(result));
    }

    // Calculate the future value of an investment with compound interest
    public static double calculateFuture(double principle, double interestRate, int years) {
        return principle * Math.pow(1 + interestRate, years);
    }

    // Calculate the initial investment before any interest accumulates
    public static double calculatePrinciple(double fututeValue, double interestRate, int years) {
        return fututeValue / Math.pow(1 + interestRate, years);
    }
}
