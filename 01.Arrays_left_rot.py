#!/usr/bin/python

# A left rotation operation on an array of size  shifts each of the array's elements  unit to the left. For example, if  left rotations are performed on array , then the array would become .

# Given an array of  integers and a number, , perform  left rotations on the array. Then print the updated array as a single line of space-separated integers.

# Input Format

# The first line contains two space-separated integers denoting the respective values of  (the number of integers) and  (the number of left rotations you must perform). 
# The second line contains  space-separated integers describing the respective elements of the array's initial state.

# Constraints

# Output Format

# Print a single line of  space-separated integers denoting the final state of the array after performing  left rotations.

# Sample Input

# 5 4
# 1 2 3 4 5
# Sample Output

# 5 1 2 3 4

def array_left_rotation(a, n, k):
    if n > 0:
        for i in range(0, k):
            x = a.pop(0)
            a.append(x)
        return a
  

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))