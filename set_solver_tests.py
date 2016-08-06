# usr/bin/env python

import unittest

from set_solver import SetSolver

# Standard set of card color, shape, fill, and number
attribs = {'colors': ['red', 'blue', 'yellow'],
           'shape':  ['circle', 'square', 'diamond'],
           'fill':   ['none', 'stripe', 'solid'],
           'number': [range(3)]}

class TestConstructSolver(unittest.TestCase):

    def test_no_attribute_fail(self):
        ''' SetSolver should raise parameter error if made without
            attributes. '''

        self.assertRaises(TypeError, SetSolver)

    def test_with_attributes(self):
        ''' SetSolver should accept a dictionary of attributes.'''
        a_solver = SetSolver(attribs)
        self.assertIsNotNone(a_solver.attributes)

    def test_with_bad_attributes(self):
        ''' SetSolver should raise TypeError if passed malform attributes'''
        pass




if __name__ == '__main__':
    unittest.main()
