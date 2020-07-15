"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    words = ''
    
    for line in file_path:
        line = line.rstrip()
        full_line = line.split(' ')
        for word in full_line:
            words = words + ' ' + word

    return words
    #"Contents of your file as one long string"




def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """ 

  
    # your code goes here

    word_list = text_string.split(' ')
    word_list.pop(0)
    chains = {}
    

    #word_count = {}
    #for item in word_list:

    #for i in range(len(text-1)):
        #print text[i] text[i+1]
    
         
 
    for index in range(len(word_list)):
    
        #index = 0
        #print(index)
    
        new_word_list = word_list[index: index + 2]
        new_tuple = tuple(new_word_list)
        chains[new_tuple] = chains.get(new_tuple, 0)  
    print(chains)
     


        #index+= 1
        #new_word_list = word_list[index: index+2]
        # two_words.append(new_word_list)
        # index+= 1

        # """test_list = []
        # for test in word_list:

        #     x = two_words.append(word_list[index])
        #     y = two_words.append(word_list[index+1])
        #     #index+=1 
        #     test_tuple.append(x)
        #     test_tuple.append(y)"""
        # two_words.append(word_list[index])
        # two_words.append(word_list[index+1])

            # break
    #print(test_tuple)
            
    #print(two_words)

    #print(index, word_list[index])

    




    #print(pairs)
    

    #word_tuples = ()
    #return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


input_path = open("green-eggs.txt")

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
print(input_text)

