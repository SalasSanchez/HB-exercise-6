# opens a file named on the command line 
"""
import argv and define arguments 
make a string out of the imported file
"""

from sys import argv
script, filename = argv

thefile = open(filename)



# thefile = f.read()
# f.close()

#counts how many times each space-separated word occurs in that file. 
"""
    check to see if the word exists in the dictionary
    if so- add 1 to the counter for that word 
    if not create a new item with that word as key (counter starts at 1)
"""
dictionary = {}

for line in thefile:
    # print line
    for word in line.split(" "):
        word = word.strip()
        if not dictionary.get(word):
            dictionary[word] = 1
        else:
            dictionary[word] += 1

for word, count in dictionary.iteritems():
    print word + " " + str(count)

