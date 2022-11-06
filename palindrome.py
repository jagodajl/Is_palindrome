# sub() function belongs to the Regular Expressions (re) module in Python.
# it returns a string where all matching occurrences of the specified pattern are replaced by the replace string.
import re
from string import punctuation

def is_palindrome(in_string):
    """ Returns True whether in_string is palindrome, False otherwise.
    Function sits in the module palindrome."""
    # Function treats strings as case-insensitive
    in_string = in_string.lower()
    # Function purges spaces
    in_string = re.sub('\s+', '', in_string)
    # Function purges punctuation
    in_string = re.sub('[' + re.escape(punctuation) + ']+', '',
                       in_string)
    # Function checks if string is same as in reverse
    return in_string == in_string[-1::-1]

