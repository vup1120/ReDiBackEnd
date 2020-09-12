import string


def split_words(key):
    key = key.lower()  # convert all the words in lower case to be regonised as the same words (ex: "The" and "the")
    translator = str.maketrans('', '', string.punctuation)
    key = key.translate(translator)
    words = key.split()
    return words


def freq_appearance(key):
    words = split_words(key)
    unique_words = set(words)
    words_count = []
    for i in unique_words:
        count = words.count(i)
        words_count.append((i, count))
    return words_count

def most_freq(key):
    words_count = freq_appearance(key)
    cout_list = [i[1] for i in words_count]
    m = max(cout_list)
    idx = [i for i, j in enumerate(cout_list) if j == m]
    most_freq_words = [words_count[i][0]for i in idx]
    most_freq_words = ' '.join(sorted(most_freq_words))
    return(most_freq_words)

def main():
    key = str(input("Enter the string: "))
    print(most_freq(key))

main()
