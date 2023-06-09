# Boolean Operators

'''
   Overview:

   Boolean Data Type: True, False.
   Comparison Operators: ==, !=, <, >, <=, >=
   == is comparison, = is assignment.
   Boolean operators: and, or, not

   Truth tables:
   Expression        Evaluates to...

   True and True     True

   True and False    False

   False and True    False

   False and False   False

   True or True      True

   True or False     True

   False or True     True

   False or False    False

   Note: The not operator only works on one boolean value.

   not True          False

   not False         True

   Now that we known about boolean values we can now use flow control
   statements like "if" and "else". This will allow us to covert flow
   charts into programs.

   Note: The accompanying flow charts of each code is saved as an image
   in the flow chart section.

'''

# Example Program 1:

'''
   The code below has two blocks within it. One can recongise another block
   simply by the fact that there is an identation.
   
'''

password = 'swordfish'
if password == 'swordfish':
    print('Access granted.')
else:
    print('Wrong password.')
    
# Example Program 2:
'''
   In this example the input() will return a string valueinstead of a boolean.
   It still works because the condtions can use "Truthy" and "Falsey" values.
   The condtion evaluates a blank string as a "Falsey" value and a input like
   'Luffy' would be considered a "Truthy" value which would essentially be all
   other values. So if it is "Truthy", it is considered "True", it goes in the
   first block of code; and if it is "Falsey", it is considered "False", and goes
   into the second line of code.

   This line of code works but I recommend being more explicit with ones defintions.

   str: '' is falsey all others are truthy. 
   int: 0 is falsey, all others are truthy.
   float: 0.0 is falsey, all others are truthy.

   You can always see if a value is Truthy or Falsey when you pass them to the bool
   function. 
'''

print('Enter a name.')
name = input()
if name != '':
    print('Thank you for entering a name.')
else:
    print('YOu did not enter a name.')
