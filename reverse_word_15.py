'''
Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order.

For example, say I type the string:
  My name is Michele
Then I would see the string:

  Michele is name My
'''
def reverse_words(s):
    return " ".join(s.split(" ")[::-1])

test_string = input("Enter a string: ")
print(reverse_words(test_string))
