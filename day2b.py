"""Determine the second solution to day 2."""


def compStrings(string1, string2):
    """Compare two strings to determine if more than one char is different."""
    print(f"Checking {string1} and {string2}")
    badchar = 0
    for x in range(0, len(string1)):
        if string1[x] != string2[x]:
            badchar += 1
            if badchar == 2:
                print("Didn't match")
                return False
            continue
        else:
            continue
    print("Close Match Found.")
    return True


def finalString(string1, string2):
    """Create the final string that is needed."""
    for x in range(0, len(string1)):
        if string1[x] == string2[x]:
            continue
        else:
            final_string = string1[0:x] + string1[x+1:]
            return final_string


with open('inputday2.txt') as f:
    dataset = f.readlines()

cleandata = []
for item in dataset:
    item = item[0:26]  #  needs to be 26 for real, 5 for test
    cleandata.append(item)

string1 = ""
string2 = ""

compareset = cleandata

while string1 == "":
    for item in cleandata:
        compareset.remove(item)
        for compitem in compareset:
            if not compStrings(item, compitem):
                continue
            else:
                string1 = item
                string2 = compitem
                break
        break

finalOutput = finalString(string1, string2)
print(finalOutput)
