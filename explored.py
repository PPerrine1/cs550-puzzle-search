"""

@author: mroch
"""


class Explored(object):
    """Maintain an explored set.  Assumes that states are hashable"""

    # TODO: Implement class Explored. Apart from the no argument constructor, it has two methods: exists(state) and
    #  add(state). Both of these expect state tuples from a TileBoard and use a hash table to determine whether a
    #  state has been seen before (exists) and to add new states as they are removed from the frontier set (add). The
    #  Python builtin hash will generate a hash key from any hashable value. Handle hash key collisions as a bucket
    #  list. The module basicsearch_lib02 contains several functions that you should use in your implementation.

    def __init__(self):
        """__init__() - Create an empty explored set"""
        explored = {}
        # raise NotImplemented

    def exists(self, state):
        """exists(state) - Has this state already been explored?
        Returns True or False, state must be hashable
        """
        if hash(state) in self.explored and state in self.explored[hash(state)]:
            return True
        else:
            return False

        raise NotImplemented

    def add(self, state):
        """add(state) - add given state to the explored set.  
        state must be hashable and we asssume that it is not already in set
        """
        if hash(state) in self.explored:
            self.explored[hash(state)].append(state)
        else:
            self.explored[hash(state)] = [state]
        # The hash function is a Python builtin that generates
        # a hash value from its argument.  Use this to create
        # a dictionary key.  Handle collisions by storing 
        # states that hash to the same key in a bucket list.
        # Note that when you access a Python dictionary by a
        # non existant key, it throws a KeyError

        raise NotImplemented
