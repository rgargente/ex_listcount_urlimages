def simple_count(l):
    """
    This is simple, sequential, O(n) algorithm to get the size of a list.
    Good for small lists.
    """
    count = 0
    while True:
        try:
            l[count]
            count += 1
        except:
            break
    return count


def binsearch_count(l):
    """
    This is a kind of binary search algorithm to search for the size of a list.
    First it tries to find a size that is too big then coverges the minimum and maximum valid indexes until
    it finds the size.

    WARNING: Does not work with empty lists! This is only optimized for large lists.
    """

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


def smart_count(l):
    """Counts a list using the right algorithm according to size."""
    MAX_SIMPLE_SIZE = 100  # Decided using the benchmarks in the test folder
    try:
        l[MAX_SIMPLE_SIZE]
        return binsearch_count(l)
    except:
        return simple_count(l)
