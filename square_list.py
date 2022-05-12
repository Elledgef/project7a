# Author: Faith Elledge
# Grithub username: Elledgef
# Date:5/11
# Description: Replaces original values with the squared values of those numbers

def square_list(lst):
    for i in range(len(lst)):
        lst[i] = lst[i] * lst[i]

