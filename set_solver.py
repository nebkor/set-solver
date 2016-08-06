# usr/bin/env python


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
        for items in attributes.values():
            if not isinstance(items, list): 
                raise TypeError('Attributes must be list.')
            elif not len(items) == possibilities:
                raise TypeError('Attributes are not equal in number.')

        return attributes

