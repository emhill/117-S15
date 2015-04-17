---
title: "Code Examples"
published: true
morea_id: board10
morea_summary: "In class"
morea_type: reading
morea_labels:
morea_sort_order: 0
---

# Board & Demo Notes

## In class 4/6

 * [csv_reader.py](in_class/csv_reader.py)
 * [harry_potter.csv](in_class/harry_potter.csv)

Sets of friends:

<a href="friend-sets.JPG"><img src="friend-sets.JPG" width="300"/></a>

Given the friend sets above, who should we recommend as a friend for Emily? Anna or Bill?

<a href="friend-rec.JPG"><img src="friend-rec.JPG" width="300"/></a>

## In class 4/17

	def mean(numbers):
		return sum(numbers) / len(numbers)
	
	
	#numbers = list(range(1,11))
	numbers = []
	file = open("numbers.txt")
	for line in file:
		numbers.append(eval(line))
	file.close()
	
	print(numbers)
	print("Mean: ", mean(numbers) )