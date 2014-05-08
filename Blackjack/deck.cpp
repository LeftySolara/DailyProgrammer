#include "deck.h"
#include <algorithm>
using std::random_shuffle;

Deck::Deck() {
    for (int i = 1; i < 14; i++) {
        Card club(i,CLUBS);
        Card spade(i,SPADES);
        Card heart(i,HEARTS);
        Card diamond(i,DIAMONDS);

        d.push_back(club);
        d.push_back(spade);
        d.push_back(heart);
        d.push_back(diamond);
    }
}

Deck::~Deck() {
    d.clear();
}

void Deck::shuffle() {
    srand(time(0));
    random_shuffle(d.begin(),d.end());
}

pair<Card,Card> Deck::deal() {
    pair<Card,Card> hand;
    hand.first = d[0];
    hand.second = d[1];
    d.erase(d.begin());
    d.erase(d.begin());
    return hand;
}

ostream &operator<<(ostream &out, const Deck &deck) {
    for (Card c : deck.d) {
        out << c;
    }
    return out;
}