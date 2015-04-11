# Slide 1

Values, Types and variables

# Slide 2

## Values

A **value** is one of the basic things a program works with, like a letter or a number. 'Hello, World!' is a value. So are numbers like 1 or 2.

## Native Types

Here is a quick overview of the types

    # Numeric Types
    2 # Integer
    231856456374891984564987987 # Long Integer
    3+4j # Complex
    1.5 # Floating Point

    # Sequence Types
    "Hello" # String
    u"World" # Unicode String
    [1,2,3] # Lists
    { "age": 18, "location": "Cagayan de Oro" } # Dictionaries

    # Boolean Types
    True
    False 

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

#### Long integers have unlimited precision.

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

Unless you are working on fields that require precision like scientific comput, you don't need to worry too much about this. Most of the time, you only need to work with plain integers and floats.




