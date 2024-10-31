"""
DESCRIPTION:
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false

"""

#first_solution
def generate_hashtag(s):
    if len(s) > 140:
        return False
    s = s.strip()
    if len(s) == 0:
        return False
    else:
         s = s.split()
         n =''
         for letter in s:
            letter = letter.capitalize()
            n+=letter
         n = str(n)
         n = '#'+n
         return n