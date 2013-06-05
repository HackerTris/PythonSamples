""" Contains code for Python sample sample programs.
The purpose of this module is to implement a few of the classic sort algorithms. Python
does have  rich set of sorting capabilities built in, so it is quite probable
that we would not be using many of these algorithims in actual practice.

"""

def insert_sort_val (working_list,last_sorted,val):
    """Insert a value and maintain the sorted nature of the list,
    up to the last sorted value.  (There may be items in the list after
    the sorted value which are not sorted.)  The items in the list must have
    comparision operations implemented.

    Sorts in place; that is, the working_list is sorted in place, with the new
    value to insert.

    Assume the list as no duplicates and size of the list remains constant

    Example:  1,4,8,9,11,15 ,7,12,13,6 last_sorted: 5 (5th position in the 0 based list)

    This function could be used as a helper function to insert_sort_list
    
    """
    size=len(working_list)
    print("The length is: ",size)
    
    for i in range(last_sorted):
        if val < working_list[i]:
            # we found where to put it
            for j in 
            

def insert_sort_list(working_list):
    """  Sort an entire list using the insert sort algorithm
    """
    pass

