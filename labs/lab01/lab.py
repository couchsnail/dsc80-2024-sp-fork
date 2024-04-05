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
    return A + np.sqrt(np.arange(len(A)))

def where_square(A):
    return A==np.sqrt(A**2)


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def filter_cutoff_loop(matrix, cutoff):
    result = []
    valid_col = []
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix[i])):
            sum += matrix[i][j]
        mean = sum / len(matrix)
        if mean > cutoff:
            valid_col.append(i)
    
    for v in valid_col:
        current_row = []
        for row in matrix:
            current_row.append(row[v])
        result.append(current_row)
    
    return np.array(result)


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def filter_cutoff_np(matrix, cutoff):
    valid = np.mean(matrix,axis=0)>cutoff
    return matrix[:,valid]


# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


def growth_rates(A):
    return np.round(np.diff(A)/A[:-1],2)

def with_leftover(A):
    differences = np.cumsum(20 % A)>=A
    return np.where(differences==True)[0][0]


# ---------------------------------------------------------------------
# QUESTION 8
# ---------------------------------------------------------------------


def salary_stats(salary):
    req_values = []
    indexes = np.array(['num_players','num_teams', 'total_salary', 'highest_salary', 'avg_los', 'fifth_lowest', 'duplicates', 'total_highest'])
    #Number of players
    req_values.append(salary.shape[0])
    #Number of Teams
    req_values.append(salary.groupby(by='Team').count().shape[0])
    #Total salary amount for all players
    req_values.append(salary['Salary'].sum())
    #Name of the player with the highest salary
    req_values.append(salary.sort_values(by='Salary',ascending=False)['Player'][0])
    #Average salary of 'Los Angeles Lakers', rounded to 2 decimal players
    lakers = salary[salary['Team']=='Los Angeles Lakers']
    req_values.append(np.round(np.mean(lakers['Salary']),2))
    #Name and team of the player who has the fifth lowest salary, separated by a comma and a space
    fifth_player = salary.sort_values(by='Salary',ascending=True)['Player'][4] + ', ' + salary.sort_values(by='Salary',ascending=False)['Team'][4]
    req_values.append(fifth_player)
    #Boolean that is True if there any duplicate last names and False otherwise
    def getLastName(name):
        first_space = name.index(' ')
        if first_space!=name.rindex(' '):
            second_space = name.rindex(' ')
            return name[first_space+1:second_space]
        else:
            return name[first_space+1:]
    names = salary['Player'].apply(getLastName).duplicated()
    req_values.append(bool(True in names))
    #Total salary of team with highest paid player
    highest_team = salary.sort_values(by='Salary',ascending=False)['Team'][0]
    req_values.append(salary[salary['Team']==(highest_team)]['Salary'].sum())
    return pd.Series(req_values, indexes)


# ---------------------------------------------------------------------
# QUESTION 9
# ---------------------------------------------------------------------


def parse_malformed(fp):
    ...
