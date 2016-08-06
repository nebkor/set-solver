# A Solver for Set

A simple class that solves games of set in N-dimensions, with unit tests.

## Testing for a set based on attribute score

The rules of the game are such that a set is considered a set if each card in it either has attributes (color, shape, fill, whatever) that are either all the same or contain one of each possibility. To test for this in a quick and dirty way, you could keep a running total of attributes on each card for each combination and then loop through them, tallying what was there and what was not, and returning a True or a False at the end of the last loop. That seems like a lot of loops. Or, in Python, you could do a hacky len(set([attribute, for, cards, in, hand])), but that would require looping through each hand of cards at least one time to build the list of the attributes, and then through each of those lists again to make a set, and then checking the length of the set. If that were equal to one or the number of possiblities, the hand would be valid for that attribute.

I wanted to find a way to mathematically calculate whether a hand was a set. If only three variations are possible, you could assign them values of -1, 0, 1, and simply tally their value to see if a hand were valid: -3, 0, and 3 are the only possible tallies for valid sets. But with more possibilities, this clearly will not work: I needed to find a way to assign values that would preclude false positives. 

After thinking for a while, I hit upon exponentiation. The valid numbers need to be at least as far away from each other as there possible variants. So, for three possibilities, you assign values to each according to n^i, where n the number of variations and i is the index of each variant. If red, blue, and yellow are the possible colors, their values are 1, 3, and 9, respectively, and the possible values for valid hands are 3 for all red, 9 for all blue, 27 for all yellow, and 13 for one of each.

In this way, you can build a function that "consumes" each combination of cards possible for a hand, and keeps a running tally of attribute scores. Those numbers tell whether a hand is valid after the combination has been made, without reference to the attributes of individual cards.

Killer.