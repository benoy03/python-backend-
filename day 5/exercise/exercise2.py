print("\n--- Exercise 2: Dictionaries ---")


student = {
    "name": "John Doe",
    "age": 20,
    "courses": ["Math", "Science", "History"]
}
print("2.1 Student dictionary:", student)


text = "hello world hello"
words = text.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("2.2 Word frequency:", frequency)


squares = {x: x**2 for x in range(1, 6)}
print("2.3 Squares dictionary:", squares)