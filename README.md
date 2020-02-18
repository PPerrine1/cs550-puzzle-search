# (A3) N Puzzle Search
In this assignment, you will write a generic graph search routine that can be used to conduct *breadth-first, depth-first, and A-star search* by varying the parameters given to it.  Several classes are provided to you in package basicsearch_lib02 to help you in this endeavor and you are required to use them.  Do not support multiple solution states for this assignment.

## Skeleton Code (Provided)

**driver02.py** – The driver module should create 31 different tile board puzzles. For each of these, a solution will be searched using breadth first, depth first, and A-star search using a Manhattan distance heuristic.  Keep track of the number of nodes expanded and the amount of time used for each of these.  Upon completion, print a table summary that indicates the mean (average) and standard deviation of the following measurements:

* length of plan (number of steps to solution)
* number of nodes expanded
* elapsed time in seconds.  Use tic/tock functions provided: t=tic(), tock(t)

Running the 31 trials will take a little bit of time, so use a much smaller number when debugging.  One execution of the 31 trials on an Intel i7-9700U took a little under 19 minutes without exploiting multiple cores (duration depends on the difficulty of the randomly generated puzzles) and it is recommended that you make sure that each search type is working before you try to start looping on solutions.

**npuzzle.py** – Partially completed class to represent the problem, derived from a generic Problem representation in basicsearch_lib02.searchrep.  Complete the skeleton code that is provided for you.  When you create a problem to be searched, you should create an instance of this class which will contain an instance of TileBoard.  The parent class, Problem, accepts two keyword arguments that you will need to use (don’t forget to call super):  g and h.  g is a cost function and h is a heuristic function.  See descriptions in modules searchstrategies specified below.  You can pass a function handle by using the name of the function, e.g. g=BreadthFist.g.

**problemsearch.py** – Implement function graph_search.  It takes an instance of NPuzzle and flags for controlling verbosity and debugging (see file for details) and conducts a search.  When instantiating the NPuzzle, be sure to use parent class’s g and h arguments to set the path cost and heuristic functions which will govern the type of search that is conducted.  It returns a 3 tuple consisting of: 

* a plan (list of actions) 
* the number of nodes that were expanded. 
* the amount of time the search took 

You will need to use a priority queue and search nodes (see below)

**searchstrategies.py** – Implement classes BreadthFirst, DepthFirst, and Manhattan.  These are classes that provide implementations for the cost to node (g) and cost from node to goal heuristic (h) functions.  Note g and h are class methods (see details on class methods in the comments of the provided code) and that when you pass them to the NPuzzle constructor, you need to pass the function handles to the constructor rather than invoking the function.  Concretely, if you wanted to pass BreadthFirst’s function handle for g to NPuzzle, you would call NPuzzle(num_tiles, g=BreadthFirst.g, ... ).  NPuzzle’s parent class stores g in a publicly accessible instance variable and other code (e.g. the Node class discussed below) will invoke the functions to evaluate search nodes.  Note that we defined DepthFirst’s g as a constant and h as the negative depth.  The structure of the Node implementation expects h to be called with a single argument:  state.  As the depth is captured in the Node, and not the state, reverse the roles of g and h when implementing DepthFirst.  The depth can be accessed from the g function which expects a parent, action, and the search node itself.

**explored.py** – Implement class Explored.  Apart from the no argument constructor, it has two methods:  exists(state) and add(state).  Both of these expect state tuples from a TileBoard and use a hash table to determine whether a state has been seen before (exists) and to add new states as they are removed from the frontier set (add).  The Python builtin hash will generate a hash key from any hashable value.  Handle hash key collisions as a bucket list.The module basicsearch_lib02 contains several functions that you should use in your implementation.  

### Do not make any changes to these:

**basicsearch_lib02.queues.py** – Class PriorityQueue should be used to maintain the order of the queue.  Remember, we defined g and h in a way that priority queues can be used all search types and f(node) = g(node)+h(node).  Order your queue by f(node).

**basicsearch_lib02.searchrep.py** – This module contains classes that will be useful in representing search problems and trees.

The Problem class represents a generic problem class that should be the parent of your NPuzzle class, and as stated has constructor arguments for specifying the g and h functions.  Class Node should be used to construct a node in the search space, and these are the objects that should be generated in your search.  To create the first node, call the constructor with instances of the problem representation, NPuzzle, and the initial state (a TileBoard).  To obtain the list of new search states obtainable from a search node, call expand with an instance of the problem.  It will use the problem’s actions method to determine the possible actions that can be generated and derive new child nodes.  Node’s get_f function will be useful for maintaining the order of your priority queue.  While you need not modify anything in the library, be sure that you understand how this is working.  Step through the code with a debugger if you cannot follow it by reading.   Finally, searchrep provides function print_nodes that takes a list of search nodes and prints out their puzzle representations on a single line.  You may find this useful for debugging, but otherwise the function provides no purpose.

## Remember to submit:

* Affidavit
* Hard copy of your code including newtonraphson.py and output of tables and one path to solution and board representations using A*.  Pair programmers:  Submit your code and questions together.
* Submit code to Blackboard (problem 1 and the N-Puzzle code excluding libraries).  Pair programmers:  Submit only one copy to either account.

### Other Notes

* Do not solve for multiple solution puzzles!
* Once you have your code, run the 31 tests, and then take statistics on them.
* A-star will outperform all other searches.
* You should show that Manhattan Distance is a consistent heuristic.