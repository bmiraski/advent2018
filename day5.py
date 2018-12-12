"""Solve advent calendar Day 5 problems."""


def removereactions(data):
    """Remove reactive characters from strings."""
    x = 0
    while ((x+2) <= len(data)):
        start_len = len(data)
        if data[x].islower():
            if data[x+1].isupper():
                if data[x] == data[x+1].lower():
                    data = data[:x] + data[x+2:]
                    print(len(data))
                    # print(data)
        elif data[x].isupper():
            if data[x+1].islower():
                if data[x].lower() == data[x+1]:
                    data = data[:x] + data[x+2:]
                    print(len(data))
                    # print(data)
        if len(data) < start_len:
            x = max(0, x-2)
        else:
            x += 1
    return data


with open('inputday5.txt') as f:
    data = f.readlines()

data = data[0][:len(data[0])-1]
print(data)

getsmallstring = removereactions(data)

print(len(getsmallstring))

# print(getsmallstring[0].capitalize())
# print(getsmallstring[1])
# print(getsmallstring[0].capitalize() == getsmallstring[1])
