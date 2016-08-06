# usr/bin/env python

import random
import unittest

from set_solver import SetSolver

# Standard set of card color, shape, fill, and number
attribs = {'colors': ['red', 'blue', 'yellow'],
           'shape':  ['circle', 'square', 'diamond'],
           'fill':   ['none', 'stripe', 'solid'],
           'number': [num for num in range(3)]}

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

class TestSolverActions(unittest.TestCase):

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

if __name__ == '__main__':
    unittest.main()
