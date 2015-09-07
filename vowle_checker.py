__author__ = 'Mobarak'

# assign vowels is the variable vowels
vowels = ['a','e','i','o','u','A','E','I','O','U']
# Here is our string to find vowels
str = str(input ("Vowel counter - Type and count vowels : "))

# initialize the counter veritable
c = 0

# This loop to iterate each character
for ch in str: # ch(characters) in string
    # This loop will check 'ch' is vowels or not
    # This loop to iterate vowels
    for v in vowels:
        if ch == v: # checks vowels
            c = c+1 # counts vowels

print("Your input: ", str)
if c==0:
    print("There is not any vowel in your given string!")
elif c<2:
    print("There is", c, "vowel in your given string!")
else:
    print("There are", c, "vowels in your given string!")