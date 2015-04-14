##  Numeric Types

Let us start with numbers. In Python, there are 4 types of numbers.

### Integers

#### Plain integers
Plain integers(also just called integers) have 32 bits of precision (sys.maxint is always set to the maximum plain integer value for the current platform, the minimum value is -sys.maxint - 1). NOTE: This is equivalent to `long` in C.

    >>> 0
    0
    >>> 1337
    1337
    >>> 108128387187
    108128387187
    >>> -10
    -10
    >>> 1,000,000 # WARNING: This is NOT an integer
    (1, 0, 0)

#### Long integers

Long integers have unlimited precision. NOTE: This is equivalent to `double` in C.

    >>> 231856456374891984564987987
    231856456374891984564987987
    >>> -6854567498198469819564
    -6854567498198469819564

### Float

Numbers with a decimal point belong to a type called float, because these numbers are represented in a format called floating-point. 

    >>> 1.2
    1.2
    >>> 1000.15687
    1000.15687
    >>> 1.2e+2
    120.0
    >>> -6854567498198469819564.5
    -6.85456749819847e+21
    >>> 123456789.987654321
    123456789.98765433
    
Did you notice something odd?

### A Brief Explanation about Floating Point Numbers

Floating-point numbers are represented in computer hardware as base 2 (binary) fractions. For example, the decimal fraction

    0.125

Unfortunately, most decimal fractions cannot be represented exactly as binary fractions. A consequence is that, in general, the decimal floating-point numbers you enter are only approximated by the binary floating-point numbers actually stored in the machine.

The problem is easier to understand at first in base 10. Consider the fraction 1/3. You can approximate that as a base 10 fraction:

    0.3

or, better,

    0.33

or, better,

    0.333

and so on. No matter how many digits you’re willing to write down, the result will never be exactly 1/3, but will be an increasingly better approximation of 1/3.

It’s easy to forget that the stored value is an approximation to the original decimal fraction, because of the way that floats are displayed at the interpreter prompt. Python only prints a decimal approximation to the true decimal value of the binary approximation stored by the machine. If Python were to print the true decimal value of the binary approximation stored for 0.1, it would have to display

    >>> 0.1
    0.1000000000000000055511151231257827021181583404541015625

That is more digits than most people find useful, so Python keeps the number of digits manageable by displaying a rounded value instead

    >>> 0.1
    0.1

It’s important to realize that this is, in a real sense, an illusion: the value in the machine is not exactly 1/10, you’re simply rounding the display of the true machine value. This fact becomes apparent as soon as you try to do arithmetic with these values

    >>> 0.1 + 0.2
    0.30000000000000004

Note that this is in the very nature of binary floating-point: this is not a bug in Python, and it is not a bug in your code either. You’ll see the same kind of thing in all languages that support your hardware’s floating-point arithmetic (although some languages may not display the difference by default, or in all output modes).

### That sucks! What if I want to work with numbers exactly as I see it?

The `fraction` and `decimal` modules are available in Python if you want more precision.

### Complex Numbers

In Python, you can put ‘j’ or ‘J’ after a number to make it imaginary, so you can write complex literals easily:

    >>> 1j
    1j
    >>> 1J
    1j
    >>> 1j * 1j
    (-1+0j)

The ‘j’ suffix comes from electrical engineering, where the variable ‘i’ is usually used for current. 

### Ugh...my brain is melting!

Ugh, all these numbers are making my head spin. How can I possibly remember all of these?

Unless you are working on fields that require precision like scientific computing, you don't need to worry too much about this. Most of the time, you only need to work with plain integers and floats.

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

#### % (modulo division)

Get the remainder of a division operation of an operand.

    x % y 

Another way to say it is, "X divided by Y with J remaining." For example, "100 divided by 16 with 4 remaining." The result of % is the J part, or the remaining part.

Examples

    >>> 100 % 16
    4
    >>> 50 % 10
    0
    >>> 7 % 2
    1
    >>> 7 % -2
    -1
    >>> -7 % 2
    1
    >>> -7 % -2
    -1 

### Bitwise Operators

#### ~ (NOT) 
    Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1.

    >>> ~7
    -8

    NOT 0111 (decimal 7)
        = 1000 (decimal 8)

#### & (AND)
    Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0. 

    >>> 5 & 3
    1

        0101 (decimal 5)
    AND 0011 (decimal 3)
        = 0001 (decimal 1)

#### | (OR)
    Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1. 

    >>> 5 | 3
    7

        0101 (decimal 5)
    AND 0011 (decimal 3)
        = 0111 (decimal 7)

#### ^ (XOR)
    Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1. 

    >>> 5 ^ 3
    6

        0101 (decimal 5)
    AND 0011 (decimal 3)
    = 0110 (decimal 6)

#### << (LEFT SHIFT)
    
    Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y. 

    >>> 23 << 1
    46

       00010111 (decimal +23)
    =  00101110 (decimal +46)

    >>> 23 << 2
    92

       00010111 (decimal +23)
    =  01011100 (decimal +92)
        

#### >> (RIGHT SHIFT)

    Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y. 

    >>> -105 >> 1
    -53

        10010111 (decimal −105)
     =  11001011 (decimal −53)

    >>> -105 >> 2
    -27

     10010111 (decimal −105)
     = 11100101 (decimal -27)

### Number representations

    30 # Decimal representation of 30

    >>> 30
    30

    0b11110 # Binary representation of 30

    >>> bin(30)
    '0b11110'

    0x1e # Hexadecimal representation of 30
   
    >>> hex(30)
    '0x1e'

    036 # Octal representation of 30

    >>> oct(30)
    '036' 

### Done
