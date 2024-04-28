"""Methods and functions for working with Linked Lists, Node, and Recursion."""

from __future__ import annotations
 
__author__ = "730411985"
 
 
class Node:
    """An item in a singly-linked list."""
    data: int
    next: Node | None
 
    def __init__(self, data: int, next: Node | None):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next
 
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """Returns data attribute for first element in linked list."""
        return self.data
    
    def tail(self) -> Node | None:
        """Returns a linked list of every element except head."""
        return self.next  # return none if len(linked list) = 1
    
    def last(self) -> int:
        """Return data of last element in linked list."""
        if self.next is None:
            return self.data
        else:
            current = self
            while current.next is not None:
                current = current.next
            return current.data


def value_at(head: Node | None, index: int) -> int:
    """Return data of Node stores at given index."""
    if head is None:  # edge case when list is empty
        raise IndexError("Index is out of bounds on the list.")  
    if index == 0:  # base case at index 0: return data of current Node
        return head.data
    return value_at(head.next, index - 1)  # modify head by moving to next and index by adding 1 to get closer to base


def max(head: Node | None) -> int:
    """Return maximum data in linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    max_value: int = head.data  # store max value, starting with base
    current: Node | None = head  # index to move through linked list
    while current is not None:
        if current.data > max_value:  # compare stored max to current
            max_value = current.data
        current = current.next  # move to next Node
    return max_value


def linkify(items: list[int]) -> Node | None:
    """Return linked list of Nodes with same vals in same order as input list."""
    if not items:  # list is empty: base case
        return None
    head = Node(items[0], None)  # head node is first element in list
    current = head
    for item in items[1:]:  # python slice notation instead of len(items)
        current.next = Node(item, None)
        current = current.next  # link nodes
    return head


def scale(head: Node | None, factor: int) -> Node | None:
    """Makes new linked list of Nodes with each value in og multipled by factor."""
    if head is None:  # base case for empty list
        return None
    scaled_data: int = head.data * factor  # new node with data multiplied by factor
    scaled_next: Node | None = scale(head.next, factor)
    scaled_node: Node = Node(scaled_data, scaled_next)
    return scaled_node