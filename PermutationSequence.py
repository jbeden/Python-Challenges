"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
"""

import math

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
        if n == 1:
            return "1"
        
        n_set = [i+1 for i in range(n)]
        
        seq = ""
        a = 0
        b = k
        c = 1
        
        for _ in range(n):
            while b > math.factorial(n-c) and n-c != 0:
                a += 1
                b -= math.factorial(n-c)

            seq += str(n_set[a])
            n_set.remove(n_set[a])

            a = 0
            c += 1
        
        return seq
