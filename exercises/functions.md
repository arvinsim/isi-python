# Function Exercises


## Basic Exercises 

*Level*: ![](http://db.irowiki.org/image/monster/1002.png "Poring")

### Functions with and without arguments

+ Choose a song that you like. Using functions, divide that song to some logical divisions(chorus, verse, bridge, etc) 
and print out the whole lyrics of the song without copy pasting the parts of the song that are repeated.

+ Define a procedure `histogram()` that takes a list of integers and prints a histogram to the screen. For example, 
histogram([4, 9, 7]) should print the following:

<pre>
    ****
    *********
    *******
</pre>

### Functions with and without return values

+ Define 2 functions, `do_nothing()` and `do_nothing2()` that returns nothing. One of the functions must use the `return`
keyword.

+ Define a function `rectangle_dimensions()` that takes a width and length/height of a rectangle and returns the area and 
perimeter based on those values. Perimeter is calculated as the sum of twice the width and twice the length. Area is calculated as the product of the width and length.

+ Define 2 functions. `is_palindrome()` should utilize the result of `reverse()`
    + `reverse()` that computes the reversal of a string. For example, reverse("I am testing") should return the string "gnitset ma I”
    + `is_palindrome()` that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome("radar") should return True.

### Named Parameters and Default Parameters

- Define a function that draws a rectangle using asterisks as default, accepting a parameter that defines how many asterisks to draw for its width and height

    **draw_rectangle(size=1)**

    <pre>
        *
    </pre>
    
    **draw_rectangle(size=2)**
    
    <pre>
        **
        **
    </pre>
    
    **draw_rectangle(size=3)**
    
    <pre>
        ***
        * *
        ***
    </pre>
    
    **draw_rectangle(size=10)**
    
    <pre>
        *********
        *       *
        *       *
        *       *
        *       *
        *       *
        *       *
        *       *
        *       *
        *********
    </pre>
    
    **draw_rectangle(character='+', size=10)**
    
    <pre>
        +++
        + +
        +++
    </pre>


## Advanced Exercises

*Level:*  ![](http://vignette3.wikia.nocookie.net/ragnarok8812/images/f/f5/RO_Deviling.gif/revision/latest?cb=20130131215804 "Deviling")

+ Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?",
 "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori",
  "Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually ignored. But make it so that it can also
   choose not to ignore those. Use functions to break down the problem into manageable chunks.

- Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
- Write a function `translate()` that will translate a text into "rövarspråket" (Swedish for "robber's language").
 That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun") should return the string "tothohisos isos fofunon".
