""""
author : Dhruvraj Lathiya
Description : Solution of 6 mostly asked interview questions from 0/1 Kanpsack.
Note : "Different functions for each problem is not created.
"""

import copy
import numpy as np
import functools as func

# SUBSET SUM PROBLEM
def subset_sum(arr, t_sum, count_subset=False, give_mat=False):
    mat = np.zeros((len(arr) + 1, t_sum + 1)) * -1

    for i in range(len(arr)+1):
        for j in range(0, t_sum+1):
            if i == 0 and j != 0:
                mat[0][j] = 0
            elif j == 0:
                mat[i][0] = 1

            elif arr[i-1] <= j:
                k = mat[i-1][j - arr[i-1]]
                o = mat[i-1][j]

                if count_subset:
                    mat[i][j] = k+o
                else:
                    mat[i][j] = k or o

            else:
                mat[i][j] = mat[i-1][j]

    if give_mat:
        return mat

    return mat[len(arr)][t_sum]


# MINIMUM SUBSET SUM PROBLEM
# COUNT NO OF SUBSETS WITH GIVEN DIFFERENCE
# TARGET SUM : Give +, - to values such that end result is 1 # It is same as finding subset with  difference 1
# It is Just that Question formation seems complex

def min_subset_sum(arr, given_diff=-1):
    set_sum = func.reduce(lambda a, b: a + b, arr)
    mat = subset_sum(arr, set_sum, give_mat=True)

    val = []
    temp_sum = copy.deepcopy(set_sum)
    for i in range(len(mat[-1])):
        if i <= (temp_sum // 2):
            if mat[-1][i] == 1:
                val.append(i)
        else:
            break

    subtract = [abs(temp_sum - (2 * i)) for i in val if i != 0]

    if given_diff+1:
        p_sum = abs(given_diff - set_sum) // 2
        return subset_sum(arr, p_sum, count_subset=True)

    return min(subtract)


# EQUAL SUMS OF 2 SUBSETS PROBLEM
def equal_sum_part(arr):
    set_sum = func.reduce(lambda a, b: a+b, arr)

    if set_sum % 2 != 0:
        return "ODD TOTAL SUM : Equal Sum Partition Cannot be Done"

    if set_sum % 2 == 0:
        a = subset_sum(arr, set_sum)
        if a == 1:
            return "Equal Sets is Possible"
        else:
            return "Equal Sets Not Possible"


if __name__ == "__main__":
    arr = [1, 2, 4, 5, 6, 8, 9, 10]

    print(subset_sum(arr, 7))   # O/P ==> 0 / 1 represent Boolean values  ==> subset with sum 7 is possible(1 - True)
    print(subset_sum(arr, 6, True))  # O/P ==> No. of subsets with sum 6
    print(min_subset_sum(arr))  # Gives min difference between 2 sets that can be formed from an array
    print(min_subset_sum(arr, given_diff=8))  # Gives no of possible subsets from array with given diff
    print(min_subset_sum(arr, given_diff=1))  # Target sum = 1
    print(equal_sum_part(arr))  # Gives output whether 2 sets with equal values can be formed or not

