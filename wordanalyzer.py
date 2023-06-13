import re

def count_words_lines (filename):
    try:
        with open(filename, "r") as file:
            content = file.read()

            lines = content.split('\n')
            destructured = content.split()
            
            line_count = len(lines)
            word_count = len(destructured)

            return line_count, word_count
        
    except FileNotFoundError:
        print(f"No File found as {filename}")
        return 0, 0
    
def count_sentences (filename):
    with open (filename, "r") as file:
        content = file.read()
        sentences = re.split(r"[.?!]+", content)

        sentences_length = len(sentences)
        return sentences_length
    
def find_common_words (filename):
    with open (filename, "r") as file:
        content = file.read()
        words = content.split()

        words_count = {}
        for word in words:
            words_count[word] = words_count.get(word, 0) + 1

        most_common_words = sorted(words_count.items(), key=lambda x: x[1], reverse=True)[:3]
        return most_common_words

def calculate_average_length (filename):
    with open (filename, "r") as file:
        content = file.read()
        destructured = content.split()

        total_length = 0

        for word in destructured:
            total_length += len(word)

        average_length = total_length // len(destructured)
        return average_length
    
def find_longest_word (filename):
    with open (filename, "r") as file:
        content = file.read()
        destructured = content.split()

        longest_word = ''
        longest_word_length = 0

        for word in destructured:
            if len(word) > longest_word_length:
                longest_word_length = len(word)
                longest_word = word
            else:
                continue

        return longest_word_length, longest_word

filename = input("Enter file name:\n")

line_count, word_count = count_words_lines(filename)
sentences = count_sentences(filename)
most_common_words = find_common_words(filename)
average_length = calculate_average_length(filename)
longest_word_length, longest_word = find_longest_word(filename)

print(f"The word count for {filename} is {word_count} and line count is {line_count}")
print(f"Number of sentences = {sentences}")
print(f"Most Common Words:{[word[0] for word in most_common_words]}")
print(f"The Average length of words is {average_length}")
print(f"Longest Word in the file is {longest_word} and length is {longest_word_length}")