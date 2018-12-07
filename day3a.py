"""Solve day 3a on the advent calendar."""


def createCanvas(size):
    """Create a square canvas of a given size."""
    arr = []
    for x in range(size):
        row = []
        for y in range(size):
            row.append('.')
        arr.append(row)
    return arr


def cleandata(dataset):
    """Create a clean set of coordinates and ids."""
    cleandset = []
    for line in dataset:
        id, col, row, xsize, ysize = "", "", "", "", ""
        atloc, comloc, colloc, xloc = 0, 0, 0, 0
        for x in range(len(line)-1):
            if line[x] == '@':
                atloc = x
            elif line[x] == ',':
                comloc = x
            elif line[x] == ':':
                colloc = x
            elif line[x] == 'x':
                xloc = x
            else:
                continue
            id = line[1:atloc].strip()
            col = line[atloc+1:comloc].strip()
            row = line[comloc+1:colloc].strip()
            xsize = line[colloc+1:xloc].strip()
            ysize = line[xloc+1:].strip()
        datarow = (id, col, row, xsize, ysize)
        cleandset.append(datarow)
    return cleandset


def createCoordinates(dataset):
    """Create a group of thruples to be used to populate canvas."""
    coords = []
    for row in dataset:
        for x in range(int(row[3])):
            for y in range(int(row[4])):
                a = (int(row[0]), int(row[1]) + x, int(row[2]) + y)
                coords.append(a)
    return coords


def markCanvas(canvas, coords):
    """Mark locations on canvas based on coordinates."""
    endcanvas = canvas
    for item in coords:
        if endcanvas[item[2]][item[1]] == '.':
            endcanvas[item[2]][item[1]] = item[0]
        elif endcanvas[item[2]][item[1]] != 'X':
            endcanvas[item[2]][item[1]] = 'X'
        else:
            continue
    return endcanvas


def countx(canvas):
    """Count the number of 'X' in canvas."""
    count = 0
    for row in canvas:
        for item in row:
            if item == 'X':
                count += 1
    return count


with open('inputday3.txt') as f:
    dataset = f.readlines()

canvas = createCanvas(1000)
# print(canvas)

cleanset = cleandata(dataset)
# print(cleanset)

coords = createCoordinates(cleanset)
# print(coords)

marked_canvas = markCanvas(canvas, coords)
# print(marked_canvas)

print(countx(marked_canvas))
