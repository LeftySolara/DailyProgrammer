/* r/Dailyprogrammer Challenge #1 (easy):
 * http://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/
 *
 * Create a program that will ask the user's name, age, and reddit username.
 * Have the program tell the info back in the form:
 *
 * "Your name is [name], you are [age] years old, and your username is [username].
 */

import java.util.Scanner;
import java.util.InputMismatchException;

public class userInfo {

    public static void main(String[] args) {

        String name, username;
        int age;
        Scanner userInput = new Scanner(System.in);

        System.out.print("Enter your name: ");
        name = userInput.next();

        try {
            System.out.print("Enter your age: ");
            age = userInput.nextInt();
        }
        catch(InputMismatchException e) {
            System.out.println("Please enter a number next time");
            return;
        }

        System.out.print("Enter your reddit username: ");
        username = userInput.next();

        System.out.println("Your name is " + name + ", you are " +
                age + " years old, and your reddit username is " + username + ".");
    }
}
