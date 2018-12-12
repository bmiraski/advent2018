"""Solve advent calendar Day 5 problems."""
from collections import defaultdict


def removereactions(data):
    """Remove reactive characters from strings."""
    x = 0
    while ((x+2) <= len(data)):
        start_len = len(data)
        if data[x].islower():
            if data[x+1].isupper():
                if data[x] == data[x+1].lower():
                    data = data[:x] + data[x+2:]
                    # print(len(data))
                    # print(data)
        elif data[x].isupper():
            if data[x+1].islower():
                if data[x].lower() == data[x+1]:
                    data = data[:x] + data[x+2:]
                    # print(len(data))
                    # print(data)
        if len(data) < start_len:
            x = max(0, x-2)
        else:
            x += 1
    return data


def remove_letter(letter, data):
    """Remove a specific letter from a data string."""
    letter_list = [letter.lower(), letter.upper()]
    input_list = []
    for char in data:
        input_list.append(char)
    new_data = []
    for item in input_list:
        if item in letter_list:
            new_data.append('')
        else:
            new_data.append(item)
    new_string = ""
    for item in new_data:
        new_string += item
    return new_string


with open('inputday5.txt') as f:
    data = f.readlines()

data = data[0][:len(data[0])-1]
# print(data)

getsmallstring = removereactions(data)

print(len(getsmallstring))

letters = "abcdefghijklmnopqrstuvwxyz"
output = defaultdict(int)
for letter in letters:
    alter_data = data
    alter_data = remove_letter(letter, alter_data)
    output[letter] = len(removereactions(alter_data))

print(output)
print(sorted(output.values()))
