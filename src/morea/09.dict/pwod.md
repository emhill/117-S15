---
title: "PWOD9"
published: true
morea_id: pwod9
morea_type: experience
morea_sort_order: 9
morea_summary: "Dictionaries, Files, & While"
morea_labels:
 - by 4/10
---
# Practice WOD9: Sets, Dictionaries, Files, & While

In this practice WOD you will create 4 programs that use data structures (sets, dictionaries), input/output from files, and while loops.

<!--{% include wod-times.html Rx="<30 min" Av="30-60 min" Sd="60-90 min" DNF="90+ min" %}-->

## while.py

Create a program `while.py` that declares the following set:

`s = {"A", "B", "C", "D", "E"}`

and prints a random element of the set until the first element is printed. In other words, the while loop continues printing letters in the set `s` until "A" is printed. See Step 4 in [Project2's]({{site.baseurl}}/morea/10.project2/Project2.docx) Background Learning for hints on how to randomly print an element from a set.

Create another set:

`r = {"A", "C", "E", "G"}`

and print the results of the following [set operations](https://docs.python.org/3.4/library/stdtypes.html#set): union, intersection, and difference.

## dictionary.py

Create a program `dictionary.py` that creates a simple dictionary with two keys, even & odd, that stores the set of even & odd numbers from 1 to 10. Print out your dictionary to the file `even_odd.txt`.

***Hints:***

 * use `set()` to initialize an empty set

***Recommended Development Steps:***

1. Write a loop that prints out the numbers from 1 to 10
2. In this loop, print out whether the number is even or odd
3. Create a set for even and a set for odd numbers. Instead of printing in the loop, add the number to the appropriate set. Print out the sets after the loop.
4. Replace your set variables by adding them to a dictionary `d` instead. For example, if you had a set named `even`, replace every occurrence of that variable with `d[even]`. Print out the dictionary after your loop to confirm the behavior is the same.
5. Instead of printing to the screen, print the dictionary to the file `even_odd.txt`.

## count.py

Write a program `count.py` that reads in [the file `turing.txt`](data/turing.txt) and counts the number of occurrences of the word "the". 

***Hints:***

  * Lowercase your words so that "the" is counted the same as "The".
  * Using one of the following functions is recommended (but don't use both! they represent different ways of tackling the problem)
    * The [string `split` function](https://docs.python.org/3.4/library/stdtypes.html#str.split) allows you to split a line of input into a list of words by splitting the line on spaces.
    * The [`count` function](http://www.thehelloworldprogram.com/python/python-string-methods/) allows you to count the number of occurrences in a string.

## frequency.py

Write a program `frequency.py` that reads in [the file `turing.txt`](data/turing.txt) and counts the number of occurrences of each word. Your program should print out these word occurrences in sorted order by decreasing frequency value. For example, "the" occurs 10 times and would be printed out before "Alan", which occurs just once.

Your program should not take in any user input, just read in the hard-coded filename `"turing.txt"`. You may use any example template to read in the file (for loop, while loop, etc).

***Recommended Development Steps:***

1. Read in the file & print it back out.
2. Read in the file, split each line on spaces, & print each word on a separate line.
3. Create a frequency dictionary and add each word to it: `freq[word] = 1`. Print out the dictionary.
4. Count the number of words. Print out the dictionary.
5. Sort the dictionary by values before printing. 

***Hints:***

  * The [string `split` function](https://docs.python.org/3.4/library/stdtypes.html#str.split) allows you to split a line of input into a list of words by splitting the line on spaces.
  * Lowercase your words so that "the" is counted the same as "The".
  * When counting words with a dictionary, you will need to check if the word is in the dictionary already. If it is, just add 1 to the current value. If it's not, initialize it to 1.
  * You can use the built-in [sorted function](https://wiki.python.org/moin/HowTo/Sorting/) to sort by values. The [`operator.itemgetter` function](https://docs.python.org/3/library/operator.html#operator.itemgetter) makes a good key.


## Demonstration

*Coming soon...*

<!--Once you've finished doing the WOD a single time, you can watch me do it:

{% include youtube.html id="hsjv5f2DlFk" %}

Recursive solution to pyramid function in text.py:

{% include youtube.html id="yBrjRTtFiTE" %}

{% include wod-warning.html %}-->

