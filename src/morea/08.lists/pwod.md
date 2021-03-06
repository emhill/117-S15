---
title: "PWOD8"
published: true
morea_id: pwod8
morea_type: experience
morea_sort_order: 8
morea_summary: "Recursion & Lists"
morea_labels:
 - by 3/25
---
# Practice WOD8: Recursion & Lists

In this practice WOD you will create 3 programs that use strings, lists, and recursion.

{% include wod-times.html Rx="<30 min" Av="30-60 min" Sd="60-90 min" DNF="90+ min" %}

## text.py

Write a function `pyramid` that takes a string of text as a parameter and outputs the text as follows:

    Enter text: we love CS
	w
	we
	we 
	we l
	we lo
	we lov
	we love
	we love 
	we love C
	we love CS
	we love C
	we love 
	we love
	we lov
	we lo
	we l
	we 
	we
	w

You may use *either* recursion *or* iteration in your solution.

Next write a function `is_palindrome` that takes a string of text as a parameter and outputs whether or not the string is the same forward & backward. For example, "Anna", "civic", and "rotator" are example palindrome words; "A man, a plan, a canal: Panama" and "Emily’s sassy lime" are example palindrome phrases.

Test your functions by getting a string of text from the user and printing the results of both functions.

<!--## baby_mangle.py-->

## mode.py

Create a program that calculates the most frequently occurring number in a list of 10 numbers entered by the user. Make sure you ask (i.e., prompt) the user to enter each number (the user will hit enter after each number). You may use the python [mode](https://docs.python.org/3.4/library/statistics.html#statistics.mode) function.

## wheel.py

Write a **recursive** function `sajak` which takes a word as a parameter and returns the number of vowels in that string.

Write an **iterative** function `count_vowels` which takes a word as a parameter and returns the number of vowels in that string.

Test both functions by asking the user to enter a word, and printing the number of vowels found by each function.


## Demonstration

<!--*Coming soon...*-->

Once you've finished doing the WOD a single time, you can watch me do it:

{% include youtube.html id="hsjv5f2DlFk" %}

Recursive solution to pyramid function in text.py:

{% include youtube.html id="yBrjRTtFiTE" %}

{% include wod-warning.html %}

