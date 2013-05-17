""" Contains code for Python list sample programs.

What is this?  Well, I worked through many of the coding problems in "Cracking he
Coding Interview", by Gayle McDowell, except I did these programming problems
in Python, rather than C++ or Java.

Each category of samples also has a unit test program to go along with it.  I
used test driven development to develop the algorithms in each of these sample
programs.

"""

import copy  # used to make deep copies of lists

def list_swap_min_max (a_list):
    """ Swap min and max values in the list.
    Account for multiple min and max values.

    """

    min_val=min(a_list)
    max_val=max(a_list)

    # get list of indexes that hold the min value

    min_indexes=[i for i,x in enumerate(a_list) if x == min_val]

    max_indexes=[i for i,x in enumerate(a_list) if x == max_val]
    

    for i in range(len(min_indexes)):
        a_list[min_indexes[i]]=max_val

    for i in range(len(max_indexes)):
        a_list[max_indexes[i]]=min_val

    return a_list

def unique_chars(test_string):
    """ Test if a string has unique chars.
    Case sensitive; l<> L

    The algorithm we will use is to take the first char, and then look
    for occurences in the next slice of the string.  We will keep doing this until
    the string is exhausted or we found a match, indicating that the string does
    not consist of unique chars.

    Blanks are not counted! 
    """
    test_string="".join(test_string.split())  #squeeze out the white space
    unique=True  # assume true to start with...
    test_char=test_string[0]
    test_slice=test_string[1:]


    while len(test_slice) > 0:
        if test_slice.find(test_char)>=0:
            unique=False
            break
        test_char=test_slice[0]
        test_slice=test_slice[1:]
    
    return unique
    

def reverse_string(test_string):
    """Reverse a string. Will do this two different ways; the easy python way
    and the brute force way.

    """

    #easy python way

    #rev_string=test_string[::-1]

    #brute force way
    rev_string=""

 
    for i in reversed(range(0,len(test_string))):
        rev_string=rev_string+test_string[i]    
        
    return rev_string


def permutation_string(string1,string2):
    """ ReturnsTrue if the strings are permutations of eachother

    """

    s1="".join(sorted(string1))
    s2="".join(sorted(string2))
    return (s1==s2)


def matrix_transform(matrix):
    """

    some notes
    determine num rows and columns
    for each row, look for 0's.  Use index to find the first 0.  Then slice the
    list and look for next 0.  So if the row is [1,0,2], first 0 index is at 1. Then
    slice the list and look for more:  row[2:]

    so, for each row, look for all 0's in the row.  Then remeber the position, and for each row
    afer the current row, 0 out in the column postion.   Always build a new matrix because
    you don't want to work on a partially transformed one.
    
    """
    
    num_rows=len(matrix)
    
    #each of the internal lists must consist of the same
    #number of elements... but not checking this for now
    
    num_cols=len(matrix[0])

    #initialize the transformed matrix to be a copy of the matrix.
    #A deep copy is needed, rather than just initializing another variable.

    transformed_matrix=copy.deepcopy(matrix)
    
    for row in range(0,num_rows):       
        for column in range(0,num_cols):
            if matrix[row][column]==0:              
                transformed_matrix[row]=[0,0,0]
                for r in range(row+1,num_rows):
                    transformed_matrix[r][column]=0
                for r in range(0,row):
                    transformed_matrix[r][column]=0
         
    return transformed_matrix

    
