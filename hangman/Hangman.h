#include <string>
using std::string;
#include <fstream>
using std::fstream;
#include <algorithm>
using std::remove_copy_if;
#include <stdlib.h>
#include <time.h>

// strings for each line in the hangman drawing
// meant to be built from the bottom up
struct hangman_drawing
{
    string gallow_right_leg = "   |     |\n   |     O\n   |    /|\\\n   |    / \\\n   |";
    string gallow_left_leg = "   |     |\n   |     O\n   |    /|\\\n   |    /\n   |";
    string gallow_right_arm = "   |     |\n   |     O\n   |    /|\\\n   |\n   |";
    string gallow_left_arm = "   |     |\n   |     O\n   |    /|\n   |\n   |";
    string gallow_body = "   |     |\n   |     O\n   |     |\n   |\n   |";
    string gallow_head = "   |     |\n   |     O\n   |\n   |\n   |";
    string gallow_pole_rope = "   |     |\n   |\n   |\n   |\n   |";
    string gallow_top = "   -------";
    string gallow_pole = "   |\n   |\n   |\n   |\n   |";
    string gallow_base = "-------";
};


#ifndef HANGMAN_H
#define HANGMAN_H

#define MAX_WORD_LENGTH 20
#define WORD_FILE "wordlist.txt"
// #define CAPS true

class Hangman
{
private:
    char* word;             // chosen word to guess
    char* display_word;     // version displayed to player
    // int word_length;
    // bool has_won;
    // string difficulty;

public:
    Hangman();
    // Hangman(string word);
    // ~Hangman();
    string get_word();
};

Hangman::Hangman()
{
    fstream wordlist(WORD_FILE);

    // get length of wordlist
    string line;
    int number_of_lines = 0;
    while (std::getline(wordlist, line)) {
        ++number_of_lines;
    }
    wordlist.clear();
    wordlist.seekg(0);


    // generate random number between 0 and length of word list
    // this will be the line number of the chosen word
    srand(time(NULL));
    int rand_num = rand() % (number_of_lines + 1);

    stringstream temp_word;
    for (int i = 0; i < rand_num; ++i)
        std::getline(wordlist, temp_word);

    wordlist.close();


    // strip word of punctuation
    remove_copy_if(temp_word.begin(), temp_word.end(),
                    std::back_inserter(this->word),
                    std::ptr_fun<int, int>(&std::ispunct)
                   );


    // convert case



    // set underscores for display word
    // char chosen_word[this->word.length()];
    // this->display_word = chosen_word;

    // for (int j = 0; j < this->word.length(); ++j) {
    //     this->display_word[j] = '_';
    //     cout << this->display_word[j];
    // }
    // cout << '\n';
}

#endif