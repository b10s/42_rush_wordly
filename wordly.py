#!/usr/bin/env python3
import random

def count_lines(filepath):
    line_count = 0
    with open(filepath, 'r') as file:
        for line in file:
            line_count += 1
    return line_count

def choose_word(line_cnt):
    line_count = 0
    with open(filepath, 'r') as file:
        for line in file:
            line_count += 1
            if line_count == line_cnt:
              return line
    return "dummy"
print("word must be 5 letters\n")
print("rules:\n X - no letter \n ? - there is letter but different place \n O - correct")
filepath = "words.txt"
line_cnt = count_lines(filepath)
rnd_line = random.randint(1, line_cnt)
word = choose_word(rnd_line)

print("line cnt ", line_cnt)
print("random line ", rnd_line)
print("word is", word)

while (1==1):
	print()
	dct = {}

	for ch in word:
		if ch in dct:
			dct[ch] = dct[ch] + 1
		else:
			dct[ch] = 1

	#print("dct")
	#print(dct)
	user_word = input("Please enter a word: ")
	if len(user_word) != 5:
		print("please enter 5 letters words\n")
		continue

	for i, ch in enumerate(user_word):
			if word[i] == ch:
				print("O", end="")
				dct[ch] = dct[ch] - 1
			elif ch in word:
				if dct[ch] != 0:
					print("?", end="")
					dct[ch] = dct[ch] - 1
				else:
					print("X", end="")
			else:
				print("X", end="")
	
