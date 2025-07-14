import doctest
import string

def expand_encoded_string(encoded_string):
    """
    Expands a run-length encoded string into its full form.

    The input string is assumed to be in the format where every character
    is followed by a digit indicating how many times that character
    should be repeated in the output. The function decodes this pattern and
    reconstructs the full, uncompressed string.

    >>> expand_encoded_string('B4')
    'BBBB'
    >>> expand_encoded_string('x0y5')
    'yyyyy'
    >>> expand_encoded_string('m1e2t1')
    'meet'
    >>> expand_encoded_string('B1o2k2e2p1e1r1!3')
    'Bookkeeper!!!'

    Args:
        encoded_string (str): The run-length encoded string to expand.
    
    Returns:
        str: The expanded string with characters repeated according to the digits.
    """
    # initialize an empty string to hold the expanded characters
    expanded_string = ""
    # iterate through the encoded string
    for i in range(len(encoded_string)):
        #if a character is alphabetic or is a punctuation, repeat it according to the number that follows and append to the expanded string
        if encoded_string[i].isalpha() or encoded_string[i] in string.punctuation:
            expanded_string += encoded_string[i] * int(encoded_string[i+1])
    return expanded_string

doctest.testmod(verbose=True)

   
