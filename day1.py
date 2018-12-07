"""Compute Day 1 Advent Calendar tasks."""


def defineChangeSet():
    """Create a list of frequency changes to iterate over."""
    changes = []
    with open('input.txt') as g:
        dataset = g.readlines()
    for line in dataset:
        if line[0] == '+':
            change = int(line[1:])
        else:
            change = int(line)
        changes.append(change)
    return changes


def frequencyLoop(changes, total, totals):
    """Continue to loop the change set until a matching total is found."""
    for item in changes:
        total += item
        if total in totals:
            print(f"The repeated total is {total}.")
            return
        else:
            totals.append(total)
    print(f'Finished loop with total: {total}')
    frequencyLoop(changes, total, totals)

changes = defineChangeSet()
frequencyLoop(changes, 0, [])
