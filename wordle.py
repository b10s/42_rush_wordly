#!/usr/bin/env python3
import random
from colorama import Fore, Style
import sys
import os

DEBUG_MODE = "-debug" in sys.argv

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

print(Style.RESET_ALL, end = "")
if len(sys.argv) < 2:
    print("Usage: python3 wordle.py [dictionaty file]")
    exit(1)

filepath = sys.argv[1]

if not os.path.exists(filepath):
    print(f"Error: file'{filepath}'is not found")
    exit(1)

line_cnt = count_lines_and_find_error(filepath)

if line_cnt == 0:
    print(Fore.RED + "Error: invalid dictionaty")
    exit(1)

rnd_line = random.randint(1, line_cnt)
word = choose_word(rnd_line)
answer_count = 0

print(Fore.RED + " __        __              _ _")
print(Fore.YELLOW + " \\ \\      / /__  _ __   __| | | ___")
print(Fore.GREEN + "  \\ \\ /\\ / / _ \\| '__\\ / _` | |/ _ \\ ")
print(Fore.CYAN + "   \\ V  V / (_) | |   | (_| | |  __/")
print(Fore.MAGENTA + "    \\_/\\_/ \\___/|_|    \\__,_|_|\\___|")
print(Style.RESET_ALL)

print("dictionary:", filepath)
print("     words:", line_cnt)

print("\nrules:")
print("word must be 5 letters")
print(Style.DIM + " x " + Style.NORMAL + "- no letter")
print(Fore.LIGHTYELLOW_EX + " x " + Style.RESET_ALL + "- there is letter but different place")
print(Fore.LIGHTGREEN_EX + " x " + Style.RESET_ALL + "- correct")
print(Style.RESET_ALL, end="")

if DEBUG_MODE:
    print("random line ", rnd_line)
    print("word is", word)

while (1):
    print(Style.RESET_ALL)

    if answer_count >= 6:
        print(Fore.RED + "GAME OVER!\n" + Fore.WHITE + "Answer is", word)
        break

    dct = {}
    for ch in word:
        if ch in dct:
            dct[ch] = dct[ch] + 1
        else:
            dct[ch] = 1

    if DEBUG_MODE:
        print("dct")
        print(dct)

    print("Remaining attempts:",6- answer_count)
    user_word = input("Please enter a word: ")
    print()
    if len(user_word) != 5:
        print(Fore.RED + "Invalid input! " + Style.RESET_ALL + "please enter 5 letters words")
        continue
    else:
        answer_count += 1

    for i, ch in enumerate(user_word):
        if word[i] == ch:
            dct[ch] = dct[ch] - 1

    for i, ch in enumerate(user_word):
        if word[i] == ch:
            print(Fore.LIGHTGREEN_EX + Style.NORMAL + ch, end="")
        elif ch in word:
            if dct[ch] != 0:
                print(Fore.LIGHTYELLOW_EX + Style.NORMAL + ch, end="")
                dct[ch] = dct[ch] - 1
            else:
                print(Fore.WHITE + Style.DIM + ch, end="")
        else:
            print(Fore.WHITE + Style.DIM + ch, end="")
    print(Style.RESET_ALL)

    if user_word == word:
        print(Fore.BLUE + "\nGAME CLEAR!")
        break
