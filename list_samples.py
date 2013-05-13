""" Contains code for Python list sample snippets.

"""

def list_swap_min_max (a_list):
    """ Swap min and max values in the list.
    Account for multiple min and max values.

    """

    min_val=min(a_list)
    max_val=max(a_list)

    # get list of indexes that hold the min value

    min_indexes=[i for i,x in enumerate(a_list) if x == min_val]

    max_indexes=[i for i,x in enumerate(a_list) if x == max_val]
    
    print("The min indexes are: ",min_indexes)
    print("The max indexes are: ",max_indexes)

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

    print("The length is: ",len(test_string))
 
    for i in reversed(range(0,len(test_string))):
        rev_string=rev_string+test_string[i]    
        
    return rev_string


    

    

    
