#Slide 1

Operators

#Slide 2

## Numeric Operators

### Unary Operators

#### - (negate)

Get the negated value of a value

    -x

Examples:

    >>> -1
    -1
    >>> -2.0
    -2.0

#### + (unchange)

Get the unchanged value of a value

    +x

Examples:

    >>> +1
    1
    >>> +2.0
    2.0

NOTE: There might be some use cases where this is needed but most of the time
this operator is unnecessary.

You can actually use both on a single value at the same time

    >>> +-2
    -2
    >>> -+2
    -2


### Binary Operators

#### + (addition)

Get the sum of two operands

    x + y

Examples

    >>> 1 + 2
    3
    >>> 1.0 + 2.2
    3.2
    >>> 1 + (-2)
    -1
    >>> 1.0 + 2 # int + float = float
    3.0

#### - (subtraction)

Get the difference of two operands

    x - y

Examples

    >>> 3 - 4
    -1
    >>> 3 - (-4)
    7
    >>> 5.0 - 2.9
    2.1
    >>> 7.0 - 9 # int - float = float
    -2.0

#### * (multiplication)

Get the product of two operands

    x * y

Examples

    >>> 2 * 3
    6
    >>> 3 * (-4)
    -12
    >>> 5.0 * 1.5
    7.5
    >>>  2.0 * 5 # int * float = float
    10.0

#### / (division)

Get the quotient of two operands

    x / y

Examples

    >>> 4 / 2
    2
    >>> 20 / -5
    -4
    >>> 1.0 / 2.0
    0.5
    >>> 1.0 / 2 # int / float = float
    0.5
    >>> 1 / 2 # ???
    0
    
If either operand is a float, classic division is performed
If both operands are of type int, floor division is performed

#### // (floor division)

Get the floored quotient of two operands

    x // y

Examples

    >>> 4 // 2
    2
    >>> 20 // -5
    -4
    >>> 1.0 // 2.0
    0.0
    >>> 1.0 // 2
    0.0
    >>> 1 // 2
    0


#### ** (exponentiation)

Get the exponent

    x ** y

Examples

    >>> 2 ** 2
    4
    >>> 2 ** -2
    0.25
    >>> 3.0 ** 2.0
    9.0
    >>> 3.0 ** 2
    9.0
    >>> -3.0 ** 2
    -9.0
    >>> -3.0 ** -2
    -0.11111111111111
