"""
File: boggle.py
Name: Caren Yang
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
from typing import List

FILE = 'dictionary.txt'
dic = []


def main():
    """
    TODO:
    """
    start = time.time()
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    row = [row1,
           row2,
           row3,
            row4]
    read_dictionary()
    row1 = input('1 row of letters:').split()
    row.append(row1)
    row2 = input('1 row of letters:').split()
    row.append(row2)
    row3 = input('1 row of letters:').split()
    row.append(row3)
    row4 = input('1 row of letters: ').split()
    row.append(row4)
    for i in range(len(row)):
        for j in range(len(row)):
            get_neighbors(row, i, j)

    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')




def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    with open(FILE, 'r') as f:
        for line in f:
            vocab = line.strip()
            dic.append(vocab)
    return dic


def get_neighbors(row, x, y):
    get_neighbors_helper(row, (x, y), [], row[x][y], [])


def get_neighbors_helper(row, cur_index, ans_lst, current_str, index_lst):
    if len(current_str) >= 4 and current_str in dic:
        if current_str not in ans_lst:
            print('Found:' + current_str)
            ans_lst.append(current_str)

    else:
        for i in range(-1, 2):
            for j in range(-1, 2):

                new_x = cur_index[0] + i
                new_y = cur_index[1] + j

                if 4 > new_x >= 0 and 4 > new_y >= 0:
                    if (new_x, new_y) not in index_lst:

                        #choose
                        current_str += row[new_x][new_y]  #(x, y)
                        index_lst.append(new_x, new_y)

                        #explore
                        if has_prefix(current_str):
                            get_neighbors_helper(row, (new_x, new_y), ans_lst, current_str, index_lst)

                        #unchoose
                        current_str = current_str[:-1]
                        index_lst.pop()


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for current_str in dic:
        if current_str == sub_s:
            return True
        return False


if __name__ == '__main__':
    main()
