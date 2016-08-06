# usr/bin/env python

attribs = {'colors': ['red', 'blue', 'yellow'],
           'shape':  ['circle', 'square', 'diamond'],
           'fill':   ['none', 'stripe', 'solid'],
           'number': [num for num in range(3)]}

class SetSolver(object):
    """docstring for SetSolver"""
    def __init__(self, attributes):
        super(SetSolver, self).__init__()
        self.attributes = self._check_attributes(attributes)
        return None

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

        return schema

