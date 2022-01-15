# Udacity-PROBLEMS-VS-ALGORITHMS

Submission to Udacity's PROBLEMS-VS-ALGORITHMS Problems

Run time analysis (Worst Case Big-O Notation) of solution

Get Time Taken to run using : time python <filename>

- Design choices -

  - This problem i used the Trie data structure to search for list of words in a tree filtered by character(s) prefix, solution uses the 0(n) complexity to sort the list while loop and ensuring it runs from 0 to n where n is the length of input list and return a list, after breaking out of the while loop

- TASK 5 : 0(n)

  - Space complexity analysis-
    - insertWord = 0(1)
    - getSuffixList = 0(1)

  - Logic explanation - Time complexity analysis-

  - Algorithm for Autocomplete with Tries algorithm :

    - create TrieNode class with is_word and children dictionary

    - create Trie class with 
        root,
        word list,
        insert function : 0(n),
        appendWordRecursion function : 0(n)
        getSuffixList function : 0 (1)
    - return suffix List 0(1)
  
  - Modular Algorithm :
    - Create Trie = 0(1)
    - Insert word in Trie = 0(n)
    - get suffix list = 0(1)
