# Lab: Word Count
# ###### Delivery Method: Prompt Only
# ------------------------------------
# #### Goal
# Write a python module to analyze a given text file containing a book for is vocabulary frequency and display the most frequent words to the user in the terminal.
# ------------------------
# #### Instructions
# Find a book on [Project Gutenberg](http://www.gutenberg.org).
# Download it as a UTF-8 text file.
# 1. Open the file and deal with any decoding error that arise.
# 1.  Normalize all of the words so differences in capitalization and punctuation attached to words don't affect the counts.
# 1.  Count how often each unique word is used, then print the most frequent top 10 out with their counts.
# 1. Count how often each unique pair of words is used, then print the most frequent top 10 out with their counts.
# --------------------------------------------------------
# #### Advanced
# 1. Make a command line tool with the `sys.argv`.  Allow the the user to pass in the filename to a `.txt` file when execiting your program.  Use the `sys.argv` to parse the filename to use for the analysis.
# ---------------------------------------------------------
# #### Super Advanced
# 1. Allow the user to enter a word and get the most likely words to follow the given word.  Store the pair counts as a dict of dicts, where the first key is the first word in the pair and the second key is the second word.
#     Enter Query Word > Mr.
#     The most likely bi-gram pair starting with "Mr." is "Mr. Darcy".
# 1. Redo the pair counts: normalize the probabilities in the inner dict by the count of pairs that start with the first word.
# 1. Chain together that ability to generate random sentences, one word at a time, from a given starting word.
# This is a language model.
#

# The following code snippet reads url of book into a list of strings:
# import urllib.request
#
# with urllib.request.urlopen('http://www.gutenberg.org/cache/epub/1661/pg1661.txt') as book_file:
#   lines = [byte_line.decode('utf-8') for byte_line in book_file]
#

import string


def convert_line(line):
    # remove line breaks and white space
    line = line.strip()
    # convert all words to lowercase for matching
    line = line.lower()
    # separate words by spaces
    word_list = line.split(" ")

    # remove punctuation and replace words
    for i in range(len(word_list)):
        word_list[i] = word_list[i].strip(string.punctuation)
    return word_list

# empty dictionary of words
word_set = {}

# open file as readable
file_name = "sherlock.txt"
with open(file_name, "r") as file:
    # add lines to word_list
    for line in file:
        # run convert_line function on file to create word_list
        word_list = convert_line(line)

        for word in word_list:
            # skip blank space
            if word == "":
                continue
            # if word is already in set, increment its value
            if word in word_set:
                word_set[word] += 1
            # add new word
            else:
                word_set[word] = 1

# put words in list
words = list(word_set.items())
# print(words)
# the part I have no idea how it works /0\
# convert list items to tuples, sort backwards (largest amount at top)
words.sort(key=lambda tup: tup[1], reverse=True)
# increment a 10-item list of top used words
# for i in range(min(10, len(words))):

# list all words by frequency
for i in range(len(words)):
    print(words[i])
