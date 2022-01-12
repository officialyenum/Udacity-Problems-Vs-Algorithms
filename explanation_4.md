

# Udacity-PROBLEMS-VS-ALGORITHMS

Submission to Udacity's PROBLEMS-VS-ALGORITHMS Problems

Run time analysis (Worst Case Big-O Notation) of solution

Get Time Taken to run using : time python <filename>

- Design choices -
  - This problem requires that you sort the list in a single traversal, solution uses the 0(log n) complexity to sort the list while loop and ensuring it runs from 0 to n/2 where n is the length of input list and return a list the list after breaking out of the while loop

- TASK 4 : 0(log n)

  - Space complexity analysis-
    - start_pos_0 = 0(1)
    - end_pos_2 = 0(1)
    - input_list = 0(n)
    - front_index = 0(1)
    - count = 0(1)

  - Logic explanation - Time complexity analysis-
  - Algorithm for Dutch National Flag Problem using sort 012 algorithm :
    - traverse from front_index to end_pos_2 input list indexes 0(log n) using while loop till front index is <= end_pos_2
    - return Input List 0(n)
