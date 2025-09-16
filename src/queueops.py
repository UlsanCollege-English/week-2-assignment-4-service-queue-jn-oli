# src/queueops.py

from typing import List, Tuple, Optional


def take_next(queue: List[str]) -> Tuple[Optional[str], List[str]]:
    """
    Take the next element from the front of the queue.
    Returns (element, new_queue).
    If the queue is empty, returns (None, []).
    """
    if not queue:
        return None, []
    return queue[0], queue[1:]


def move_to_back(queue: List[str], name: str) -> List[str]:
    """
    Move the first occurrence of `name` to the back of the queue.
    If `name` is not in the queue, return the queue unchanged.
    """
    if name not in queue:
        return queue[:]  # unchanged copy

    new_queue = []
    moved = False
    for person in queue:
        if person == name and not moved:
            moved = True  # skip first occurrence
            continue
        new_queue.append(person)

    new_queue.append(name)
    return new_queue


def interleave(q1: List[str], q2: List[str]) -> List[str]:
    """
    Interleave two queues element by element.
    Any leftover elements are appended at the end.
    """
    result = []
    i, j = 0, 0

    while i < len(q1) and j < len(q2):
        result.append(q1[i])
        result.append(q2[j])
        i += 1
        j += 1

    # Append leftovers
    if i < len(q1):
        result.extend(q1[i:])
    if j < len(q2):
        result.extend(q2[j:])

    return result
