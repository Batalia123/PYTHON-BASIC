"""
Write function which reads a number from input nth times.
If an entered value isn't a number, ignore it.
After all inputs are entered, calculate an average entered number.
Return string with following format:
If average exists, return: "Avg: X", where X is avg value which rounded to 2 places after the decimal
If it doesn't exists, return: "No numbers entered"
Examples:
    user enters: 1, 2, hello, 2, world
    >>> read_numbers(5)
    Avg: 1.67
    ------------
    user enters: hello, world, foo, bar, baz
    >>> read_numbers(5)
    No numbers entered

"""


def read_numbers(n: int) -> str:
    input_values = [input() for _ in range(n)]
    flag = True
    output_values = [int(i) for i in input_values if i.isnumeric()]
    #return input_values[1].isnumeric()
    return "Avg: {}".  format(round(sum(output_values) / len(output_values), 2)) if output_values else "No Numbers entered"


