# lab2_Lovella-ntl
coding lab/ plagiarism detector

Overview

This is a simple Python program that checks similarity between two essays (essay1.txt and essay2.txt) and calculates a plagiarism percentage.

Features
1. Read Files

Reads and loads both essay text files.

2. Text Cleaning
Converts text to lowercase
Removes punctuation
Splits text into words

This ensures accurate comparison.

3. Word Counting

Stores how many times each word appears using a dictionary.

4. Common Words

Finds words that appear in both essays and shows their frequency.

5. Word Search

Allows the user to search for a word and shows how many times it appears in each essay.
Includes validation to reject:

Numbers
Empty input
Invalid characters
6. Plagiarism Check

Uses set operations:

Intersection → common words
Union → all unique words


Decision:

≥ 50% → Plagiarism detected
< 50% → No plagiarism

How to Run
Add essay1.txt and essay2.txt in the same folder

Run:
python plagiarism_detector.py

Skills Used:

File handling
Dictionaries
Sets
Functions
Input validation