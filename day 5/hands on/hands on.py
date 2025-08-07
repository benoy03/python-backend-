
words = input("Enter words separated by spaces: ").split()


unique_words = set(words)
print("Unique words:", unique_words)
def count_words(word_list):
    freq = {}
    for word in word_list:
        freq[word] = freq.get(word, 0) + 1
    return freq


frequency = count_words(words)
print("Word frequency:", frequency)

dict1 = {'apple': 2, 'banana': 2}
dict2 = {'banana': 1, 'apple': 1, 'cherry': 3}


merged_dict = dict1.copy()
for key, value in dict2.items():
    if (existing := merged_dict.get(key)) is not None:
        merged_dict[key] = existing + value
    else:
        merged_dict[key] = value

print("Merged dictionary:", merged_dict)
