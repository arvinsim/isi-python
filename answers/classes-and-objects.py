#====================================================================================================
# CountLeObject
#====================================================================================================
class CountLeObject(object):
    ctr = 0

    def __init__(self):
        CountLeObject.ctr += 1

a = CountLeObject()
print CountLeObject.ctr

b = CountLeObject()
c = CountLeObject()
print CountLeObject.ctr

#====================================================================================================
# Calculator
#====================================================================================================
class Calculator(object):

    def __init__(self, operand):
        self.current_value = operand

    def add(self, operand):
        self.current_value += operand

    def subtract(self, operand):
        self.current_value -= operand

    def multiply(self, operand):
        self.current_value *= operand

    def divide(self, operand):
        self.current_value /= operand

    def get_result(self):
        return self.current_value

c = Calculator(5)
c.add(1)
c.subtract(2)
c.multiply(3)
c.divide(4)
print c.get_result()  # The answer should be 3

#====================================================================================================
# Phonebook
#====================================================================================================

class Contact(object):
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number


class Phonebook(object):
    def __init__(self):
        self.contacts = []

    def add_entry(self, name, phone_number):
        for contact in self.contacts:
            if contact.phone_number == phone_number:
                print "Duplicate Phone Number!"
                return

        new_contact = Contact(name, phone_number)
        self.contacts.append(new_contact)

    def get_entry(self, phone_number):
        for contact in self.contacts:
            if contact.phone_number == phone_number:
                return contact

    def remove_entry(self, phone_number):
        index_to_delete = None
        for index, contact in enumerate(self.contacts):
            if contact.phone_number == phone_number:
                index_to_delete = index
                break
        self.contacts.pop(index_to_delete)

    def get_entries(self):
        entries = """
=========================
CONTACT LIST
=========================
        """
        for contact in self.contacts:
            entries += """
Name: {}
Phone Number: {}
-------------------------
            """.format(contact.name, contact.phone_number)
        return entries


p = Phonebook()
p.add_entry('Jowy', '111111')
p.add_entry('Nanami', '33333')
p.add_entry('Riou', '222222')

print p.get_entries()

nanami = p.get_entry('33333')
print nanami.name
p.remove_entry('33333')
nanami = p.get_entry('33333')
print nanami

print p.get_entries()

# ====================================================================================================
# Poker Hands
# ====================================================================================================

class Player(object):
    def __init__(self):
        self.hand = []


class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __repr__(self):
        return "Suit: {}, Rank: {}".format(self.suit, self.rank)

class Deck(object):
    def __init__(self):
        self.cards = []
        for rank in range(1, 14):
            if rank == 1:
                rank = "Ace"
            if rank == 11:
                rank = "Jack"
            if rank == 12:
                rank = "Queen"
            if rank == 13:
                rank = "King"

            for suit in ['Spades', 'Hearts', 'Diamonds', 'Clubs']:
                self.cards.append(Card(suit, rank))

    # TODO
    def deal_poker_hands(self, number):
        if number < 2 and number > 8:
            print "Invalid number was passed!"
            return

d = Deck()






