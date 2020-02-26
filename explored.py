"""

@author: mroch
"""


class Explored(object):
    """Maintain an explored set.  Assumes that states are hashable"""

    def __init__(self):
        """__init__() - Create an empty explored set"""
        self.explored = {}

    def exists(self, state):
        """exists(state) - Has this state already been explored?
        Returns True or False, state must be hashable
        """
        key = hash(state)  # Store key value

        # Check explored set for key and state
        if key in self.explored and state in self.explored[key]:
            return True
        return False

    def add(self, state):
        """add(state) - add given state to the explored set.  
        state must be hashable and we asssume that it is not already in set
        """
        key = hash(state)  # Store key value

        # If key exists, append state.
        # #Else, create key with empty list and append state.
        self.explored.setdefault(key, []).append(state)

        # The hash function is a Python builtin that generates
        # a hash value from its argument.  Use this to create
        # a dictionary key.  Handle collisions by storing 
        # states that hash to the same key in a bucket list.
        # Note that when you access a Python dictionary by a
        # non existant key, it throws a KeyError

