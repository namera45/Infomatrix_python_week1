def find_chars_with_frequency_less_than_2(input_string):
    char_frequency = {}
    for char in input_string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    result = [char for char, freq in char_frequency.items() if freq < 2]
    return result


input_string = input("Enter a string: ")
result = find_chars_with_frequency_less_than_2(input_string)
print("Characters with frequency less than 2:", result)
