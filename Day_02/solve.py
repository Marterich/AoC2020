#! /usr/bin/env python3
import re

"""
Enable <1> or Disable <0> debugging. Debugging includes a timer for the runtime of the script
and assertions to test if the examples work result in the correct values
"""

debug = 0

if debug:
	import time
	start = time.perf_counter()

	example_input = []	
	with open("example_input.txt", "r") as f:			#Read input Files into a list
		example_input = [x.strip() for x in f]

puzzle_input = []	
with open("puzzle_input.txt", "r") as f:				#Read input Files into a list
	puzzle_input = [x.strip() for x in f]

def part1(inp):
	correct_passwords = 0
	for x in inp:
		#Seperate the different parts of every line using RegEx
		p1 = int(re.search(r'^\w+',x)[0].strip())
		p2 = int(re.search(r'-(\w+)',x)[1].strip())
		char = re.search(r'(\w):',x)[1].strip()
		password = re.search(r'\w*$',x)[0].strip()
		
		#count how ofthen a given char apperas in the password and return the value
		char_counter = 0
		for y in range(len(password)):
			if password[y] == char:
				char_counter += 1
		if p1 <= char_counter <= p2:
			correct_passwords += 1
	return correct_passwords

def part2(inp):
	correct_passwords = 0
	for x in inp:
		#Seperate the different parts of every line using RegEx
		p1 = int(re.search(r'^\w+',x)[0].strip())
		p2 = int(re.search(r'-(\w+)',x)[1].strip())
		char = re.search(r'(\w):',x)[1].strip()
		password = re.search(r'\w*$',x)[0].strip()
		
		#check if the given char only exists in one of the two locations. If yes, increment the counter, if no, do nothing
		if password[p1-1] == char and not password[p2-1] == char or password[p2-1] == char and not password[p1-1] == char:
			correct_passwords += 1
	return correct_passwords

#Test the functions using the example data and the known result
if debug:
	assert (part1(example_input) == 2)
	print("Example for Part 1 results in the correct value")
	assert (part2(example_input) == 1)
	print("Example for Part 2 results in the correct value")

print("Part I: ",part1(puzzle_input))
print("Part II: ",part2(puzzle_input))

if debug:
	end = time.perf_counter()
	print('Runtime {:5.3f}s'.format(end - start))




