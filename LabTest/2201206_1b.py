import collections

def analyze_text(filename):
    with open(filename, 'r') as f:
        text = f.read()
        words = text.split()
        num_lines = text.count('\n')
        num_spaces = text.count(' ')
        num_words = len(words)
        unique_words = len(set(words))
        word_freq = collections.Counter(words)
        longest_word = max(words, key=len)
        avg_word_length = sum(len(word) for word in words) / num_words

    print(f"Total number of words: {num_words}")
    print(f"Total number of lines: {num_lines+1}")
    print(f"Total number of spaces: {num_spaces}")
    print(f"Number of unique words: {unique_words}")
    print(f"Frequency of each word: {word_freq}")
    print(f"Longest word: {longest_word}")
    print(f"Average word length: {avg_word_length}")

def compare_texts(filename1, filename2):
    with open(filename1, 'r') as f1, open(filename2, 'r') as f2:
        text1 = f1.read()
        text2 = f2.read()

    if text1 == text2:
        return 1
    else:
        return 0

if __name__ == "__main__":
    filename1 = "LabTest/text1.txt"
    filename2 = "LabTest/text2.txt"
    analyze_text(filename1)
    result = compare_texts(filename1, filename2)
    if result == 1:
        print("The two files are identical")
    elif(result == 0):
        print("The two files are different")
    else:
        print("Error: Invalid result")