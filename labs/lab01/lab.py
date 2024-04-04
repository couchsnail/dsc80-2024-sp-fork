# lab.py


from pathlib import Path
import io
import pandas as pd
import numpy as np


# ---------------------------------------------------------------------
# QUESTION 0
# ---------------------------------------------------------------------


def consecutive_ints(ints):
    if len(ints) == 0:
        return False

    for k in range(len(ints) - 1):
        diff = abs(ints[k] - ints[k+1])
        if diff == 1:
            return True

    return False


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def median_vs_mean(nums):
    sorted_list = sorted(nums)
    sorted_len = len(sorted_list)
    
    if sorted_len%2==0:
        median = (sorted_list[sorted_len//2]+sorted_list[sorted_len//2-1])//2
    else:
        median = sorted_list[sorted_len//2]

    sum = 0
    for i in nums:
        sum += i
    
    if median <= sum/sorted_len:
        return True
    else:
        return False


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def n_prefixes(s, n):
    result = ''
    for i in range(n, 0, -1):
        result += s[:i]
    return result


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def exploded_numbers(ints, n):
    result = []
    for i in ints:
        current = ''
        index = n
        while index > 0:
            cur_int = str(i - (index))
            current += cur_int.zfill(n) + " "
            index -= 1
        current += str(i).zfill(n) + " "
        index = 1
        while index <= n:
            cur_int = str(i + (index))
            current += cur_int.zfill(n) + " "
            index += 1
        result.append(current[:-1])
    return result


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def last_chars(fh):
    result = str()
    for line in fh:
        result += line.strip()[-1]
    return result


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def add_root(A):
    ...

def where_square(A):
    ...


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def filter_cutoff_loop(matrix, cutoff):
    ...


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def filter_cutoff_np(matrix, cutoff):
    ...


# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


def growth_rates(A):
    ...

def with_leftover(A):
    ...


# ---------------------------------------------------------------------
# QUESTION 8
# ---------------------------------------------------------------------


def salary_stats(salary):
    ...


# ---------------------------------------------------------------------
# QUESTION 9
# ---------------------------------------------------------------------


def parse_malformed(fp):
    ...
