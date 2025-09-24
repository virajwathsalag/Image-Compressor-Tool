import collections
def create_deque(iterable=None):
    if iterable is not None:
        return collections.deque(iterable)
    else:
        return collections.deque()
