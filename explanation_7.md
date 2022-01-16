# Udacity-PROBLEMS-VS-ALGORITHMS

Submission to Udacity's PROBLEMS-VS-ALGORITHMS Problems

Run time analysis (Worst Case Big-O Notation) of solution

Get Time Taken to run using : time python <filename>

- Design choices -

  - This problem requires i use the trie data structure method to add routes, handlers and be able to look them up.

- TASK 7 : 0(n)

  - Logic explanation - Time complexity analysis - Space complexity analysis -
  - Algorithm for Router :

    - _init_ method in Router class

      - Space : 0(1)
      - Time : 0(1)

    - add handler method in Router class:

      - Space : 0(1)
      - Time : 0(1) - get routes and insert routes to route trie node 0(1)

    - lookup in method Router class :

      - Space : 0(1)
      - Time : 0(1) - split path to return found routes list and find handler in route trie nodes children 0(1)

    - split path method in Router class :
      - Space : 0(1)
      - Time : 0(n) - split paths 0(1), traverse routes list and remove empty elements 0(n), then return routes list

  - Algorithm for RouteTrie :

    - _init_ method in RouteTrie class
      - Space : 0(1)
      - Time : 0(1)

    - insert in method RouteTrie class

      - Space : 0(1)
      - Time : 0(1) insert routes and handler

    - insertRec in method RouteTrie class
      - Space : 0(n) where n is the length of the routes to be inserted since we need to perform n recursive traversal.
      - Time : 0(n) recursively insert route into children
    - find method in RouteTrie class
      - Space : 0(1)
      - Time : 0(n) traverse through routes to return handler 0(n)

  - Algorithm for RouteTrieNode :
    - Insert in RouteTrieNode class
      - Space : 0(1)
      - Time : 0(1) insert in children dictionary using route as key and handler as value
