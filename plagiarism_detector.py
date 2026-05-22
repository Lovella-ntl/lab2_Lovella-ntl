# PLAGIARISM DETECTOR
# Import library
import string

# FUNCTION 1: READ AND CLEAN FILE

def read_file(filename):

    try:
        with open(filename, "r") as file:
            text = file.read()

        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = text.split()
        return words

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []

# FUNCTION 2: COUNT WORDS

def count_words(words):

    word_count = {}

    for word in words:

        # Count occurrences
        if word in word_count:
            word_count[word] += 1

        else:
            word_count[word] = 1

    return word_count

# FUNCTION 3: FIND COMMON WORDS

def common_words(count1, count2):

    # Find common words
    common = set(count1.keys()).intersection(set(count2.keys()))

    print("\n")
    print("COMMON WORDS")
    print("")

    # Display common words
    for word in common:

        print(
            f"{word} -> "
            f"Essay1: {count1[word]} times | "
            f"Essay2: {count2[word]} times"
        )

    return common

# FUNCTION 4: SEARCH FOR A WORD

def search_word(word, count1, count2):

    # Convert input to lowercase
    word = word.lower()

    # Check if word exists in essays
    found1 = word in count1
    found2 = word in count2

    # If word found in both essays
    if found1 and found2:

        print(f"\n'{word}' found in both essays.")
        print(f"Essay1 count: {count1[word]}")
        print(f"Essay2 count: {count2[word]}")

        return True

    # If not found
    else:

        print(f"\n'{word}' not found in one or both essays.")

        return False

# FUNCTION 5: CALCULATE PLAGIARISM

def plagiarism_percentage(words1, words2):

    # Convert lists into sets
    set1 = set(words1)
    set2 = set(words2)

    # Intersection = common words
    intersection = set1.intersection(set2)

    # Union = all unique words
    union = set1.union(set2)

    # Validation
    if len(union) == 0:
        print("No words found.")
        return

    # Formula
    plagiarism = (len(intersection) / len(union)) * 100

    print("\n")
    print("PLAGIARISM ANALYSIS")
    print("")

    print(f"Number of Common Words: {len(intersection)}")
    print(f"Total Unique Words: {len(union)}")

    print(f"\nPlagiarism Percentage: {plagiarism:.2f}%")

    # Decision
    if plagiarism >= 50:

        print("Decision: There is plagiarism.")

    else:

        print("Decision: There is no plagiarism.")

# MAIN PROGRAM

print("")
print("PLAGIARISM DETECTOR")
print("")

# STEP 1: READ ESSAYS

essay1_words = read_file("essay1.txt")
essay2_words = read_file("essay2.txt")

print("\nEssay files loaded successfully.")

# STEP 2: COUNT WORDS

essay1_count = count_words(essay1_words)
essay2_count = count_words(essay2_words)

print("Word counting completed.")

# STEP 3: DISPLAY COMMON WORDS

common_words(essay1_count, essay2_count)

# STEP 4: SEARCH FOR A WORD

print("\n")
print("WORD SEARCH")
print("")

# Loop until valid input is entered
while True:

    user_word = input("Enter a word to search: ")

    # Remove extra spaces
    user_word = user_word.strip()

    # Validation

    # Reject empty input
    if user_word == "":
        print("Error: Input cannot be empty.")

    # Reject numbers
    elif user_word.isdigit():
        print("Error: Numbers are not allowed. Please enter a word.")

    # Reject mixed letters and numbers
    elif not user_word.isalpha():
        print("Error: Please enter letters only.")

    # Valid input
    else:
        break

# Search word
search_word(user_word, essay1_count, essay2_count)

# STEP 5: CALCULATE PLAGIARISM

plagiarism_percentage(essay1_words, essay2_words)
