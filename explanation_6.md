



# Udacity-PROBLEMS-VS-ALGORITHMS

Submission to Udacity's PROBLEMS-VS-ALGORITHMS Problems

Run time analysis (Worst Case Big-O Notation) of solution

Get Time Taken to run using : time python <filename>


- Design choices -
  - This problem requires that i traverse through a list and update the max and min variables, solution uses the 0(n) complexity to retrieve the max and min values

- TASK 6 : 0(n)

  - Space complexity analysis-
    - min_value = 0(1)
    - max_value = 0(1)
    - ints = 0(n)

  - Logic explanation - Time complexity analysis-
  - Algorithm for Get Min Max :
    - if length of int list is between 0 - 2 return tuple of min and max value 0(1)
    - traverse throught int list 0(n)
        - if current value <= min update min 0(1)
        - if current value >= max update max 0(1)
    - return tuple of min and max value 0(1)
