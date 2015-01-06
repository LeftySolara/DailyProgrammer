// Blackjack Simulator
// finds percentage of natural blackjacks delt

#include "deck.h"
#include "card.h"
#include <vector>
using std::vector;
#include <time.h>
#include <cstdlib>
#include <thread>
using std::this_thread::sleep_for;
#include <chrono>
using std::chrono::seconds;
#include <utility>
using std::pair;
#include <iostream>
using std::cin; using std::cout; using std::endl;


void shuffle_decks(int num, vector<Deck> &v) {
    for (int i = 0; i < num; i++) {
        Deck d;
        sleep_for(seconds(2));
        d.shuffle();
        v.push_back(d);
    }
}

void print_decks(vector<Deck> &v) {
    for (Deck d : v) {
        cout << d << endl;
    }
}

void deal_hands(vector<Deck> &decks, vector<pair<Card,Card>> &hands, double &count, double &delt) {
    pair<Card,Card> hand;
    int rank1, rank2;
    for (int i = 0; i < decks.size(); i++) {
        while (decks[i].d.size() > 0) {
            hand = decks[i].deal();
            hands.push_back(hand);
            ++delt;
            rank1 = hand.first.rank();
            rank2 = hand.second.rank();
    
            if (rank1 > 10) { rank1 = 10; }
            else if (rank1 == 1) { rank1 = 11; }

            if (rank2 > 10) { rank2 = 10; }
            else if (rank2 == 1) { rank2 = 11; }

            if (rank1 + rank2 == 21) { ++count; }
        }
    }
}

void print_hands(vector<pair<Card,Card>> v) {
    for (pair<Card,Card> p : v) {
        cout << p.first;
        cout << p.second;
        cout << endl;
    }
}

int main() {
    int num;
    double delt = 0, count = 0;
    vector<Deck> decks;
    vector<pair<Card,Card>> hands;
    cout << "Enter number of decks: ";
    cin >> num;
    cout << endl;
    shuffle_decks(num, decks);
    // print_decks(decks);
    deal_hands(decks, hands, count, delt);
    print_hands(hands);
    cout << endl;
    cout << "After " << delt << " hands there were " << count << " blackjacks at "
    << (count / delt) * 100 << "%" << endl;

    return 0;
}