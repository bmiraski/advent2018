"""Determine answers for Day 6 in advent calendar."""


def manhattan(x1, y1, x2, y2):
    """Calculate the Manhattan distance between two points."""
    return (abs(y2 - y1) + abs(x2 - x1))
