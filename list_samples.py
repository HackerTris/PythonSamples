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




    

    

    
