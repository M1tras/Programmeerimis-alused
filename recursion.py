"""Recursion exercises."""
import sys
sys.set_int_max_str_digits(6000)


def loop_reverse(s: str) -> str:
    """
    Reverse a string using a loop.

    loop_reverse("hey") => "yeh"
    loop_reverse("aaa") => "aaa"
    loop_reverse("") => ""
    loop_reverse("1") => "1"

    :param s: input string
    :return: reversed input string
    """
    new_string = ""
    for i in range(len(s)-1, -1, -1):
        new_string += s[i]
    return new_string
    pass


def recursive_reverse(s: str) -> str:
    """
    Reverse a string using recursion.

    recursive_reverse("hey") => "yeh"
    recursive_reverse("aaa") => "aaa"
    recursive_reverse("") => ""
    recursive_reverse("1") => "1"

    :param s: input string
    :return: reversed input string
    """
    if not s:
        return s
    else:
        return s[-1] + recursive_reverse(s[:-1])
    pass


def loop_sum(n: int) -> int:
    """
    Calculate the sum of all numbers up to n (including n) using a loop.

    loop_sum(0) => 0
    loop_sum(3) => 6
    loop_sum(5) => 15

    :param n: the last number to add to the sum
    :return: sum
    """
    total = 0
    for number in range(0, n + 1):
        total += number
    return total
    pass


def recursive_sum(n: int) -> int:
    """
    Calculate the sum of all numbers up to n (including n) using recursion.

    recursive_sum(0) => 0
    recursive_sum(3) => 6
    recursive_sum(5) => 15

    :param n: the last number to add to the sum
    :return: sum
    """
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n - 1)
    pass


def sum_digits_recursive(number: int) -> int:
    """
    Return the sum of the digits in number.

    Given a non-negative int n, return the sum of its digits recursively (no loops).

    sum_digits_recursive(123) => 6
    sum_digits_recursive(1) => 1
    sum_digits_recursive(0) => 0
    sum_digits_recursive(999) => 27

    :param number: non-negative number
    :return: sum of digits in the number
    """
    if number // 10 == 0:
        return number
    else:
        return sum_digits_recursive(number // 10) + number % 10
    pass


def pair_star_recursive(s: str) -> str:
    """
    Add star between identical adjacent chars.

    Given a string, compute recursively a new string
    where identical chars that are adjacent in the original string
    are separated from each other by a "*".

    :param s: input string
    :return: string with stars between identical chars.
    """
    if len(s) <= 1:
        return s
    elif s[0] == s[1]:
        return s[0] + "*" + pair_star_recursive(s[1:])
    else:
        return s[0] + pair_star_recursive(s[1:])
    pass
