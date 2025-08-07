print("\n--- Exercise 1: Sets ---")


nums = [3, 5, 7, 5, 9, 3]
unique_nums = list(set(nums))
print("1.1 Unique values:", unique_nums)


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("1.2 Union (A ∪ B):", A | B)
print("1.2 Intersection (A ∩ B):", A & B)
print("1.2 Difference (A - B):", A - B)
print("1.2 Symmetric Difference (A ∆ B):", A ^ B)


text = "apple banana apple cherry banana"
words = text.split()
unique_words = set(words)
print("1.3 Unique words:", unique_words)
print("1.3 Count of unique words:", len(unique_words))