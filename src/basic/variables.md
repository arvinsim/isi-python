## Variables

One of the most powerful features of a programming language is the ability to manipulate variables. A variable is a name that refers to a value.

## Assignment 

An assignment statement creates new variables and gives them values. We use the `=` operator to do assignment.

    >>> message = 'And now for something completely different'
    >>> n = 17
    >>> pi = 3.1415926535897932

## Variable Names

Programmers generally choose names for their variables that are meaningful—they document what the variable is used for.

Variable names can be arbitrarily long. They can contain both letters and numbers, but they have to begin with a letter. It is legal to use uppercase letters, but it is a good idea to begin variable names with a lowercase letter

The underscore character, _, can appear in a name. It is often used in names with multiple words, such as my_name or airspeed_of_unladen_swallow. 

If you give a variable an illegal name, you get a syntax error:

    >>> 76trombones = 'big parade'
    SyntaxError: invalid syntax
    >>> more@ = 1000000
    SyntaxError: invalid syntax
    >>> class = 'Advanced Theoretical Zymurgy'
    SyntaxError: invalid syntax

76trombones is illegal because it does not begin with a letter. more@ is illegal because it contains an illegal character, @.

But what’s wrong with class?

## Keywords

It turns out that class is one of Python’s keywords. The interpreter uses keywords to recognize the structure of the program, and they cannot be used as variable names. 

Python 2 has 31 keywords:

and       del       from      not       while    
as        elif      global    or        with     
assert    else      if        pass      yield    
break     except    import    print              
class     exec      in        raise              
continue  finally   is        return             
def       for       lambda    try

## Examples of variable usage

    >>> a = 1
    >>> a
    1
    >>> a = 2
    >>> a
    2

    >>> x = 10
    >>> y = 5
    >>> x + y
    15

    >>> a = 2
    >>> b = 3
    >>> a + b
    5
    >>> a = a + b
    >>> a
    5
    >>> a = a + b
    8

## Shorthand for combining combining assignment and some operators

### +=

    >>> a = 0
    >>> a += 10 # a = a + 10
    >>> a
    10

### -=

    >>> a = 5
    >>> a -= 3 # a = a - 3
    >>> a
    2

### *=

    >>> a = 3
    >>> a *= 4 # a = a * 4
    >>> a
    12

### /=

    >>> a = 100
    >>> a *= 5 # a = a * 5
    >>> a
    20 

%=, //= are also available
