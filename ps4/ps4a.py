# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import math
def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    first_ele = 0
    last_ele = len(sequence)
    ans_list = []
    a = list(sequence)
    if first_ele == last_ele:
        ans_list.append(a)
    else:
        for i in range(first_ele, last_ele):
            (a[first_ele], a[i]) = (a[i], a[first_ele])
            first_ele += 1
            get_permutations(a)
            (a[first_ele], a[i]) = (a[i], a[first_ele])
    if (len(ans_list) == math.factorial(len(sequence))):
        return ans_list  

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    print(get_permutations("ABC"))
    
