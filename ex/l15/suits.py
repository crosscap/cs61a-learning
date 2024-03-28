def list_demos():
    suits = ['coin', 'string', 'myriad']  # A list literal
    original_suits = suits
    suits.pop()             # Removes and returns the final element
    suits.remove('string')  # Removes the first element that equals the argument
    suits.append('cup')              # Add an element to the end
    suits.extend(['sword', 'club'])  # Add all elements of a list to the end
    suits[2] = 'spade'  # Replace an element
    suits
    suits[0:2] = ['heart', 'diamond']  # Replace a slice
    original_suits
    [suit.upper() for suit in suits]
    [suit[1:4] for suit in suits if len(suit) == 5]

