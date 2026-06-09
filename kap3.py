from collections import Counter

# Given list
L1 = [1, 2, 2, 3, 2, 3, 4, 5]

# Count frequency of each element
counter = Counter(L1)

# Find the most common element
most_common_element, frequency = counter.most_common(1)[0]

print(f"The most repetitive element is {most_common_element} with {frequency} occurrences.")
