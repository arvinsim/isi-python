# Basic Exercise

# Functions with and without arguments

def histogram(values):
    for value in values:
        print value * "*"

histogram([4, 5, 7])

# Functions with and without return values

def do_nothing():
    pass

def do_nothing2():
    # return None
    return

do_nothing()
do_nothing2()

def rectangle_dimensions(width, length):
    return {
        'area': width * length,
        'perimeter': (2*width) + (2*length)
    }

dimensions = rectangle_dimensions(10, 20)
print """
The area is {}.
The perimeter is {}.
""".format(dimensions['area'], dimensions['perimeter'])

def reverse(word):
    return word[::-1]

def is_palindrome(word):
    return word == reverse(word)

print is_palindrome("asa")
print is_palindrome("qwertasdf")

# Named and Default Parameters

def draw_rectangle(size, character="*"):
    for s in range(size):
        if s == 0 or s == size - 1:
            print character * size
        else:
            hollow_character = ' '
            number_of_hollow_characters_per_line = size - 2
            print character + (hollow_character * number_of_hollow_characters_per_line) + character

draw_rectangle(5)
draw_rectangle(character='*', size=10)

# Advanced exercises

def is_palindrome_improved(phrase, remove_whitespace=True, remove_punctuation=True, remove_capitalization=True):
    whitespace_characters = ' \t\n\r\f\v'
    punctuation_characters = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'

    if remove_whitespace:
        for spacing_character in whitespace_characters:
            phrase = phrase.replace(spacing_character, '')
    if remove_punctuation:
        for punctuation_character in punctuation_characters:
            phrase = phrase.replace(punctuation_character, '')
    if remove_capitalization:
        phrase = phrase.lower()

    return phrase == phrase[::-1]

phrase = "Go hang a salami I'm a lasagna hog."
print is_palindrome_improved(phrase)
print is_palindrome_improved(phrase, remove_whitespace=False)
print is_palindrome_improved(phrase, remove_punctuation=False)
print is_palindrome_improved(phrase, remove_capitalization=False)
print is_palindrome_improved(phrase, remove_whitespace=False, remove_punctuation=False)
print is_palindrome_improved(phrase, remove_whitespace=False, remove_capitalization=False)
print is_palindrome_improved(phrase, remove_punctuation=False, remove_capitalization=False)

def is_vowel(character):
    return character in ('a', 'e', 'i', 'o', 'u')

def translate(word):
    translated_word = ""
    for character in word:
        if not is_vowel(character) and character != ' ':
            translated_word += character + 'o' + character
        else:
            translated_word += character
    return translated_word

print translate("this is fun")
