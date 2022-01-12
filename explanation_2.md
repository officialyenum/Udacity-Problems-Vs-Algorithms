# Udacity-PROBLEMS-VS-ALGORITHMS

Submission to Udacity's PROBLEMS-VS-ALGORITHMS Problems

Run time analysis (Worst Case Big-O Notation) of solution

Get Time Taken to run using : time python <filename>


- Design choices -
  - This problem requires that you Find the index by searching in a rotated sorted array. my solution uses the binary search recursive algorithm with 0(log n) complexity to find pivot and use that pivot to recursively search the array using the binary search recursion

- TASK 2 : 0(log n)

  - Space complexity analysis-
    - input list = 0(n)
    - number = 0(1)
    - pivot_index = 0(1)

  - Logic explanation - Time complexity analysis-
  - Algorithm for Rotated Array Search Function :
    - find pivot index O(log n)
    - if not found traverse through the whole input list using binary_search algorithm 0(log n)
    - if value in input list pivot == target number return pivot index O(1)
    - if value in input list pivot index < target number traverse 0 to pivot index minus 1(left side) using binary search O(log n)
    - if value in input list pivot index > target number traverse pivot index plus 1 to length of input list - 1(right side) using binary search O(log n)
