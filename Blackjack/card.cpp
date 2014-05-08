#include "card.h"
#include <string>
using std::string;
#include <iostream>
using std::cin; using std::cout; using std::endl;

ostream &operator<<(ostream &out, const Card &c) {
    string card_suit, card_rank;
    switch (c.s) {
        case SPADES:
            card_suit = "Spades";
            break;
        case CLUBS:
            card_suit = "Clubs";
            break;
        case HEARTS:
            card_suit = "Hearts";
            break;
        case DIAMONDS:
            card_suit = "Diamonds";
            break;
        default:
            card_suit = "No suit";
    }
    switch (c.r) {
        case 1:
            card_rank = "Ace";
            break;
        case 11:
            card_rank = "Jack";
            break;
        case 12:
            card_rank = "Queen";
            break;
        case 13:
            card_rank = "King";
            break;
        default:
            out << c.r << " of " << card_suit << endl;
            return out;
    }
    out << card_rank << " of " << card_suit << endl;
    return out;
}