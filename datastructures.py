"""Data Structures"""

class LinkedList:
    """Linked List Data Structure"""
    
    class Node:
        ''"Node in a data structure"""
        
        def _init__(self):
            """Constructor"""
            self.data = None
            self.next = None
            
    def _init_ (self):
        """Constructor""" 
        self._head - None 
        self._tail - None 
        self._size - 0
        
    @property 
    def is_empty(self):
        """Whether the linked list empty or not."""
        return self._head is None
    

    @property
    def size(self):
        """Property for size"""
        return self._size

    def add_to_front(self, data):
        """Add a new element to the front of the linked list"""
         # Make a new variable to also reference the head of the list
        old_head = self._head
        # Make a new node and assign it to the head variable
        self._head = self.Node()
        # Set the data on the new node
        self._head.data = data
         # Make the next property of the node point to the old head
        self._head.next = old_head
        # Increment the size of the list
        self._size += 1
        # Ensure that if we are adding the very first node to the linked list
        # the tail will be pointing to the new node we create
        if self._size == 1:
            self._tail = self._head

    def add_to_back(self, data):
        """Add a new element to the back of the linked list"""
        # Make a pointer to the tail called old_tail
        old_tail = self._tail
        # Make a new node and assign it to the tail variable
        self._tail = self.Node()
        # Assign the data and set the next pointer
        self._tail.data = data
        self._tail.next = None  # Not needed since constructor sets it. Shown for clarity.
        # Increment the size
        self._size += 1
        # Check to see if the list is empty. If so, make the head point to the
        # same location as the tail.
        if self._size == 1:
            self._head = self._tail
        else:
            old_tail.next = self._tail

    def remove_from_front(self, data):
        """Remove an element from the front of the linked list"""
        # If the list is empty, raise an error
        if self.is_empty:
            raise IndexError("Nothing to remove. List is empty.")
        
        # Let's get the data to return
        data = self._head.data
         # Move the head pointer to the next in the list
        self._head = self._head.next
        # Decrease the size of the list
        self._size -= 1
        # Check to see if we just removed the last node from the list
        if self.is_empty():
            # If so, tail needs to be set to None
            self._tail = None
    
        # Return the data from the removed node
        return data

    def remove_from_back(self, data):
        """Remove an element from the back of the linked list"""
        # If the list is empty raise an error
        if self.is_empty:
            raise IndexError("Nothing to remove. List is empty")


            #Get the data to return
            data = self._tail.data

            # Decrease the size of the list
            self._size -= 1

            # Return the data
            return data

    def __str__(self):
        """String method."""

    