# Merge-sort
The program is the same as shown at the end of the Merge sort section, with the following changes:

Numbers are entered by a user in a separate helper function, read_nums(), instead of defining a specific list.
Output of the list has been moved to the function print_nums().
An output has been added to merge_sort(), showing the indices that will be passed to the recursive function calls.
Add code to the merge sort algorithm to count the number of comparisons performed.

Add code at the end of the program that outputs "comparisons: " followed by the number of comparisons performed (Ex: "comparisons: 12")

Hint: Use a global variable to count the comparisons.

Note: Take special care to look at the output of each test to better understand the merge sort algorithm.

Ex: When the input is:

3 2 1 5 9 8
the output is:

unsorted: 3 2 1 5 9 8

0 2 | 3 5
0 1 | 2 2
0 0 | 1 1
3 4 | 5 5
3 3 | 4 4

sorted:   1 2 3 5 8 9
comparisons: 8
