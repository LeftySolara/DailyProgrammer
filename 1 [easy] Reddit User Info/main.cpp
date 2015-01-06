#include <iostream>
#include <fstream>
#include <string>

using std::cin; using std::cout; using std::endl;
using std::string;
using std::ofstream;

void get_info(string& name, string& username, int& age) {
    // prompts user for reddit info
    cout << "What's your name?" << endl;
    cin >> name;
    cout << "What's your username?" << endl;
    cin >> username;
    cout << "How old are you?" << endl;
    cin >> age;
}

void show_info(string& name, string& username, int& age) {
    cout << "Your name is " << name << endl;
    cout << "Your reddit handle is " << username << endl;
    cout << "You are " << age << " years old" << endl;
    cout << "" << endl;
}

void write_info(string& name, string& username, int& age) {
    ofstream myfile ("reddit_users.txt",ofstream::app);
    myfile << name << "   " << username << "   " << age << endl;
    myfile.close();
}

int main()
{
    string name, username;
    int age = 0;

    get_info(name,username,age);
    show_info(name,username,age);
    write_info(name,username,age);

    return 0;
}