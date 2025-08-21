

def word_ascii_dict(words):
    return {word: {ch: ord(ch) for ch in word} for word in words}


words = ["hi", "cat"]
print(word_ascii_dict(words))

