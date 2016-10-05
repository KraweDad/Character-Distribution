"""
distribution.py
Author: Matthew
Credit: Robbie

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
import string
import collections
from string import ascii_lowercase
from string import ascii_letters

start = input(" Please enter a string of text (the bigger the better): ")
print("The distribution of characters in " '"' + start + '"'". is: ")

p = start.lower()
g = p.replace(" ","")
w = filter(str.isalpha,g)

ll= []
d = collections.defaultdict(int)

for k in w:
    d[k] += 1
lol = sorted(d.items())

for x in range(100, 0, -1):
    for h in lol:
        if h[1] == x:
            print(h[0]*h[1])
 