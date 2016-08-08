# usr/bin/env python3

from set_solver import SetSolver, Card

#  _______  _______  _______    _______  _______  __   __  _______ 
# |       ||       ||       |  |       ||   _   ||  |_|  ||       |
# |  _____||    ___||_     _|  |    ___||  |_|  ||       ||    ___|
# | |_____ |   |___   |   |    |   | __ |       ||       ||   |___ 
# |_____  ||    ___|  |   |    |   ||  ||       ||       ||    ___|
#  _____| ||   |___   |   |    |   |_| ||   _   || ||_|| ||   |___ 
# |_______||_______|  |___|    |_______||__| |__||_|   |_||_______|
#      _______  _______  ___      __   __  _______  ______    __   
#     |       ||       ||   |    |  | |  ||       ||    _ |  |  |  
#     |  _____||   _   ||   |    |  |_|  ||    ___||   | ||  |  |  
#     | |_____ |  | |  ||   |    |       ||   |___ |   |_||_ |  |  
#     |_____  ||  |_|  ||   |___ |       ||    ___||    __  ||__|  
#      _____| ||       ||       | |     | |   |___ |   |  | | __   
#     |_______||_______||_______|  |___|  |_______||___|  |_||__|  
#
# Play a game of Set by instantiating a Solver with either the preset
# card attributes, or with randomly generated ones:
#
#    solver = SetSolver(attributes=attributes)
#    game = solver.deal_game(num_of_cards=24)
#    all_sets = solver.find_all_sets(game)
#    print(all_sets)

# I've included some basic card attributes for 3, 4, and 5 variant games.
# The function get_random_attribs will make an attribute dictionary with
# the passed parameter depth:

#    n_depth_attributes = get_random_attribs(depth=n)
def get_random_attributes(depth):
    ''' Return randomized attribute dictionary of requested depth.'''
    n_hand = {key: [value for value in range(depth)]
              for key in range(depth)}
    n_hand['number'] = [value for value in range(depth)]
    return n_hand


def main():
    print('''Play a game of Set by instantiating a Solver with either the preset
card attributes, or with randomly generated ones:

   solver = SetSolver(attributes=attributes)
   game = solver.deal_game(num_of_cards=24)
   all_sets = solver.find_all_sets(game)
   print(all_sets)

I've included some basic card attributes for 3, 4, and 5 variant games.
The function get_random_attribs will make an attribute dictionary with
the passed parameter depth:

   n_depth_attributes = get_random_attributes(depth=n)

Preloaded solvers are three_solver, four_solver, five_solver.

HAVE FUN.''')


# Preloaded attributes
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

three_solver = SetSolver(three_hand)
four_solver = SetSolver(four_hand)
five_solver = SetSolver(five_hand)

if __name__ == '__main__':
    main()