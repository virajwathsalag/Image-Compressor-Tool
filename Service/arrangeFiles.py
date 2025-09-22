import collections
def create_deque(iterable=None):
    """
    Creates and returns a collections.deque object.

    Args:
        iterable (optional): An iterable to initialize the deque.
                             If not provided, an empty deque is returned.

    Returns:
        collections.deque: A new deque instance.
    """
    if iterable is not None:
        return collections.deque(iterable)
    else:
        return collections.deque()
