#include <ostream>
using std::ostream;
#include <vector>
using std::vector;
#include <utility>
using std::pair;

#ifndef __CARD_H_INCLUDED__
#define __CARD_H_INCLUDED__

enum suit {SPADES, CLUBS, HEARTS, DIAMONDS};

class Card {
    private:
        int r;
        suit s;
    public:
        Card() {this->r = 1; this->s = SPADES;};
        Card(int card_rank, suit card_suit) {this->r = card_rank; this->s = card_suit;};
        int rank() {return r;};
        friend ostream &operator<<(ostream &out, const Card &c);
};

#endif