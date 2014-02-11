# opens a file named on the command line 
# import argv and define arguments 
# make a string out of the imported file


from sys import argv
script, filename = argv

f = open(filename)
thefile = f.read()
f.close()


#counts how many times each space-separated word occurs in that file. 
# check to see if the word exists in the dictionary
# if so- add 1 to the counter for that word 
# if not create a new item with that word as key (counter starts at 1)

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


for word in thefile.split():
    word = word.lower()
    word = word.strip(notalphabet)
    if not dictionary.get(word):
        dictionary[word] = 1
    else:
        dictionary[word] += 1

## This prints out the word counts with no sorting
# for word, count in dictionary.iteritems():
#     print word + " " + str(count)


## This will sort them according to the number of appearances


# loop through sorted list of keys: get length of its value, sort value list,
# for i in range(len(value)), print that key along with its value[i] each time

sorteddictionary = {}

for word, count in dictionary.iteritems():
    if not sorteddictionary.get(count):
        sorteddictionary[count] = [word]
    else:
        sorteddictionary.get(count).append(word)

key_list = sorteddictionary.keys()
key_list.sort(reverse = True)

for count in key_list:
    howmany = len(sorteddictionary[count])
    sorteddictionary[count].sort()
    for i in range(howmany):
        print str(count) + " " + sorteddictionary[count][i]

