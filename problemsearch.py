"""
problemsearch - Functions for seaarching.
"""

from basicsearch_lib02.searchrep import (Node, print_nodes)
from basicsearch_lib02.queues import PriorityQueue
from explored import Explored


def graph_search(problem, verbose=False, debug=False):
    """graph_search(problem, verbose, debug) - Given a problem representation
      (instance of basicsearch_lib02.representation.Problem or derived class),
      attempt to solve the problem.
      
      If debug is True, debugging information will be displayed.
      
      if verbose is True, the following information will be displayed:
      
      Number of moves to solution
      List of moves and resulting puzzle states
      Example:
      
            Solution in 25 moves        
            Initial state
                  0        1        2    
            0     4        8        7    
            1     5        .        2    
            2     3        6        1    
            Move 1 -  [0, -1]
                  0        1        2    
            0     4        8        7    
            1     .        5        2    
            2     3        6        1    
            Move 2 -  [1, 0]
                  0        1        2    
            0     4        8        7    
            1     3        5        2    
            2     .        6        1    
            
            ... more moves ...
            
                  0        1        2    
            0     1        3        5    
            1     4        2        .    
            2     6        7        8    
            Move 22 -  [-1, 0]
                  0        1        2    
            0     1        3        .    
            1     4        2        5    
            2     6        7        8    
            Move 23 -  [0, -1]
                  0        1        2    
            0     1        .        3    
            1     4        2        5    
            2     6        7        8    
            Move 24 -  [1, 0]
                  0        1        2    
            0     1        2        3    
            1     4        .        5    
            2     6        7        8    
      
      If no solution were found (not possible with the puzzles we
      are using), we would display:
      
      No solution found

      Returns a tuple (path, nodes_explored) where:
      path - list of actions to solve the problem or None if no solution was found
      nodes_explored - Number of nodes explored (dequeued from frontier)
      """
    initial_node = Node(problem, problem.puzzle.state_tuple())
    frontier = PriorityQueue()
    frontier.append(initial_node)

    explored = Explored()
    nodes_explored = 0

    done = found = False
    while not done:
        node = frontier.pop()
        if debug:
            print("Node:", node)
            print("Frontier:", frontier)

        state = node.state
        explored.add(state)
        nodes_explored += 1

        if problem.goal_test(state):
            found = done = True
        else:
            for act in problem.actions(state):
                next_state = problem.result(state, act)
                if next_state not in frontier and not explored.exists(next_state):
                    frontier.append(node.child_node(act))

    if not found:
        print("No solution found.")
    else:
        if verbose:
            print("Solution in", len(node.solution()), "moves")
            print(problem.puzzle)
            for i, act in enumerate(node.solution()):
                problem.puzzle = problem.puzzle.move(act)
                act.reverse()
                print("Move", i + 1, "-", act)
                print(problem.puzzle)

        if debug:
            print("*" * 10, "Win")

        return node.solution(), nodes_explored
