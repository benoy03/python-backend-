
def second_largest(lst):
    unique = list(set(lst))
    if len(unique) < 2:
        return None
    unique.sort()
    return unique[-2]

nums = list(map(int, input("Enter numbers to find second-largest (space-separated): ").split()))
result = second_largest(nums)

if result is not None:
    print("Second-largest number is:", result)
else:
    print("Not enough unique numbers.")


def parse_dict(pairs):
    return {k: int(v) for item in pairs for k, v in [item.split(":")]}

print("\nEnter two dictionaries (format: key:value):")
dict1_input = input("First dictionary (e.g., a:1 b:2): ").split()
dict2_input = input("Second dictionary (e.g., b:3 c:4): ").split()

dict1 = parse_dict(dict1_input)
dict2 = parse_dict(dict2_input)

merged = dict1 | dict2 
print("Merged dictionary:", merged)
