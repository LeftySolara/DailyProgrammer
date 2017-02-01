/* r/Dailyprogrammer Challenge #1 (easy):
 * http://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/
 *
 * Create a program that will ask the user's name, age, and reddit username.
 * Have the program tell the info back in the form:
 *
 * "Your name is [name], you are [age] years old, and your username is [username]."
 *
 * For extra credit, have the program log this information to a file to be accessed later.
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAXLINE 256  /* maximum length of an input line */

enum error_codes
{
    E_INVALID_AGE = 1,
    E_FILE_IO_ERROR = 2
};

int main(int argc, char *argv)
{
    char name[MAXLINE], username[MAXLINE], agestr[MAXLINE];
    int age;

    printf("What is your name?\n");
    fgets(name, MAXLINE, stdin);

    printf("What is your age?\n");
    fgets(agestr, MAXLINE, stdin);

    if ((age = atoi(agestr)) == 0 || age < 0) {   /* not an integer, or is negative */
        fprintf(stderr, "error: invalid value for age\n");
        return E_INVALID_AGE;
    }

    printf("What is your reddit username?\n");
    fgets(username, MAXLINE, stdin);

    /* remove leftover newline characters from fgets() */
    name[strlen(name)-1] = '\0';
    username[strlen(username)-1] = '\0';

    printf("Your name is %s, you are %d years old, and your username is %s.\n", name, age, username);

    /* write info to a file */
    FILE *fp = fopen("userinfo.txt", "w");
    if (fp == NULL) {
        fprintf(stderr, "Error opening file\n");
        exit(E_FILE_IO_ERROR);
    }
    fprintf(fp, "Name: %s\nAge: %d\nUsername: %s", name, age, username);
    fclose(fp);

    return 0;
}
