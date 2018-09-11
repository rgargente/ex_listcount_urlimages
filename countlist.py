from typing import List


def simple_count(l: List):
    count = 0
    while True:
        try:
            l[count]
            count += 1
        except:
            break
    return count


def binsearch_count(l: List):
    """WARNING: Does not work with empty lists! This is only optimized for large lists. """
    def get_middle(min, max):
        return int(min + (max - min) / 2)

    min = 0
    max = 10
    i = max
    overboard = False

    while (max - min) > 1:
        if overboard:  # converge min and max to find the solution
            try:
                l[i]
                min = i
            except:
                max = i
            i = get_middle(min, max)
        else:  # still havent found the max
            try:
                l[max]
                min = max
                max *= 10
            except:  # we found our max
                overboard = True
                i = get_middle(min, max)
    return max
