
# Udacity-PROBLEMS-VS-ALGORITHMS

Submission to Udacity's PROBLEMS-VS-ALGORITHMS Problems

Run time analysis (Worst Case Big-O Notation) of solution

Get Time Taken to run using : time python <filename>


- Design choices -
  - This problem requires that you sort the list and get two max sum values from that list. my solution uses the 0(n log n) complexity to sort the list using merge sort algorithm and 0(n) to traverse the sorted list and return a list of Two maximum sums values

- TASK 3 : 0(n log n)

  - Space complexity analysis-
    - leftSum = 0(1)
    - rightSum = 0(1)
    - input_list = 0(n)
    - sorted_digits = 0(n)
    - n = 0(1)

  - Logic explanation - Time complexity analysis-
  - Algorithm for Rearrange Digits Function :
    - get sorted digits using merge sort O(n log n)
    - traverse through the sorted list and modify left and right sum to get Two maximum sums 0(n)
    - return list of Two maximum sums 0(n)
