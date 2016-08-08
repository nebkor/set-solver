# usr/bin/env python

import random
import unittest

from set_solver import SetSolver, Card


class TestConstructSolver(unittest.TestCase):

    def test_no_attribute_fail(self):
        ''' SetSolver should raise parameter error if made without
            attributes. '''

        self.assertRaises(TypeError, SetSolver)

    def test_with_attributes(self):
        ''' SetSolver should accept a dictionary of attributes.'''
        attribs = {'colors': ['red', 'blue', 'yellow'],
                   'shape':  ['circle', 'square', 'diamond'],
                   'fill':   ['none', 'stripe', 'solid'],
                   'number': [num for num in range(3)]}
        a_solver = SetSolver(attribs)
        self.assertIsNotNone(a_solver.attributes)

    def test_with_bad_attributes(self):
        ''' SetSolver should raise TypeError if passed malform attributes'''
        bad_len_attribs = {'colors': ['red', 'blue', 'yellow'],
                           'shape':  ['circle', 'square', 'diamond'],
                           'fill':   ['none', 'solid'],
                           'number': [num for num in range(3)]}
        attribs_not_list = {'colors': 'blue, red, green',
                            'number': [0, 1]
                           }
        self.assertRaises(TypeError, 
                          SetSolver, bad_len_attribs,
                          msg='Attributes are not equal in number.')
        self.assertRaises(TypeError, 
                          SetSolver, attribs_not_list,
                          msg='Attributes must be list.')


class TestSchemaActions(unittest.TestCase):

    def test_schema_creation(self):
        ''' Test scoring schema creation for varying hand sizes. '''

        two_hand   = {'colors': ['red', 'blue'],
                      'shape':  ['circle', 'square'],
                      'fill':   ['none', 'stripe'],
                      'number': ['one', 'two']}
        three_hand = {'colors': ['red', 'blue', 'yellow'],
                      'shape':  ['circle', 'square', 'diamond'],
                      'fill':   ['none', 'stripe', 'solid'],
                      'number': ['one', 'two', 'three']}
        four_hand  = {'colors': ['red', 'blue', 'yellow', 'green'],
                      'shape':  ['circle', 'square', 'diamond', 'oval'],
                      'fill':   ['none', 'stripe', 'solid', 'polkadot'],
                      'number': ['one', 'two', 'three', 'four']}
        
        # And some randomly generated n-dimensional Set game
        # the 'numbers' key is necessary for the SetSolver class 
        n = random.randrange(5, 11)
        n_hand = {key: [value for value in range(n)]
                  for key in range(n)}
        n_hand['number'] = [value for value in range(n)]

        two_set = SetSolver(two_hand)
        three_set = SetSolver(three_hand)
        four_set = SetSolver(four_hand)
        n_set = SetSolver(n_hand)

        self.assertIsNotNone(two_set.make_validation_schema())
        self.assertIsNotNone(three_set.make_validation_schema())
        self.assertIsNotNone(four_set.make_validation_schema())
        self.assertIsNotNone(n_set.make_validation_schema())

    def test_schema_validity(self):
        ''' Validate schema scoring for three, four, and five card games.'''
        three_hand = {'colors': ['red', 'blue', 'yellow'],
                      'shape':  ['circle', 'square', 'diamond'],
                      'fill':   ['none', 'stripe', 'solid'],
                      'number': ['one', 'two', 'three']}
        four_hand  = {'colors': ['red', 'blue', 'yellow', 'green'],
                      'shape':  ['circle', 'square', 'diamond', 'oval'],
                      'fill':   ['none', 'stripe', 'solid', 'polkadot'],
                      'number': ['one', 'two', 'three', 'four']}
        five_hand  = {'colors': ['red', 'blue', 'yellow', 'green', 'purple'],
                      'shape':  ['circle', 'square', 'diamond', 'oval', 'zig'],
                      'fill':   ['none', 'stripe', 'solid', 'polkadot', 'zag'],
                      'number': ['one', 'two', 'three', 'four', 'five']}

        valid_3    = {'colors': {'red': 1,
                                 'blue': 3,
                                 'yellow': 9},
                      'shape':  {'circle': 1,
                                 'square': 3,
                                 'diamond': 9},
                      'fill':   {'none': 1,
                                 'stripe': 3, 
                                 'solid': 9},
                      'number': {'one': 1,
                                 'two': 3,
                                 'three': 9},
                      'valid_scores': {3, 9, 27, 13} 
                     }

        valid_4    = {'colors': {'red': 1,
                                 'blue': 4,
                                 'yellow': 16,
                                 'green': 64},
                      'shape':  {'circle': 1,
                                 'square': 4,
                                 'diamond': 16,
                                 'oval': 64},
                      'fill':   {'none': 1,
                                 'stripe': 4,
                                 'solid': 16,
                                 'polkadot': 64},
                      'number': {'one': 1,
                                 'two': 4,
                                 'three': 16,
                                 'four': 64},
                      'valid_scores': {4, 16, 64, 256, 85}
                     }

        valid_5    = {'colors': {'red': 1,
                                 'blue': 5,
                                 'yellow': 25,
                                 'green': 125,
                                 'purple': 625}, 
                      'shape':  {'circle': 1,
                                 'square': 5, 
                                 'diamond': 25,
                                 'oval': 125,
                                 'zig': 625},
                      'fill':   {'none': 1,
                                 'stripe': 5, 
                                 'solid': 25,
                                 'polkadot': 125,
                                 'zag': 625},
                      'number': {'one': 1,
                                 'two': 5,
                                 'three': 25,
                                 'four': 125,
                                 'five': 625},
                      'valid_scores': {5, 25, 125, 625, 3125, 781}
                     }

        three_set = SetSolver(three_hand)
        four_set = SetSolver(four_hand)
        five_set = SetSolver(five_hand)
        self.assertDictEqual(three_set.make_validation_schema(), valid_3)
        self.assertDictEqual(four_set.make_validation_schema(), valid_4)
        self.assertDictEqual(five_set.make_validation_schema(), valid_5)


class TestConstructCard(unittest.TestCase):
    ''' Test Card class construction'''

    def test_no_attribute_fail(self):
        ''' SetSolver should raise parameter error if made without
            attributes. '''

        self.assertRaises(TypeError, Card)

    def test_random_attributes(self):
        ''' SetSolver should accept a dictionary of attributes.'''
        attribs = {'colors': ['red', 'blue', 'yellow'],
                   'shape':  ['circle', 'square', 'diamond'],
                   'fill':   ['none', 'stripe', 'solid'],
                   'number': ['one', 'two', 'three']}
        a_card = Card(attribs)
        self.assertIsNotNone(a_card.attributes)

    def test_assigned_attributes(self):
        ''' SetSolver should accept a dictionary of attributes.'''
        attribs = {'colors': 'red',
                   'shape': 'circle',
                   'fill': 'none',
                   'number': 'one'}
        a_card = Card(attribs)
        self.assertIsNotNone(a_card.attributes)

    def test_assigned_attributes_malformed(self):
        ''' SetSolver should accept a dictionary of attributes.'''
        attribs = {'colors': 1,
                   'shape': ['circle'],
                   'fill': 'none',
                   'number': 'one'}
        params = {'attributes': attribs, 'randomize': False}
        self.assertRaises(TypeError, Card, **params)


class TestSetChecking(unittest.TestCase):
    ''' Test SetSolver's check_for_set method. '''

    def test_wrong_size_hand(self):
        ''' Solver should throw TypeError if hand smaller or larger than 
            length of number attribute list. '''
        three_hand = {'colors': ['red', 'blue', 'yellow'],
                      'shape': ['circle', 'square', 'diamond'],
                      'fill': ['none', 'stripe', 'solid'],
                      'number': ['one', 'two', 'three']}

        too_small_hand = [Card(three_hand), Card(three_hand)]
        too_large_hand = [Card(three_hand), Card(three_hand), Card(three_hand), Card(three_hand)]
        three_solver = SetSolver(three_hand)

        self.assertRaises(TypeError, three_solver.check_for_set, too_small_hand)
        self.assertRaises(TypeError, three_solver.check_for_set, too_large_hand)

    def test_hands_with_set(self):
        three_hand = {'colors': ['red', 'blue', 'yellow'],
                      'shape': ['circle', 'square', 'diamond'],
                      'fill': ['none', 'stripe', 'solid'],
                      'number': ['one', 'two', 'three']}
        four_hand  = {'colors': ['red', 'blue', 'yellow', 'green'],
                      'shape':  ['circle', 'square', 'diamond', 'oval'],
                      'fill':   ['none', 'stripe', 'solid', 'polkadot'],
                      'number': ['one', 'two', 'three', 'four']}
        five_hand  = {'colors': ['red', 'blue', 'yellow', 'green', 'purple'],
                      'shape':  ['circle', 'square', 'diamond', 'oval', 'zig'],
                      'fill':   ['none', 'stripe', 'solid', 'polkadot', 'zag'],
                      'number': ['one', 'two', 'three', 'four', 'five']}

        # Instantiate some Cards
        card1 = Card({'colors': 'red', 'shape': 'circle', 'fill': 'none', 
                      'number': 'one'}, randomize=False)
        card2 = Card({'colors': 'blue', 'shape': 'square', 'fill': 'stripe', 
                      'number': 'two'}, randomize=False)
        card3 = Card({'colors': 'yellow', 'shape': 'diamond', 'fill': 'solid', 
                      'number': 'three'}, randomize=False)
        card4 = Card({'colors': 'green', 'shape': 'oval', 'fill': 'polkadot', 
                      'number': 'four'}, randomize=False)
        card5 = Card({'colors': 'purple', 'shape': 'zig', 'fill': 'zag', 
                      'number': 'five'}, randomize=False)

        three_solver = SetSolver(three_hand)
        four_solver = SetSolver(four_hand)
        five_solver = SetSolver(five_hand)
        self.assertTrue(three_solver.check_for_set([card1, card2, card3]))
        self.assertTrue(four_solver.check_for_set([card1, card2, card3, card4]))
        self.assertTrue(five_solver.check_for_set([card1, card2, card3, card4, card5]))

    def test_hands_without_set(self):
        three_hand = {'colors': ['red', 'blue', 'yellow'],
                      'shape': ['circle', 'square', 'diamond'],
                      'fill': ['none', 'stripe', 'solid'],
                      'number': ['one', 'two', 'three']}
        four_hand  = {'colors': ['red', 'blue', 'yellow', 'green'],
                      'shape':  ['circle', 'square', 'diamond', 'oval'],
                      'fill':   ['none', 'stripe', 'solid', 'polkadot'],
                      'number': ['one', 'two', 'three', 'four']}
        five_hand  = {'colors': ['red', 'blue', 'yellow', 'green', 'purple'],
                      'shape':  ['circle', 'square', 'diamond', 'oval', 'zig'],
                      'fill':   ['none', 'stripe', 'solid', 'polkadot', 'zag'],
                      'number': ['one', 'two', 'three', 'four', 'five']}

        # Instantiate some Cards
        card1 = Card({'colors': 'red', 'shape': 'circle', 'fill': 'none', 
                      'number': 'one'}, randomize=False)
        card2 = Card({'colors': 'blue', 'shape': 'square', 'fill': 'stripe', 
                      'number': 'two'}, randomize=False)
        card3 = Card({'colors': 'yellow', 'shape': 'diamond', 'fill': 'solid', 
                      'number': 'three'}, randomize=False)
        card4 = Card({'colors': 'green', 'shape': 'oval', 'fill': 'polkadot', 
                      'number': 'four'}, randomize=False)
        card5 = Card({'colors': 'purple', 'shape': 'zig', 'fill': 'zag', 
                      'number': 'five'}, randomize=False)

        three_solver = SetSolver(three_hand)
        four_solver = SetSolver(four_hand)
        five_solver = SetSolver(five_hand)
        self.assertFalse(three_solver.check_for_set([card1, card2, card1]))
        self.assertFalse(four_solver.check_for_set([card1, card2, card3, card1]))
        self.assertFalse(five_solver.check_for_set([card1, card2, card3, card4, card1]))

class TestGameChecking(unittest.TestCase):
    ''' Test SetSolver's ability to count total instances of sets
        in a given hand. '''

    def test_hand_two_sets(self):
        ''' Test 3, 4, 5 variable games with six cards and two sets. '''
        three_hand = {'colors': ['red', 'blue', 'yellow'],
                      'shape': ['circle', 'square', 'diamond'],
                      'fill': ['none', 'stripe', 'solid'],
                      'number': ['one', 'two', 'three']}
        four_hand  = {'colors': ['red', 'blue', 'yellow', 'green'],
                      'shape':  ['circle', 'square', 'diamond', 'oval'],
                      'fill':   ['none', 'stripe', 'solid', 'polkadot'],
                      'number': ['one', 'two', 'three', 'four']}
        five_hand  = {'colors': ['red', 'blue', 'yellow', 'green', 'purple'],
                      'shape':  ['circle', 'square', 'diamond', 'oval', 'zig'],
                      'fill':   ['none', 'stripe', 'solid', 'polkadot', 'zag'],
                      'number': ['one', 'two', 'three', 'four', 'five']}

        # Instantiate some Cards; fix the violation of PEP 8 later
        hollow_red_circle = Card({'colors': 'red', 'shape': 'circle', 'fill': 'none', 'number': 'one'}, randomize=False)
        two_hollow_blue_squares = Card({'colors': 'blue', 'shape': 'square', 'fill': 'stripe',  'number': 'two'}, randomize=False)
        three_solid_yellow_diamonds = Card({'colors': 'yellow', 'shape': 'diamond', 'fill': 'solid', 'number': 'three'}, randomize=False)
        four_polkadot_green_ovals = Card({'colors': 'green', 'shape': 'oval', 'fill': 'polkadot', 'number': 'four'}, randomize=False)
        five_purple_zag_zigs = Card({'colors': 'purple', 'shape': 'zig', 'fill': 'zag', 'number': 'five'}, randomize=False)

        three_hand_game = [hollow_red_circle, hollow_red_circle,
                           hollow_red_circle, two_hollow_blue_squares,
                           two_hollow_blue_squares, two_hollow_blue_squares]

        four_hand_game = [four_polkadot_green_ovals, four_polkadot_green_ovals,
                          four_polkadot_green_ovals, four_polkadot_green_ovals,
                          hollow_red_circle, hollow_red_circle, 
                          hollow_red_circle, hollow_red_circle]

        five_hand_game = [five_purple_zag_zigs, five_purple_zag_zigs,
                          five_purple_zag_zigs, five_purple_zag_zigs,
                          five_purple_zag_zigs, three_solid_yellow_diamonds,
                          three_solid_yellow_diamonds, 
                          three_solid_yellow_diamonds,
                          three_solid_yellow_diamonds,
                          three_solid_yellow_diamonds]
        
        three_solver = SetSolver(three_hand)
        four_solver = SetSolver(four_hand)
        five_solver = SetSolver(five_hand)

        # .find_all_sets returns a list of sets; just checking length for
        # number of sets in the list here.
        three_hand_sets = len(three_solver.find_all_sets(three_hand_game))
        four_hand_sets = len(four_solver.find_all_sets(four_hand_game))
        five_hand_sets = len(five_solver.find_all_sets(five_hand_game))
        self.assertEqual(three_hand_sets, 2)
        self.assertEqual(four_hand_sets, 2)
        self.assertEqual(five_hand_sets, 2)

class TestGameDealing(unittest.TestCase):
    ''' Test SetSolver's .deal_game method '''

    def test_with_default_attribs(self):
        ''' Create game with specified attributes. '''

        three_hand = {'colors': ['red', 'blue', 'yellow'],
                      'shape':  ['circle', 'square', 'diamond'],
                      'fill':   ['none', 'stripe', 'solid'],
                      'number': ['one', 'two', 'three']}

        three_solver = SetSolver(three_hand)
        hand = three_solver.deal_game(15)

        for card in hand:
            self.assertIsInstance(card, Card)

    def test_with_random_attribs(self):
        ''' Create game with randomized attributes. '''

        n = random.randrange(5, 11)
        n_hand = {key: [value for value in range(n)]
                  for key in range(n)}
        n_hand['number'] = [value for value in range(n)]

        n_solver = SetSolver(n_hand)
        hand = n_solver.deal_game(50)

        for card in hand:
            self.assertIsInstance(card, Card)

if __name__ == '__main__':
    unittest.main()
