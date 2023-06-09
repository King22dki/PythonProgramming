#https://www.youtube.com/watch?v=buMTH6ICnqk

#This programs says hello and asks for my name

print('Hello World')

print('What is your name') # ask for their name
myName = input ()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))

print('What is your age?') # ask for thier age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

'''
    Remember that the input value always returns a string value
    so we may use other functions to change that input into a an
    integer, float or vice versa turn an integer or float into a
    string.

    You can use concatenation to put a series of similar data types
    together, but remember they all have to be the same data type,
    otherwise it will not work and give you a TypeError. This is
    because Python can not convert data types to other data types

    When you look at Python code remeber it operates in a similar
    manner to how rows of operations are completed (BIDMAS).

    Example: Let's say that the input for age is 29. Thus python
    will go through the following steps.
    
    print('You will be ' + str(int(myAge) + 1) + ' in a year.')
    print('You will be ' + str(int('29') + 1) + ' in a year.')
    print('You will be ' + str(29 + 1) + ' in a year.')
    print('You will be ' + str(30) + ' in a year.')
    print('You will be ' + '30' + ' in a year.')
    print('You will be 30' + ' in a year.')
    print('You will be 30 in a year.')

    Recap:
    The excution starts at the top and moves down.
    # comments are ignored by Python.
    Functions are mini-programs in your program.
    - print() displays the value passed to it.
    - input() lets user type in a value,
    - len () takes a string value and returns an integer value of the
      string's length.
    - int(), str(), and float() convert values' data types.
    
'''

