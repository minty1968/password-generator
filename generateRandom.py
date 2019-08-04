#!/usr/bin/env python3
import random, sys, csv
from string import punctuation

####################################
###   Main Program starts here   ###
####################################

print(' ')
print(' ')
print(' ')

alphaChars=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numberChars=['0','1','2','3','4','5','6','7','8','9']
passLength=0
numTotal=0
passChars=''
alpha=''
digit=''
special=''
charPass=''

# Ask user for password length
print(' ')
while True:
  try:
    passLength=int(input('Password Length - Numbers only: '))
    break
  except ValueError:
    print("Please enter a number only")
print(' ')

# Ask user if they want to include Upper and Lower case letters,
# this would also be set as easy to remember password type for GUI
while True:
  try:
    alpha=input('Include Upper and Lower case Letters - Y or N  only: ').upper()
    if alpha == 'Y' or alpha == 'N':
      break
  except ValueError:
    print("Please enter Y or N only")
print(' ')

# Ask user if they want to include numbers,this would also be set as
# medium style password for GUI, when used with letters
while True:
  try:
    digits=input('Include Digits 0 to 9 - Y or N  only: ').upper()
    if digits == 'Y' or digits == 'N':
      break
  except ValueError:
    print("Please enter Y or N only")
print(' ')

# Ask user if they want to include special characters, this would also be set as
# difficult to remember password type for GUI, when used with letter and numbers.
while True:
  try:
    special=input('Include Special Characters - Y or N  only: ').upper()
    if special == 'Y' or special == 'N':
      break
  except ValueError:
    print("Please enter Y or N only")
print(' ')

# Here we create password from user input above
for i in range(0, int(passLength)):
  if alpha == 'Y' and digits == 'Y' and special == 'Y':
    charTypeNum=random.randint(0, 3)
  elif alpha == 'N' and digits == 'Y' and special == 'Y':
    charTypeNum=random.randint(2, 3)
  elif alpha == 'Y' and digits == 'Y' and special == 'N':
    charTypeNum=random.randint(0, 2)
  elif alpha == 'Y' and digits == 'N' and special == 'N':
    charTypeNum=random.randint(0, 1)
  elif alpha == 'N' and digits == 'N' and special == 'Y':
    charTypeNum=3
  elif alpha == 'N' and digits == 'Y' and special == 'N':
    charTypeNum=2
  # 0  is for lowercase letters  a to z
  if charTypeNum == 0:
    charPass=random.choice(alphaChars).lower()
    passChars=passChars+charPass
  # 1  is for uppercase letters A to Z
  if charTypeNum == 1:
    charPass=random.choice(alphaChars).upper()
    passChars=passChars+charPass
  # 2  is for mumbers 0 to 9
  if charTypeNum == 2:
    charPass=random.choice(numberChars)
    passChars=passChars+charPass
  # 3  is for special characters - using puncuation from python module string
  if charTypeNum == 3:
    charPass=random.choice(punctuation)
    passChars=passChars+charPass

# Print generated password
print(' ')
print(' ')
print('Your password is {}'.format(passChars))
print(' ')
print(' ')
