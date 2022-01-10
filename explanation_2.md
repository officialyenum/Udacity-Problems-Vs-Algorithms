# Udacity-PROBLEMS-VS-ALGORITHMS

Submission to Udacity's PROBLEMS-VS-ALGORITHMS Problems

Run time analysis (Worst Case Big-O Notation) of solution

Get Time Taken to run using : time python <filename>

- How i solved this problem ?

This problem requires that you input a number and return back another number. my solution uses the 0(1) complexity to input a number modify that number and return the number

- TASK 2 : 0(log n)

  - Space Complexities

    - input list = 0(n)
    - number = 0(1)
    - pivot_index = 0(1)

  - Algorithm for Rotated Array Search Function :
    - find pivot index O(log n)
    - if not found traverse through the whole input list using binary_search algorithm 0(log n)
    - if value in input list pivot == target number return pivot index O(1))
    - if value in input list pivot index < target number traverse 0 to pivot index minus 1 using binary search O(log n)
    - if value in input list pivot index > target number traverse pivot index plus 1 to length of input list - 1 using binary search O(log n)
