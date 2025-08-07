print("\n--- Exercise 4: Combined Challenge ---")


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = {}

for key in dict1.keys() | dict2.keys():
    val1 = dict1.get(key)
    val2 = dict2.get(key)

    if (val1 is not None) and (val2 is not None):
        merged[f"{key}_resolved"] = val1 + val2
    else:
        merged[key] = val1 if val1 is not None else val2

print("4.1 Merged dictionary with conflict resolution:", merged)