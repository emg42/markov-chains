"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path).read()
    return f'{contents}'


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each i       tem in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    # your code goes here
    words = text_string.split(" ")
    words.append(None)
    for i in range(len(words) - 2):
        bigram = (words[i], words[i + 1])
        value = words[i + 2]
        
        if bigram not in chains:
            chains[bigram] = []
        chains[bigram].append(value)
            
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    first_key = choice(list(chains))
    while first_key in chains:
        new_key = (first_key[1], choice(chains[first_key]))
        words.append(new_key[0])
        words.append(new_key[1])
        first_key = new_key
        
    # your code goes here
    return ' '.join(words)

    # box? Would you could you with a mouse? Would you could you
    # in a house? Would you could you in a house? Would you
    # could you in a house? Would you could you with a fox?
    # Would you like green eggs and ham? Would you like them, Sam
    # I am?


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
