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

In this practice WOD you will create 4 programs that use data structures (i.e., sets, lists, tuples, and dictionaries), input/output from files, and while loops. ***Make sure to read the hints & recommended development steps for each program.***

The last program, frequency.py, will likely take as long to implement as the first 3 programs. I recommend completing the first 3, and watching the video for those if you didn't complete them, *before* attempting frequency.py.


{% include wod-times.html Rx="<45 min" Av="45-90 min" Sd="90-135 min" DNF="135+ min" %}

## while.py

Create a program `while.py` that declares the following set:

`s = {"A", "B", "C", "D", "E"}`

and prints a random element of the set until the first element is sampled. In other words, the while loop continues printing letters in the set `s` until "A" is the next letter. The output should have no "A"'s.

Then, create another set:

`r = {"A", "C", "E", "G"}`

and print the results of the following [set operations](https://docs.python.org/3.4/library/stdtypes.html#set): union, intersection, and difference.

***Hints:***

 * See Step 4 in [Project2's]({{site.baseurl}}/morea/10.project2/Project2.docx) Background Learning for hints on how to randomly print an element from a set. For more information see the [random sample function](https://docs.python.org/3.4/library/random.html#random.sample).
 
* I recommend following the sentinel while loop pattern:

      value = initialize
      while value != sentinel:
        process value
        value = updated value

***Recommended Development Steps:***

1. Create the set `s` and print it out
2. Print out a random sample of 1 element from `s` instead (see hints above)
3. Use the sentinal template in the hints above to create a while loop that prints out a random letter until the value is "A"
4. Create the set `r` and print out the union with `s`
5. Print out the intersection and difference


## dictionary.py

Create a program `dictionary.py` that creates a simple dictionary with two keys, even & odd, that stores the set of even & odd numbers from 1 to 10. Print out your dictionary to the file `even_odd.txt`.

***Hints:***

 * Use the [`set()` function](https://docs.python.org/3.4/library/stdtypes.html#set) to initialize an empty set.

***Recommended Development Steps:***

1. Write a loop that prints out the numbers from 1 to 10
2. In this loop, print out whether the number is even or odd
3. Create a set for even and a set for odd numbers. Instead of printing in the loop, add the number to the appropriate set. Print out the sets after the loop.
4. Replace your set variables by adding them to a dictionary `d` instead. For example, if you had a set named `even`, replace every occurrence of that variable with `d['even']`. Make sure you initialize `d` to be an empty dictionary (`d = {}`). Print out the dictionary after your loop to confirm the behavior is the same as in the prior step.
5. Instead of printing to the screen, print the dictionary to the file `even_odd.txt`. See Step 3 in [Project2's]({{site.baseurl}}/morea/10.project2/Project2.docx) Background Learning for hints on how to output to a file.

## count.py

Write a program `count.py` that reads in [the file `turing.txt`](data/turing.txt) and counts the number of occurrences of the word "the". 

***Hints:***

  * Lowercase your words so that "the" is counted the same as "The".
  * Using one of the following functions is recommended (but don't use both! they represent different ways of tackling the problem)
    * The [string `split` function](https://docs.python.org/3.4/library/stdtypes.html#str.split) allows you to split a line of input into a list of words by splitting the line on spaces.
    * The [`count` function](http://www.thehelloworldprogram.com/python/python-string-methods/) allows you to count the number of occurrences in a string.
  * Review the lecture slides or example file programs in the unit for help on reading in a file.

## frequency.py

Write a program `frequency.py` that reads in [the file `turing.txt`](data/turing.txt) and counts the number of occurrences of each word. Your program should print out these word occurrences in sorted order by decreasing frequency value. For example, "the" occurs 10 times and would be printed out before "Alan", which occurs just once.

Your program should not take in any user input, just read in the hard-coded filename `"turing.txt"`. You may use any example template to read in the file (for loop, while loop, etc).

***Recommended Development Steps:***

1. Read in the file & print it back out.
2. Read in the file, split each line on spaces, & print each word on a separate line.
    * To check your work, use the UNIX command `python3 frequency.py | sort | uniq -c | sort -rn` to give a list of all the words sorted by frequency. 
    * Make sure you don't see any unwanted values like punctuation or spaces. If you do, tweak your program to get your desired output. (See hints below.)
    * Your next step is to implmement the above UNIX command in your python program using a dictionary.
3. Create a frequency dictionary and add each word to it: `freq[word] = 1`. Print out the dictionary.
4. Count the number of words (see hints below). Print out the dictionary.
5. Sort the dictionary by values before printing. (See hints below.)

***Hints:***

  * The [string `split` function](https://docs.python.org/3.4/library/stdtypes.html#str.split) allows you to split a line of input into a list of words by splitting the line on spaces.
  * Lowercase your words so that "the" is counted the same as "The".
  * Don't forget to replace punctuation so "Alan" is counted the same as "Alan,". I recommend the [`replace` function](http://www.tutorialspoint.com/python/string_replace.htm) for this. You can use a loop on a string to replace many characters.  
  * When counting words with a dictionary, you may need to check if the word is in the dictionary already. If it is, just add 1 to the current value. If it's not, initialize it to 1. If you are using the `count` function you may not encounter this issue.
  * You can use the built-in [sorted function](https://wiki.python.org/moin/HowTo/Sorting/) to sort by values. The [`operator.itemgetter` function](https://docs.python.org/3/library/operator.html#operator.itemgetter) makes a good key. For more information, see [this answer on stack overflow](http://stackoverflow.com/a/613218)


## Demonstration

<!--*Coming soon...*-->

Once you've finished doing the WOD a single time, you can watch me do it:

{% include youtube.html id="FMj6DvHxJw8" %}

{% include wod-warning.html %}

