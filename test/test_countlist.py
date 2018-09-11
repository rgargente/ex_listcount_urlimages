"""
1. Count the number of elements in a list without using count, size or length operators (or their equivalents).
Assume the list only can be asked for an element at a certain position,
make sure this is efficient for extreme large lists as well.

Provide a couple of sentences describing the reasoning behind your approach.
"""
from countlist import simple_count, binsearch_count,smart_count
import pytest


def test_zero():
    assert 0 == simple_count([])
    assert 0 == binsearch_count([])

def test_one():
    assert 1 == simple_count(['a'])
    assert 1 == binsearch_count(['a'])


@pytest.mark.parametrize("size", [5, 100, 230, 231, 232, 1000])
def test_simple_count(size):
    assert size == simple_count([0] * size)


def test_simple_count_exhaustive():
    for i in range(1000):
        l = [0] * i
        assert len(l) == simple_count(l)


@pytest.mark.parametrize("size", [5, 100, 999])
def test_binsearch(size):
    assert size == binsearch_count([0] * size)

def test_binsearch_exhaustive():
    for i in range(1000)[1:]: # We skip 0 because binsearch is not working with empty lists
        l = [0] * i
        assert len(l) == binsearch_count(l)


def test_smart_count_exhaustive():
    for i in range(1000):
        l = [0] * i
        assert len(l) == smart_count(l)