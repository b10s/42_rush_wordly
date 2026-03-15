#!/usr/bin/env python3
import random
from colorama import Fore, Style


def count_lines_and_find_error(filepath):
    line_count = 0
    with open(filepath, 'r') as file:
        for line in file:
            word = line.strip()
            if len(word) != 5:
                return 0
            else:
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


filepath = "words.txt"
line_cnt = count_lines_and_find_error(filepath)

if line_cnt == 0:
    print(Fore.RED + "Error: invalid dictionaty")
    exit(1)

rnd_line = random.randint(1, line_cnt)
word = choose_word(rnd_line)
answer_count = 0

print("\ndictionary:",filepath)
print("     words:", line_cnt)

print("\nrules:")
print("word must be 5 letters")
print(Style.DIM + " x " + Style.NORMAL + "- no letter")
print(Fore.YELLOW + " x " + Fore.WHITE + "- there is letter but different place")
print(Fore.GREEN + " x " + Fore.WHITE + "- correct")
print(Style.RESET_ALL, end="")

# print("random line ", rnd_line)
# print("word is", word)

while (1):
    print()

    if answer_count >= 6:
        print(Fore.RED + "GAME OVER!\n" + Fore.WHITE + "Answer is", word)
        break

    dct = {}
    for ch in word:
        if ch in dct:
            dct[ch] = dct[ch] + 1
        else:
            dct[ch] = 1
    # print("dct")
    # print(dct)

    user_word = input("Please enter a word: ")
    print()
    if len(user_word) != 5:
        print(Fore.RED + "Invalid input! " + Fore.WHITE + "please enter 5 letters words")
        continue
    else:
        answer_count += 1

    for i, ch in enumerate(user_word):
        if word[i] == ch:
            dct[ch] = dct[ch] - 1

    for i, ch in enumerate(user_word):
        if word[i] == ch:
            print(Fore.GREEN + Style.NORMAL + ch, end="")
        elif ch in word:
            if dct[ch] != 0:
                print(Fore.YELLOW + Style.NORMAL + ch, end="")
                dct[ch] = dct[ch] - 1
            else:
                print(Fore.WHITE + Style.DIM + ch, end="")
        else:
            print(Fore.WHITE + Style.DIM + ch, end="")
    print(Style.RESET_ALL)

    if user_word == word:
        print(Fore.BLUE + "\nGAME CLEAR!")
        break
