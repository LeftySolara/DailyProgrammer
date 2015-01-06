// [02/24/14] Challenge #149 [Easy] Disemvoweler
// http://www.reddit.com/r/dailyprogrammer/comments/1ystvb/022414_challenge_149_easy_disemvoweler/


#include <string>
using std::string;
#include <array>
using std::array;
#include <algorithm>
using std::remove;
#include <iostream>
using std::cin; using std::cout; using std::endl;

int main() {
    string mystring;
    size_t place;
    array<char,11> targets = {'a','e','i','o','u','A','E','I','O','U',' '};

    cout << "Enter a string:" << endl;
    getline(cin,mystring);

    for (auto elem : targets) {
        mystring.erase(remove(mystring.begin(),mystring.end(),elem),mystring.end());
    }
    cout << mystring << endl;

    return 0;
}