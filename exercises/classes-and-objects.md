# Classes and Objects Exercises

Requirements: Using global variables in solving these problems is NOT allowed. 

### CountLeObject

Create a class `CountLeObject`. Then output the current number of objects 
of that class that was instantiated.

    a = CountLeObject()
    print CountLeObject.ctr # 1
    
    b = CountLeObject()
    c = CountLeObject()
    print CountLeObject.ctr # 3

### Simple Calculator 

Create a simple calculator class that does something below

    c = new Calculator(5)
    c.add(1)
    c.subtract(2)
    c.multiply(3)
    c.divide(4)
    c.get_result() # The answer should be 3

### Phonebook

Create 2 classes `Phonebook` and `Contact`. The `Contact` class should hold the name and phone number. The `Phonebook`
should hold a list of contacts. Define these methods in `Phonebook`:

- A method that adds an entry to the contact list. The argument should be a dictionary with name and phone number
- A method that removes an entry from the contact list based on the number
- A method that gets an entry from a contact list based on the number
- A method that prints out a list of all the contact entries

### BDO(Bangko Dhens Oro)

### Poker Hand

1. Define 3 classes, `Deck`, `Card` and `Player` which represents a deck of cards, an individual card and a player
respectively. The classes should be modeled like it's real world counterpart(a deck is composed of 52 cards, a card
has a number and a club, a player has a name, etc)

2. Define a method for `Deck` named `deal_poker_hands` that:
- accepts the number of players. The number of players should be 2 minimum, 8 maximum. If invalid number is passed,
the function should print a message that says that the number is invalid instead of processing it.
- returns a list of players with 2 random Card objects assigned to it. No two or more players should have the same card.

NOTE: To generate a random from a specific range, add this code at the top of your file

    import random
    
then use this method to generate random numbers

    random.randrange(1,10) # Get a random number between 1 to 10
    
<img src="http://sd.keepcalm-o-matic.co.uk/i/good-luck-have-fun-10.png" alt="Good Luck and Have Fun!" style="text-align: center" />
