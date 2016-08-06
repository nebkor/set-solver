# usr/bin/env python

attribs = {'colors': ['red', 'blue', 'yellow'],
           'shape':  ['circle', 'square', 'diamond'],
           'fill':   ['none', 'stripe', 'solid'],
           'number': ['one', 'two', 'three']}


class SetSolver(object):
    """ Class that solves for number of sets in a hand of Set. 
        :param attributes: is a dictionary of dictionaries of list, top level
        keyed to attributes like 'color' or 'number'. Attribute lists must 
        all be the same length. 'number' is a required attribute. """
    def __init__(self, attributes):
        super(SetSolver, self).__init__()
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

    def check_for_set(self, list_of_cards):
        ''' Check for combination of cards to see if it is a set. '''

        if not len(list_of_cards) == len(self.attributes['number']):
            raise TypeError('Number of cards not equal to number of variations')
        

