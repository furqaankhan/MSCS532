def insertion_sort(numbers):
    for index in range(1, len(numbers)):
        key = numbers[index]
        position = index - 1

        while position >= 0 and numbers[position] < key:
            numbers[position + 1] = numbers[position]
            position -= 1

        numbers[position + 1] = key

    return numbers


examples = [
    [5, 2, 9, 1, 5, 6],
    [9, 7, 4, 2],
    [4, 2, 4, 1, 2],
]

for example in examples:
    original = example.copy()
    sorted_numbers = insertion_sort(example)
    print(f"Original: {original}")
    print(f"Sorted:   {sorted_numbers}")
    print()
