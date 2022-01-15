# Udacity-PROBLEMS-VS-ALGORITHMS

Submission to Udacity's PROBLEMS-VS-ALGORITHMS Problems

Run time analysis (Worst Case Big-O Notation) of solution

Get Time Taken to run using : time python <filename>

- Design choices -

  - This problem requires i use the trie data structure method to add routes, handlers and be able to look them up.

- TASK 7 : 0(n)

  - Space complexity analysis-

    - RouteTrie
      - root = 0(1)
    - RouteTrieNode
      - handler = 0(1)
      - children = 0(n)
    - Router
      - route_trie = 0(1) ref(RouteTrie-root)
      - self.route_trie.root.handler = 0(1) ref (RouteTrieNode-handler)

  - Logic explanation - Time complexity analysis-
  - Algorithm for Router :

    - add handler : get routes and insert routes to route trie node 0(1)
    - lookup : split path to return found routes list and find handler in route trie nodes children 0(1)
    - split path : split paths 0(1), traverse routes list and remove empty elements 0(n), then return routes list

  - Algorithm for RouteTrie :

    - insert : 0(1)
    - insertRec : 0(n)
    - find : traverse through routes to return handler 0(n)

  - Algorithm for RouteTrieNode :

    - insert : insert node to the current children route 0(1)

  - Modular Algorithm :
    - Create Router = 0(1)
    - add Handler = 0(1)
    - look up = 0(1)
