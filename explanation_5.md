# Udacity-PROBLEMS-VS-ALGORITHMS

Submission to Udacity's PROBLEMS-VS-ALGORITHMS Problems

Run time analysis (Worst Case Big-O Notation) of solution

Get Time Taken to run using : time python <filename>

- Design choices -

  - This problem i used the Trie data structure to search for list of words in a tree filtered by character(s) prefix, solution uses the 0(n) complexity to sort the list while loop and ensuring it runs from 0 to n where n is the length of input list and return a list, after breaking out of the while loop

- TASK 5 : 0(n)

  - Logic explanation - Time complexity analysis - Space complexity analysis -

  - Algorithm for Autocomplete with Tries algorithm :

    - create TrieNode class with is_word bool and children dictionary

    - create Trie class with
      - root,
      - word list,
      - insert function,
      - appendWordRecursion function,
      - getSuffixList function,

  - Modular Algorithm for Trie class:

    - Insert word in Trie class

      - Space : 0(n) where n is the length of the string to be inserted since we need to perform n iterations.

      - Time : 0(n) where n is the length of the word since n new nodes are added which takes up space O(n).

    - append Word Trie class

      - Space : 0(n) maximum depth of trie is proportional to n,
      - Time : 0(n) traverse deep into the trie tree and append word to word list where is_word is true

    - get suffix list Trie class
      - Space : 0(1)
      - Time : 0(n) In this case, the time complexity will be O(n) where n is the length of the key/word to be searched.
