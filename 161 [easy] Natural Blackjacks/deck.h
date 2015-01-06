#include "card.h"
#include <utility>
using std::pair;
#include <ostream>
using std::ostream;

#ifndef __DECK_H_INCLUDED__
#define __DECK_H_INCLUDED__

class Deck {
    private:
        vector<Card> d;
    public:
        Deck();
        ~Deck();
        void shuffle();
        pair<Card,Card> deal();
        friend ostream &operator<<(ostream &out, const Deck &deck);
        friend void deal_hands(vector<Deck> &decks, vector<pair<Card,Card>> &hands, double &count, double &delt);
};

#endif