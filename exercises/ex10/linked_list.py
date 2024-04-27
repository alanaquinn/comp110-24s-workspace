"""Utility functions for working with Linked Lists."""

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