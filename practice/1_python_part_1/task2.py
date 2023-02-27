"""
Write function which updates dictionary with defined values but only if new value more then in dict
Restriction: do not use .update() method of dictionary
Examples:
    >>> set_to_dict({'a': 1, 'b': 2, 'c': 3}, a=0, b=4)  # only b updated because new value for a less then original value
    {'a': 1, 'b': 4, 'c': 3}
    >>> set_to_dict({}, a=0)
    {a: 0}
    >>> set_to_dict({'a': 5})
    {'a': 5}
"""
from typing import Dict


def set_to_dict(dict_to_update: Dict[str, int], **items_to_set) -> Dict:
    for a in items_to_set:
        if a not in dict_to_update or dict_to_update[a] < items_to_set[a]: dict_to_update[a] = items_to_set[a]
    return dict_to_update

set_to_dict({'a': 1, 'b':2}, b=4, a=0)
set_to_dict({}, a=5) 
