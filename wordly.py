#!/usr/bin/env python3
import random
from colorama import Fore, Style

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
              return line.strip()
    return "dummy"
print("word must be 5 letters\n")
print("rules:\n X - no letter \n ? - there is letter but different place \n O - correct")
filepath = "words.txt"
line_cnt = count_lines(filepath)
rnd_line = random.randint(1, line_cnt)
word = choose_word(rnd_line)
answer_count = 0

print("line cnt ", line_cnt)
print("random line ", rnd_line)
print("word is", word)

while (1==1):
	print()

	if answer_count >= 6:
		print("GAME OVER\nAnswer is" ,word)
		break
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
		print("please enter 5 letters words", end="")
		continue
	else:
		answer_count += 1

	for i, ch in enumerate(user_word):
			if word[i] == ch:
				print(Fore.GREEN + ch, end="")
				dct[ch] = dct[ch] - 1
			elif ch in word:
				if dct[ch] != 0:
					print(Fore.YELLOW + ch, end="")
					dct[ch] = dct[ch] - 1
				else:
					print(Fore.WHITE + Style.DIM + ch, end="")
			else:
				print(Fore.WHITE + Style.DIM + ch, end="")
			print(Style.RESET_ALL, end="")
