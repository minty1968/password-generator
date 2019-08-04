#!/usr/bin/env python
import random, sys, csv

####################################
###   Main Program starts here   ###
####################################

print(' ')
print(' ')
print(' ')

# Set up variables
diceRoll=''
randWords=''
dice1=0
dice2=0
dice3=0
dice4=0
dice5=0

# Ask user how many words they want in password
print(' ')
generateCheck=input('How many words would you like to generate : ')
print(' ')

# Generate 6 random numbers which will be used for word assignment
for i in range(0, int(generateCheck)):
  dice1=random.randint(1, 6)
  dice2=random.randint(1, 6)
  dice3=random.randint(1, 6)
  dice4=random.randint(1, 6)
  dice5=random.randint(1, 6)
  diceRoll=str(dice1)+str(dice2)+str(dice3)+str(dice4)+str(dice5)

  # Access word file and search for above code, then assign the word to a variable
  # This will be repeated for total number of words requested by user.
  with open('wordlist.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
      wordCode = row[0]
      if wordCode == diceRoll:
        decodedWord = row[1]
        randWords = randWords + decodedWord
        print('Your random word is ' + decodedWord)

# Print out words as passphrase
print(' ')
print(' ')
print('Generated Passphrase  ' + randWords)
