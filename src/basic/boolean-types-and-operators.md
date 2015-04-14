# Boolean Values

    >>> True
    True
    >>> False
    False

# Boolean/Logical Operators

## not

    >>> not True
    False
    >>> not False
    True

## and

    >>> True and True
    True
    >>> True and False
    False
    >>> False and True
    False
    >>> False and False
    False

Tip: As long as one of the operands is False, the result will be False

## or

    >>> True or True
    True
    >>> True or False
    True
    >>> False or True
    True
    >>> False or False
    False

Tip: As long as one of the operands is True, the result will be True

# Relational Operators

## Equal To
    
    >>> 100 == 100
    True
    >>> 100 == 50
    False
    >>> -100 == 100
    False
    >>> 100 == True
    False

# Not Equal To

    >>> 100 != 100
    False
    >>> 100 != 50
    True
    >>> -100 != 100
    True
    >>> 100 != True
    True

## Greater Than / Greater Than Equal To

    >>> 5 > 10
    False
    >>> 10 > 5
    True
    >>> 5 > 5
    False
    >>> 5 >= 5
    True

## Less Than

    >>> 5 < 10
    True
    >>> 10 < 5
    False
    >>> 5 < 5
    False
    >>> 5 <= 5
    True

# Trivia!

Any nonzero number is interpreted as "true"

    >>> 17 and True
    True

This flexibility can be useful, but there are some subtleties to it that might be confusing. You might want to avoid it (unless you know what you are doing).

    >>> 0 and True
    0
    >>> 1 > True
    False
