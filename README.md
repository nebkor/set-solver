```
 _______  _______  _______    _______  _______  __   __  _______ 
|       ||       ||       |  |       ||   _   ||  |_|  ||       |
|  _____||    ___||_     _|  |    ___||  |_|  ||       ||    ___|
| |_____ |   |___   |   |    |   | __ |       ||       ||   |___ 
|_____  ||    ___|  |   |    |   ||  ||       ||       ||    ___|
 _____| ||   |___   |   |    |   |_| ||   _   || ||_|| ||   |___ 
|_______||_______|  |___|    |_______||__| |__||_|   |_||_______|
     _______  _______  ___      __   __  _______  ______    __   
    |       ||       ||   |    |  | |  ||       ||    _ |  |  |  
    |  _____||   _   ||   |    |  |_|  ||    ___||   | ||  |  |  
    | |_____ |  | |  ||   |    |       ||   |___ |   |_||_ |  |  
    |_____  ||  |_|  ||   |___ |       ||    ___||    __  ||__|  
     _____| ||       ||       | |     | |   |___ |   |  | | __   
    |_______||_______||_______|  |___|  |_______||___|  |_||__|  
```
A simple class that solves games of Set in N-dimensions, with unittests used to track functionality. Try it out:

```
    python3 -i play_set.py
```

The rules of [Set](https://en.wikipedia.org/wiki/Set_(game)) are simple, but hard to explain: given a group of cards showing various numbers, shapes, and colors, select groups that either have one of each variance or are all the same. That is, given three possible variations for each attribute&mdash;say color, shape, fill, and number&mdash;a set will display either all the same or one of each color, shape, etc.

## Mathematically Determining Sets

So long as you play by the rules that a Set must be made up of as many cards as there are possible attributes, you can use math to determine if a given group of cards is a set. Given a list of possible variants for an attribute, assign each variant a numerical "score" equal to n<sup>i</sup>, where _n_ is the length of the list, and _i_ is the index of the variant. For a three variant list of shapes, ['circle', 'square', 'triangle'], circles recieve 1 point (3<sup>0</sup>), squares 3 (3<sup>1</sup>), and triangles 9 (3<sup>2</sup>). With three possible shapes, there four ways to make a set: 3 circles, 3 squares, 3 triangles, or 1 of each. These possible sets are worth 3, 9, 27, and 13 points respectively, and because of the way that the math works out, using only three cards, those four combinations are the only way to tally to a winning score for shape. If squiggles are added to the shape possibilities, scores for each shape would be 4<sup>i</sup>, or 1, 4, 16, and 64, and possible winning scores would be 4, 16, 64, 256, and 85. And so on for 5 and more attributes.

This means that determining if a combination of cards is a Set is simply tallying scores for each attribute and checking if they are in the set (the Python datatype) of acceptable combinations. Simpler than a bunch of nested loops. For large numbers of cards with many attributes, things still get slow.

## How SetSolver Implements This

The SetSolver class requires an `attributes` parameter when it is instantiated, which it uses to build a instance schema to tally scores for hands of cards. The `attributes` must be a dictionary of dictionaries of lists; the lists must be of equal lengths, and one of the attribute dictionaries must be keyed to `number`. This will work:
```
    five_hand = {'colors': ['red', 'blue', 'yellow', 'green', 'purple'],
                 'shape':  ['circle', 'square', 'diamond', 'oval', 'zig'],
                 'fill':   ['none', 'stripe', 'solid', 'polkadot', 'zag'],
                 'number': ['one', 'two', 'three', 'four', 'five']}
```
but so will this:
```
    n = random.randrange(5, 11)
    n_hand = {key: [value for value in range(n)]
              for key in range(n)}
    n_hand['number'] = [value for value in range(n)]
```
so long as you include the `number` dict.

The same dictionary can be used to instantiate Cards, iterables of which SetSolver will consume and verify as Sets. The Card class can be randomized on creation, randomly choosing one variant from each attribute. Shuffle and deal a game like so:
```
    a_12_card_game = [Card(attributes=five_hand) for card in range(12)]  
```
or make a specific card like this:
```
    a_single_polkadot_yellow_triangle = Card({'colors': ['yellow'], 'shape': ['triangle'], 'fill': ['polkadot'], 'number': ['one']}, randomize=False)
```


## Unittests

The set_solver_tests.py file has unittests covering the majority of the intended funcitonality. 
