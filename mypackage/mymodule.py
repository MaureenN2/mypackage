def top_n (items,n):
    """
    Return top n items in an array, in descending order.

    Args:
        items(array): list or array_like object containing numeric values
        n(int): number of top items to return

    Returns:
        array: top n items, in descending order.

    Example:
        >>> top_n([8,9,5,3,2],3)
        [9,8,5]
    """

    for i in range(n): #keep sorting until we have top n items
        for j in range(len(items)-1-i):

            if items [j] > items[j+1]: #if this item is bigger than the next item
                items[j], items[j+1] = items[j+1], items[j] #swap the two!
    
    #get the last two items
    top_n = items[-n:]

    #return in descending order
    return top_n[::-1]