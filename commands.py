import collections
import math
import fractions
from functools import reduce

letters = list("abcdefghijklmnopqrstuvwxyz")
numbers = list("0123456789")

def is_digit_value(value):
    value = str(value)
    try:
        for X in value:
            if numbers.__contains__(X):
                continue
            else:
                return False
        return True
    except:
        return False


def flatten(x):
    if isinstance(x, collections.Iterable):
        return [a for i in x for a in flatten(i)]
    else:
        return [x]


def is_alpha_value(value):
    value = str(value)
    try:
        for X in value:
            if letters.__contains__(X.lower()):
                continue
            else:
                return False
        return True
    except:
        return False


def convert_to_base(n, base):
    """convert positive decimal integer n to equivalent in another base (2-36)"""

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!\"#$%&'()*+/:;<=>?@[\]^_`{|}" \
             "\u20AC\u201A\u0192\u201E\u2026\u2020\u2021\u02C6\u2030\u0160\u2039\u0152\u017D\u00ED\u00EE" \
             "\u2022\u2013\u2014\u00EF\u2122\u0161\u203A\u0153\u017E\u0178\u00A1\u00A2\u00A3\u00A4\u00A5" \
             "\u00A6\u00A7\u00A8\u00A9\u00AA\u00AB\u00AC\u00AE\u00AF\u00B0\u00B1\u00B2\u00B3\u00B4\u00B5" \
             "\u00B6\u00B7\u00B8\u00B9\u00BA\u00BB\u00BC\u00BD\u00BE\u00BF\u00C0\u00C1\u00C2\u00C3\u00C4" \
             "\u00C5\u00C6\u00C7\u00C8\u00C9\u00CA\u00CB\u00CC\u00CD\u00CE\u00CF\u00D0\u00D1\u00D2\u00D3" \
             "\u00D4\u00D5\u00D6\u00D7\u00D8\u00D9\u00DA\u00DB\u00DC\u00DD\u00DE\u00DF\u00E0\u00E1\u00E2" \
             "\u00E3\u00E4\u00E5\u00E6\u00E7\u00E8\u00E9\u00EA\u00EB\u00EC"

    if int(n) == 0:
        return "0"

    try:
        n = int(n)
        base = int(base)
    except:
        return ""

    if n < 0 or base < 2 or base > 190:
        return ""

    s = ""
    while 1:
        r = n % base
        s = digits[int(r)] + s
        n = n / base
        if n == 0:
            break

    try:
        while s[0] == "0":
            s = s[1:]
    except:
        0

    return s


def convert_from_base(n, base):

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!\"#$%&'()*+/:;<=>?@[\]^_`{|}" \
             "\u20AC\u201A\u0192\u201E\u2026\u2020\u2021\u02C6\u2030\u0160\u2039\u0152\u017D\u00ED\u00EE" \
             "\u2022\u2013\u2014\u00EF\u2122\u0161\u203A\u0153\u017E\u0178\u00A1\u00A2\u00A3\u00A4\u00A5" \
             "\u00A6\u00A7\u00A8\u00A9\u00AA\u00AB\u00AC\u00AE\u00AF\u00B0\u00B1\u00B2\u00B3\u00B4\u00B5" \
             "\u00B6\u00B7\u00B8\u00B9\u00BA\u00BB\u00BC\u00BD\u00BE\u00BF\u00C0\u00C1\u00C2\u00C3\u00C4" \
             "\u00C5\u00C6\u00C7\u00C8\u00C9\u00CA\u00CB\u00CC\u00CD\u00CE\u00CF\u00D0\u00D1\u00D2\u00D3" \
             "\u00D4\u00D5\u00D6\u00D7\u00D8\u00D9\u00DA\u00DB\u00DC\u00DD\u00DE\u00DF\u00E0\u00E1\u00E2" \
             "\u00E3\u00E4\u00E5\u00E6\u00E7\u00E8\u00E9\u00EA\u00EB\u00EC"

    n = str(n)[::-1]
    r = 0
    range_v = 0

    for Q in n:
        r += digits.index(Q) * base ** range_v
        range_v += 1

    return r


def is_prime(n):
    if n < 2:
        return 0
    if n == 2 or n == 3:
        return 1
    if n < 2 or n % 2 == 0:
        return 0
    if n < 9:
        return 1
    if n % 3 == 0:
        return 0
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return 0
        if n % (f + 2) == 0:
            return 0
        f += 6

    return 1


def combinations(n, r):
    n = int(n)
    r = int(r)
    return int(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))


def permutations(n, r):
    n = int(n)
    r = int(r)
    return int(math.factorial(n) / math.factorial(n - r))


def prime_factorization(n):
    n = int(n)
    list_of_factors = []

    if n < 2:
        return []
    else:
        if n == 2:
            return [2]
        else:
            for Q in range(2, n + 1):
                if is_prime(Q):
                    if n % Q == 0:
                        list_of_factors.append(Q)
    return list_of_factors


def get_letter(n):
    n = int(n)
    if n == 1:return "A"
    if n == 2:return "B"
    if n == 3:return "C"
    if n == 4:return "D"
    if n == 5:return "E"
    if n == 6:return "F"
    if n == 7:return "G"
    if n == 8:return "H"
    if n == 9:return "I"
    if n == 10:return "J"
    if n == 11:return "K"
    if n == 12:return "L"
    if n == 13:return "M"
    if n == 14:return "N"
    if n == 15:return "O"
    if n == 16:return "P"
    if n == 17:return "Q"
    if n == 18:return "R"
    if n == 19:return "S"
    if n == 20:return "T"
    if n == 21:return "U"
    if n == 22:return "V"
    if n == 23:return "W"
    if n == 24:return "X"
    if n == 25:return "Y"
    if n == 26:return "Z"
    return None


def prime_factorization_duplicates(n):
    n = int(n)
    list_of_factors = []

    if n < 2:
        return []
    else:
        if n == 2:
            return [2]
        else:
            for Q in range(2, n + 1):
                if is_prime(Q):
                    while n % Q == 0:
                        list_of_factors.append(Q)
                        n = int(int(n) / int(Q))

    return list_of_factors


def prime_factorization_powers(n):
    n = int(n)
    list_of_factors = []

    if n < 2:
        return []
    else:
        if n == 2:
            return [1]
        else:
            for Q in range(2, n + 1):
                if is_prime(Q):
                    value = 0
                    while n % Q == 0:
                        value += 1
                        n = int(int(n) / int(Q))
                    list_of_factors.append(value)

    try:
        while list_of_factors[len(list_of_factors) - 1] == 0:
            list_of_factors.pop()
    except:0

    return list_of_factors


def get_nth_prime(n):
    n = int(n) + 1
    current_prime = 2
    while n > 0:
        if is_prime(current_prime):
            n -= 1
            if n > 0:
                current_prime += 1
        else:
            current_prime += 1
    return current_prime


def get_all_substrings(input_string):
  length = len(input_string)
  return [input_string[i:j+1] for i in range(length) for j in range(i,length)]


def command_gcd(numbers):
    if 0 in numbers:
        return 0
    try:
        return reduce(fractions.gcd, numbers)
    except:
        return 1