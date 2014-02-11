# opens a file named on the command line 
# import argv and define arguments 
# make a string out of the imported file


from sys import argv
script, filename = argv

f = open(filename)
thefile = f.read()
f.close()


#counts how many times each space-separated word occurs in that file. 

dictionary = {}

# alphabet: ascii 97 through 122

notalphabet = []
for i in range(0, 97):
    thechar = chr(i)
    notalphabet.append(thechar)
for i in range(123, 128):
    thechar = chr(i)
    notalphabet.append(thechar)
notalphabet = ''.join(notalphabet)

# check to see if the word exists in the dictionary
# if so- add 1 to the counter for that word 
# if not create a new item with that word as key (counter starts at 1)

for word in thefile.split():
    word = word.lower()
    word = word.strip(notalphabet)
    if len(word) != 0:
        if not dictionary.get(word):
            dictionary[word] = 1
        else:
            dictionary[word] += 1



## This will sort them according to the number of appearances



sorteddictionary = {}

# Check to see if count exists as a key in new dictionary; if not, add count + corresponding word (as a list)
# If count exists, append value list

for word, count in dictionary.iteritems():
    if not sorteddictionary.get(count):
        sorteddictionary[count] = [word]
    else:
        sorteddictionary.get(count).append(word)

# get list of all keys, sort in descending order

key_list = sorteddictionary.keys()
key_list.sort(reverse = True)

# print each key repeated as necessary with all corresponding values from lists

for count in key_list:
    howmany = len(sorteddictionary[count])
    sorteddictionary[count].sort()
    for i in range(howmany):
        print str(count) + " " + sorteddictionary[count][i]