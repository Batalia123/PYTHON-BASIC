"""
Write function which deletes defined element from list.
Restriction: Use .pop method of list to remove item.
Examples:
    >>> delete_from_list([1, 2, 3, 4, 3], 3)
    [1, 2, 4]
    >>> delete_from_list(['a', 'b', 'c', 'b', 'd'], 'b')
    ['a', 'c', 'd']
    >>> delete_from_list([1, 2, 3], 'b')
    [1, 2, 3]
    >>> delete_from_list([], 'b')
    []
"""
from typing import List, Any


def delete_from_list(list_to_clean: List, item_to_delete: Any) -> List:
    indexes_to_pop = [i for i in range(len(list_to_clean)) if list_to_clean[i]==item_to_delete]
    for ind in indexes_to_pop[::-1]: list_to_clean.pop(ind)
    return list_to_clean

delete_from_list([1, 2, 3, 4, 3], 3)
delete_from_list(['a', 'b', 'c', 'b', 'd'], 'b')
delete_from_list([1, 2, 3], 'b')
