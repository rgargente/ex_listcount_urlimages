import pytest

from countlist import simple_count, binsearch_count


@pytest.mark.parametrize(
    "size, function", [
        (10, simple_count),
        (10, binsearch_count),
        (100, simple_count),
        (100, binsearch_count),
        (1000, simple_count),
        (1000, binsearch_count),
    ]
)
def test_big_list(size, function, benchmark):
    """
    This is a benchmarking test to decide when to change from the simple_count algorithm to the binary search one.
    We can see that it is already faster but on the same order of magnitude at 100 elements, so we will use that
    value.
    We can also observe how the binary search time is growing much slower than the simple search because
    the simple search has O(n) complexity while the binary search has O(log n)
    """
    l = int(size) * [0]
    assert len(l) == benchmark(function, l)

