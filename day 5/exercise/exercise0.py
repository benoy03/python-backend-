
words1 = input("Enter first list of words (separated by spaces): ").split()
words2 = input("Enter second list of words (separated by spaces): ").split()

unique_words1 = set(words1)
unique_words2 = set(words2)
print("\nUnique words in list 1:", unique_words1)
print("Unique words in list 2:", unique_words2)


def count_words(word_list):
    freq = {}
    for word in word_list:
        freq[word] = freq.get(word, 0) + 1
    return freq

freq_dict1 = count_words(words1)
freq_dict2 = count_words(words2)

print("\nWord frequencies in list 1:", freq_dict1)
print("Word frequencies in list 2:", freq_dict2)


merged_dict = freq_dict1.copy()

for key, value in freq_dict2.items():
    if (existing := merged_dict.get(key)) is not None:
        merged_dict[key] = existing + value
    else:
        merged_dict[key] = value

print("\nMerged dictionary with resolved conflicts:", merged_dict)
