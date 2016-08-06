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


class TestSetChecking(unittest.TestCase):
    ''' Test SetSolver's check_for_set method. '''

    def test_wrong_size_hand(self):
        ''' Solver should throw TypeError if hand smaller or larger than 
            length of number attribute list. '''
        three_hand = {'colors': ['red', 'blue', 'yellow'],
                      'shape': ['circle', 'square', 'diamond'],
                      'fill': ['none', 'stripe', 'solid'],
                      'number': ['one', 'two', 'three']}

        # replace with list of cards when card class done
        too_small_hand = [Card(three_hand), Card(three_hand)]
        too_large_hand = [Card(three_hand), Card(three_hand), Card(three_hand), Card(three_hand)]
        three_solver = SetSolver(three_hand)

        self.assertRaises(TypeError, three_solver.check_for_set, too_small_hand)
        self.assertRaises(TypeError, three_solver.check_for_set, too_large_hand)


if __name__ == '__main__':
    unittest.main()
