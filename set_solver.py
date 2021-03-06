# usr/bin/env python

import random
from itertools import combinations


ATTRIBS = {'colors': ['red', 'blue', 'yellow'],
           'shape':  ['circle', 'square', 'diamond'],
           'fill':   ['none', 'stripe', 'solid'],
           'number': ['one', 'two', 'three']}


class Deck(object):
    '''Stateful representation of a Set deck.'''
    def __init__(self, size=81, attribs=ATTRIBS, shuffle=True):
        self.size = size
        self.attribs = attribs
        self.cards = self._make_deck()
        if shuffle:
            random.shuffle(self.cards)
        else:
            pass

    def _make_deck(self):
        return []

    def deal(self, num_cards=3):
        "Returns a list of num_cards cards."
        try:
            ret = self.cards[0:num_cards]
            self.cards = self.cards[num_cards:]
            return ret
        except:
            raise "empty"

    def size(self):
        return len(self.cards)

class Game(object):
    '''Class to represent a game of Set, comprising a deck and
       a number of dealt cards.'''
    def __init__(self, num_cards=12, deck=None):
        if deck == None:
            self.deck = Deck()
        else:
            self.deck = deck
        self.visible = self.deck.deal(numcards)
        self.num_cards = num_cards

    def check(self, pset):
        if is_valid(pset):
            # remove the cards in pset from the visible state,
            # and deal three cards from the deck to the visible state
            for card in pset:
                self.visible.remove(card)
            if self.deck.size() > 2:
                self.visible.append(self.deck.deal(3))
            else:
                print "Deck is empty."
            return True
        else:
            # don't do anything if the proposed set is not valid
            return False


class SetSolver(object):
    ''' Class that solves for number of sets in a hand of Set.
        :param attributes: is a dictionary of dictionaries of list, top level
        keyed to attributes like 'color' or 'number'. Attribute lists must
        all be the same length. 'number' is a required attribute. '''
    def __init__(self, attributes):
        self.attributes = self._check_attributes(attributes)
        self.schema = self.make_validation_schema(attributes)
        return

    def _check_attributes(self, attributes):
        ''' Ensure attributes is a dict of lists of equal length. '''
        if not isinstance(attributes, dict):
            raise TypeError('Pass a dictionary of lists of attributes')

        possibilities = len(attributes['number'])
        for types in attributes.values():
            if not isinstance(types, list):
                raise TypeError('Attributes must be list.')
            elif not len(types) == possibilities:
                raise TypeError('Attributes are not equal in number.')

        return attributes

    def make_validation_schema(self, attributes=None):
        ''' Create a validation schema for calculating valid hands.'''

        # Default to instance attributes
        if not attributes:
            attributes = self.attributes

        # Hand scoring schema will be a dict of dicts, mapping to ints
        # that calculated based on the number of possible variations
        # for each attribute: number_of_attribs ^ attrib_index
        schema = dict()
        size_of_hand = len(attributes['number'])

        for attribute, variations in attributes.items():
            schema[attribute] = {variation: pow(size_of_hand, exponent)
                                 for exponent, variation
                                 in enumerate(variations)}

        # Valid hands will be those that have one of each possible variation,
        # or all of the same kind. With the scoring
        # schema above for a 3 card game, the values for variations are
        # 1, 3, 9. Winning hands would have scores of 3, 9, 27, or 13--
        # all 1s, 3s, 9s, or one of each--for each attribute. This can be
        # generalized as a set of ints from size_of_hand ** 2 to
        # size_of_hand ** (size_of_hand + 1), plus the sum of the score for
        # each attribute.
        schema['valid_scores'] = {pow(size_of_hand, exp)
                                  for exp in range(1, size_of_hand + 1)}
        schema['valid_scores'].add(sum(pow(size_of_hand, exp)
                                       for exp in range(size_of_hand)))

        return schema

    def check_for_set(self, hand):
        ''' Check hand of cards to see if it is a set. '''

        if not len(hand) == len(self.attributes['number']):
            raise TypeError('Hand size must equal possible variations.')

        # Loop through cards and build a score for each attribute, card by
        # card. If by some mishap cards do not share the SetSolver's attributes
        # here, a KeyError will be thrown.
        hand_score = {attribute: 0 for attribute in self.attributes.keys()}
        for card in hand:
            for attribute in self.attributes.keys():
                card_variation = card.attributes[attribute]
                hand_score[attribute] += self.schema[attribute][card_variation]

        for score in hand_score.values():
            if not score in self.schema['valid_scores']:
                return False
        else:
            return True

    def find_all_sets(self, cards):
        ''' Given a number of cards, find all possible sets. '''
        sets = []
        for hand in combinations(cards, len(self.attributes['number'])):
            if self.check_for_set(hand):
                sets.append(hand)
        return sets

    def print_cards(self, cards):
        ''' Given iterable of cards, print their attributes. '''
        for card in cards:
            print(str(card))
        return

    def deal_game(self, num_to_deal):
        ''' Create a game by randomly generating num_to_deal cards.
            Attributes for cards from self.attributes. '''
        return [Card(self.attributes) for card in range(num_to_deal)]


class Card(object):
    ''' Stores card attributes. Takes attribute dict from SetSolver. If
        randomized, arbitrarily chooses one attribute from each.'''
    def __init__(self, attributes, randomize=True):
        self.attributes = self._parse_attribs(attributes, randomize)

    def __repr__(self):
        repr_str = ['< Card:']
        for attribute, value in self.attributes.items():
            repr_str.append('{}: {};'.format(attribute, value))
        repr_str.append('>')
        return ' '.join(repr_str)

    def __str__(self):
        header = 'Card:\n'
        card_attribs = '\n'.join('{}: {}'.format(attribute, value) for attribute, value in self.attributes.items())
        return header + card_attribs

    def _parse_attribs(self, attributes, randomize):
        ''' '''
        if randomize:
            return {attribute: random.choice(values)
                    for attribute, values in attributes.items()}

        else:
            # Check to make sure non-randomized cards have single variant
            for variant in attributes.values():
                if not isinstance(variant, str):
                    raise TypeError('Card attributes must be strings.')

            return attributes
